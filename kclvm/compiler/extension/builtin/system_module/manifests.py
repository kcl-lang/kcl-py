import io

import kclvm.compiler.extension.builtin.system_module.yaml as yaml


def KMANGLED_yaml_stream(data: list, opts: dict = {}) -> None:
    """This function is used to serialize the KCL object list into YAML output with the --- separator. It has two parameters:


    Parameters
    ----------
    + values - A list of KCL objects
    + opts - The YAML serialization options
        + sort_keys: Whether to sort the serialized data in the dictionary order of attribute names (the default is False).
        + ignore_private: Whether to ignore the attribute output whose name starts with the character _ (the default value is True).
        + ignore_none: Whether to ignore the attribute with the value of' None '(the default value is False).
        + sep: Set the separator between multiple YAML documents (the default value is "---").
    """
    if not data:
        return None
    sort_keys = opts.get("sort_keys", False)
    ignore_private = opts.get("ignore_private", True)
    ignore_none = opts.get("ignore_none", False)
    sep = opts.get("sep", "---")
    outputs = ""
    with io.StringIO() as buf:
        if data:
            for result in data[:-1]:
                if result:
                    buf.write(
                        yaml.KMANGLED_encode(
                            result,
                            sort_keys=sort_keys,
                            ignore_private=ignore_private,
                            ignore_none=ignore_none,
                        )
                    )
                    buf.write(f"{sep}\n")
            if data[-1]:
                buf.write(
                    yaml.KMANGLED_encode(
                        data[-1],
                        sort_keys=sort_keys,
                        ignore_private=ignore_private,
                        ignore_none=ignore_none,
                    )
                )
            outputs = buf.getvalue()

    from kclvm.vm.vm import VirtualMachine

    VirtualMachine.hook_output = list(yaml.KMANGLED_load_all(outputs))
    return None
