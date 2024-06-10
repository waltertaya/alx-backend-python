# 0x01. Python - Async

## Overview
This project focuses on asynchronous programming in Python, specifically using the `asyncio` library. It covers the basics of `async` and `await` syntax, how to run concurrent coroutines, create asyncio tasks, and utilize the `random` module. 

## Learning Objectives
By the end of this project, you should be able to:
- Understand `async` and `await` syntax.
- Execute an async program with `asyncio`.
- Run concurrent coroutines.
- Create `asyncio` tasks.
- Use the `random` module effectively.

## Resources
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Requirements
- A `README.md` file at the root of the project folder is mandatory.
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- All files should end with a new line and must be executable.
- Code should follow the `pycodestyle` style (version 2.5.x).
- Functions and coroutines must be type-annotated.
- Modules and functions should have documentation.

## Project Tasks

### Task 0: The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value 10) and waits for a random delay between 0 and `max_delay` seconds before returning it.

**File**: `0-basic_async_syntax.py`

### Task 1: Let's execute multiple coroutines at the same time with async
Write an async routine `wait_n` that takes two int arguments `n` and `max_delay`. It spawns `wait_random` `n` times with the specified `max_delay` and returns the list of all delays in ascending order.

**File**: `1-concurrent_coroutines.py`

### Task 2: Measure the runtime
Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`.

**File**: `2-measure_runtime.py`

### Task 3: Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

**File**: `3-tasks.py`

### Task 4: Tasks
Alter the code from `wait_n` into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

**File**: `4-tasks.py`

## Repository
- **GitHub Repository**: `alx-backend-python`
- **Directory**: `0x01-python_async_function`

## Usage
To run the provided examples, you can use the following commands in your terminal:

```sh
# Task 0
python3 0-main.py

# Task 1
python3 1-main.py

# Task 2
python3 2-main.py

# Task 3
python3 3-main.py

# Task 4
python3 4-main.py
```

## Author

- **@waltertaya**
