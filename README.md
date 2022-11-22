# KCLVM-Py

KCLVM binding for Python

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

Run KCL code with kclvm-py

```python3
import kclvm.program.exec as kclvm_exec
import kclvm.vm.planner as planner

print(planner.plan(kclvm_exec.Run(["hello.k"]).filter_by_path_selector()))
```

Output

```
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
