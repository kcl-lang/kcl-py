<h1 align="center">KCL Python SDK</h1>

<p align="center">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  <img src="https://img.shields.io/github/release/kcl-lang/kcl-py.svg">
  <img src="https://img.shields.io/github/license/kcl-lang/kcl-py.svg">
  <img src="https://app.fossa.com/projects/git%2Bgithub.com%2Fkcl-lang%2Fkcl-py?ref=badge_shield">
  <img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkcl-lang%2Fkcl-py.svg?type=shield">
</p>

## How to use

### Installation

Run the cmd for the installation and help:

```cmd
python3 -m pip install kclvm && python3 -m kclvm --help
```

### Command Line Tools

Write the KCL file named `hello.k`:

```python
name = "kcl"
age = 1

schema Person:
    name: str = "kcl"
    age: int = 1

x0 = Person {}
x1 = Person {
    age = 101
}
```

Run the cmd:

```cmd
python3 -m kclvm hello.k
```

The output is:

```yaml
name: kcl
age: 1
x0:
  name: kcl
  age: 1
x1:
  name: kcl
  age: 101
```

### API

Run KCL code with the KCL Python SDK

```python3
import kclvm.program.exec as kclvm_exec
import kclvm.vm.planner as planner

print(planner.plan(kclvm_exec.Run(["hello.k"]).filter_by_path_selector()))
```

Output

```shell
$ python3 main.py
name: kcl
age: 1
x0:
  name: kcl
  age: 1
x1:
  name: kcl
  age: 101
```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkcl-lang%2Fkcl-py.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkcl-lang%2Fkcl-py?ref=badge_large)
