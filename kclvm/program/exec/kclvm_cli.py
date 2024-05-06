# Copyright 2022 The KCL Authors. All rights reserved.

import os
import sys
import platform
import typing
import json
import inspect

from ctypes import *

import kclvm.compiler.extension.plugin.plugin as kcl_plugin
import kclvm.kcl.info as kcl_info
import kcl_lib.api.spec_pb2 as pb2
import kclvm.api.object as objpkg
import kcl_lib.api as api
from ruamel.yaml import YAML

# Ruamel YAML instance
ruamel_yaml = YAML(typ="unsafe", pure=True)
# Convert None to null
ruamel_yaml.representer.add_representer(
    type(None),
    lambda dumper, data: dumper.represent_scalar("tag:yaml.org,2002:null", "null"),
)

# Create the api instance
_api = api.API()

kclvm_PANIC_INFO_KEY = "__kcl_PanicInfo__"

# Using kclvm rust cli PATH or current exec path.
_exe_root = os.path.dirname(
    os.environ.get("KCLVM_CLI_BIN_PATH") or os.path.dirname(sys.executable)
)
_cli_dll = None


def init_cli_dll():
    global _cli_dll

    if _cli_dll:
        return

    if platform.system() == "Darwin":
        if os.path.exists(f"{_exe_root}/lib/libkclvm_cli_cdylib.dylib"):
            _cli_dll_path = f"{_exe_root}/lib/libkclvm_cli_cdylib.dylib"
        else:
            _cli_dll_path = f"{_exe_root}/bin/libkclvm_cli_cdylib.dylib"
    elif platform.system() == "Linux":
        if os.path.exists(f"{_exe_root}/lib/libkclvm_cli_cdylib.so"):
            _cli_dll_path = f"{_exe_root}/lib/libkclvm_cli_cdylib.so"
        else:
            _cli_dll_path = f"{_exe_root}/bin/libkclvm_cli_cdylib.so"
    elif platform.system() == "Windows":
        _cli_dll_path = f"{_exe_root}\\bin\\kclvm_cli_cdylib.dll"
    else:
        raise f"unknown os: {platform.system()}"
    _cli_dll = CDLL(_cli_dll_path)


class PluginContext:
    def __init__(self):
        self._plugin_dict: typing.Dict[str, any] = {}

    def call_method(self, name: str, args_json: str, kwargs_json: str) -> str:
        return self._call_py_method(name, args_json, kwargs_json)

    def _call_py_method(self, name: str, args_json: str, kwargs_json: str) -> str:
        try:
            return self._call_py_method_unsafe(name, args_json, kwargs_json)
        except Exception as e:
            return json.dumps({"__kcl_PanicInfo__": f"{e}"})

    def _get_plugin(self, plugin_name: str) -> typing.Optional[any]:
        if plugin_name in self._plugin_dict:
            return self._plugin_dict[plugin_name]

        module = kcl_plugin.get_plugin(plugin_name)
        self._plugin_dict[plugin_name] = module
        return module

    def _call_py_method_unsafe(
        self, name: str, args_json: str, kwargs_json: str
    ) -> str:
        dotIdx = name.rfind(".")
        if dotIdx < 0:
            return ""

        modulePath = name[:dotIdx]
        mathodName = name[dotIdx + 1 :]

        plugin_name = modulePath[modulePath.rfind(".") + 1 :]

        module = self._get_plugin(plugin_name)
        mathodFunc = None

        for func_name, func in inspect.getmembers(module):
            if func_name == kcl_info.demangle(mathodName):
                mathodFunc = func
                break

        args = []
        kwargs = {}

        if args_json:
            args = json.loads(args_json)
            if not isinstance(args, list):
                return ""
        if kwargs_json:
            kwargs = json.loads(kwargs_json)
            if not isinstance(kwargs, dict):
                return ""

        result = mathodFunc(*args, **kwargs)
        return json.dumps(result)


__plugin_context__ = PluginContext()
__plugin_method_agent_buffer__ = create_string_buffer(1024)


@CFUNCTYPE(c_char_p, c_char_p, c_char_p, c_char_p)
def plugin_method_agent(method: str, args_json: str, kwargs_json: str) -> c_char_p:
    method = str(method, encoding="utf-8")
    args_json = str(args_json, encoding="utf-8")
    kwargs_json = str(kwargs_json, encoding="utf-8")

    json_result = __plugin_context__.call_method(method, args_json, kwargs_json)

    global __plugin_method_agent_buffer__
    __plugin_method_agent_buffer__ = create_string_buffer(json_result.encode("utf-8"))
    return addressof(__plugin_method_agent_buffer__)


def kclvm_cli_native_run_dylib(args: pb2.ExecProgram_Args) -> objpkg.KCLResult:
    result: pb2.ExecProgram_Result = _api.exec_program(args)
    if result.err_message:
        raise Exception(result.err_message)

    if result.log_message:
        print(result.log_message)

    data = list(ruamel_yaml.load_all(result.yaml_result))

    return objpkg.KCLResult(data, os.path.abspath(args.k_filename_list[-1]))
