# Python Variable Annotations

## Overview
This repository contains solutions for tasks related to Python Variable Annotations. These tasks are part of the **"0x00. Python - Variable Annotations"** project, which is a short specialization within the Python curriculum focused on advanced Python concepts.

## Concepts Covered
- Advanced Python
- Type annotations in Python 3
- Specifying function signatures and variable types using type annotations
- Duck typing
- Code validation with mypy

## Requirements
- **Editors**: `vi`, `vim`, `emacs`
- **Interpreter/Compiler**: Python 3.7 on Ubuntu 18.04 LTS
- **Code Style**: pycodestyle (version 2.5.0)
- **File Endings**: All files should end with a new line
- **Shebang**: First line of all files should be exactly `#!/usr/bin/env python3`
- **Executability**: All files must be executable
- **Documentation**: Modules, classes, and functions must have proper documentation

## Tasks

### Task 0: Basic annotations - add
- **File**: `0-add.py`
- **Function**: `add`
- **Description**: A type-annotated function that takes two floats `a` and `b` and returns their sum as a float.

```python
def add(a: float, b: float) -> float:
    return a + b
```

### Task 1: Basic annotations - concat
- **File**: `1-concat.py`
- **Function**: `concat`
- **Description**: A type-annotated function that takes two strings `str1` and `str2` and returns a concatenated string.

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### Task 2: Basic annotations - floor
- **File**: `2-floor.py`
- **Function**: `floor`
- **Description**: A type-annotated function that takes a float `n` and returns the floor of the float as an integer.

```python
def floor(n: float) -> int:
    import math
    return math.floor(n)
```

### Task 3: Basic annotations - to string
- **File**: `3-to_str.py`
- **Function**: `to_str`
- **Description**: A type-annotated function that takes a float `n` and returns the string representation of the float.

```python
def to_str(n: float) -> str:
    return str(n)
```

### Task 4: Define variables
- **File**: `4-define_variables.py`
- **Description**: Define and annotate the following variables:
  - `a`: an integer with value 1
  - `pi`: a float with value 3.14
  - `i_understand_annotations`: a boolean with value True
  - `school`: a string with value "Holberton"

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### Task 5: Complex types - list of floats
- **File**: `5-sum_list.py`
- **Function**: `sum_list`
- **Description**: A type-annotated function that takes a list of floats and returns their sum as a float.

```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### Task 6: Complex types - mixed list
- **File**: `6-sum_mixed_list.py`
- **Function**: `sum_mixed_list`
- **Description**: A type-annotated function that takes a list of integers and floats and returns their sum as a float.

```python
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
```

### Task 7: Complex types - string and int/float to tuple
- **File**: `7-to_kv.py`
- **Function**: `to_kv`
- **Description**: A type-annotated function that takes a string `k` and an int/float `v`, returning a tuple where the second element is the square of `v` as a float.

```python
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
```

### Task 8: Complex types - functions
- **File**: `8-make_multiplier.py`
- **Function**: `make_multiplier`
- **Description**: A type-annotated function that takes a float `multiplier` and returns a function that multiplies a float by the multiplier.

```python
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
```

### Task 9: Let's duck type an iterable object
- **File**: `9-element_length.py`
- **Function**: `element_length`
- **Description**: Annotate the function’s parameters and return values with the appropriate types.

```python
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

## Repository Structure
```
alx-backend-python
├── 0x00-python_variable_annotations
│   ├── 0-add.py
│   ├── 1-concat.py
│   ├── 2-floor.py
│   ├── 3-to_str.py
│   ├── 4-define_variables.py
│   ├── 5-sum_list.py
│   ├── 6-sum_mixed_list.py
│   ├── 7-to_kv.py
│   ├── 8-make_multiplier.py
│   └── 9-element_length.py
└── README.md
```

## Getting Started
To run any of the provided scripts:
1. Ensure you have Python 3.7 installed.
2. Clone the repository.
3. Navigate to the appropriate directory.
4. Run the script using `./<script_name>.py`.

Ensure all scripts are executable by running `chmod +x <script_name>.py` if necessary.
