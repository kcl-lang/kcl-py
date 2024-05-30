#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pkg_resources import require
import setuptools

# Steps:
# 1. modify kclvm version in setup.py
# 2. run `python3 setup.py sdist` to build package
# 3. run `python3 -m twine upload dist/kclvm-*.tar.gz` to upload package to PyPI
# 4. input username and password of PyPI

install_requires = []
require_path = pathlib.Path(__file__).parent.joinpath("kclvm/scripts/requirements.txt")
with open(require_path) as f:
    requires = f.read().split("\n")
    for require in requires:
        install_requires.append(require)

setup(
    name="kclvm",
    author="KCL Authors",
    version="0.9.0-beta.1",
    license="Apache License 2.0",
    python_requires=">=3.7",
    description="KCL Python SDK",
    long_description="""A constraint-based record & functional language mainly used in configuration and policy scenarios.""",
    author_email="",
    data_files=[
        "kclvm/tools/docs/templates/md.mako",
        "kclvm/scripts/requirements.txt",
        "kclvm/api/version/checksum.txt",
        "kclvm/kcl/grammar/kcl.lark",
        "kclvm/tools/docs/model.proto",
        "kclvm/encoding/protobuf/kcl.proto",
        "kclvm/spec/gpyrpc/gpyrpc.proto",
        "kclvm/spec/gpyrpc/protorpc_wire.proto",
        "kclvm/spec/modfile/modfile.proto",
    ],
    url="https://kcl-lang.io/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
)
