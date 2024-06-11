# 0x02. Python - Async Comprehension

## Project Overview

This project covers the concepts of asynchronous programming in Python, focusing on asynchronous comprehensions and generators. You will learn to write asynchronous generators, use async comprehensions, and properly type-annotate these components.

## Resources

- **PEP 530 – Asynchronous Comprehensions**
- **What’s New in Python: Asynchronous Comprehensions / Generators**
- **Type-hints for generators**

## Learning Objectives

By the end of this project, you should be able to:

1. Write an asynchronous generator.
2. Use async comprehensions.
3. Type-annotate generators.

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter**: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- **File Format**:
  - All files should end with a new line.
  - The first line of all files should be `#!/usr/bin/env python3`.
  - All files must adhere to `pycodestyle` style (version 2.5.x).
  - File lengths will be tested using `wc`.

- **Documentation**:
  - All modules should have documentation.
  - All functions should have documentation.
  - Documentation must be a complete sentence explaining the purpose of the module, class, or method.
  
- **Type Annotations**: All functions and coroutines must be type-annotated.

## Tasks

### Task 0: Async Generator

Write a coroutine called `async_generator` that takes no arguments.

- The coroutine will loop 10 times.
- Each time, it will asynchronously wait 1 second, then yield a random number between 0 and 10.

**Example Usage**:
```python
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

**File**: `0-async_generator.py`

### Task 1: Async Comprehensions

Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that takes no arguments.

- The coroutine will collect 10 random numbers using an async comprehension over `async_generator`.
- It will then return the 10 random numbers.

**Example Usage**:
```python
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

**File**: `1-async_comprehension.py`

### Task 2: Run time for four parallel comprehensions

Import `async_comprehension` from the previous task and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

- `measure_runtime` should measure the total runtime and return it.
- The total runtime is expected to be roughly 10 seconds.

**Example Usage**:
```python
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
```

**File**: `2-measure_runtime.py`

## Repository Structure

- **GitHub repository**: `alx-backend-python`
- **Directory**: `0x02-python_async_comprehension`
  - `0-async_generator.py`
  - `1-async_comprehension.py`
  - `2-measure_runtime.py`


## Authors

- **@waltertaya**
