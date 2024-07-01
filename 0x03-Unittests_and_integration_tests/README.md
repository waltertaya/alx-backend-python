# 0x03. Unittests and Integration Tests

## Project Overview

This project focuses on creating and running unittests and integration tests for a backend application. The aim is to understand the difference between unit and integration tests, and to learn common testing patterns such as mocking, parameterization, and fixtures.

### Key Concepts
- **Unit Tests:** Test individual functions to ensure they return expected results for different inputs, including standard inputs and corner cases. 
- **Integration Tests:** Test code paths end-to-end, ensuring interactions between all parts of the code work as expected.
- **Mocking:** Replacing parts of the system under test with mock objects to isolate the behavior of the code being tested.
- **Parameterization:** Running a test multiple times with different sets of inputs.
- **Fixtures:** Setting up fixed data sets for tests to run against.

### Execution
To execute your tests, use the following command:
```sh
$ python -m unittest path/to/test_file.py
```

### Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/12176822/how-to-mock-read-only-properties-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
By the end of this project, you should be able to:
- Differentiate between unit and integration tests.
- Implement and understand common testing patterns such as mocking, parameterizations, and fixtures.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- Files must be executable.
- Modules, classes, and functions should have documentation.
- Functions and coroutines must be type-annotated.

## Required Files
- `utils.py`
- `client.py`
- `fixtures.py`

## Tasks

### 0. Parameterize a Unit Test
- Write a unit test for `utils.access_nested_map`.
- Create a `TestAccessNestedMap` class inheriting from `unittest.TestCase`.
- Implement the `test_access_nested_map` method using `@parameterized.expand`.

### 1. Parameterize a Unit Test Exception
- Write a unit test for `utils.access_nested_map` that raises `KeyError`.
- Implement `TestAccessNestedMap.test_access_nested_map_exception` using `assertRaises` and `@parameterized.expand`.

### 2. Mock HTTP Calls
- Write a unit test for `utils.get_json`.
- Define the `TestGetJson(unittest.TestCase)` class and implement `test_get_json`.
- Use `unittest.mock.patch` to patch `requests.get`.

### 3. Parameterize and Patch
- Write a unit test for the `utils.memoize` decorator.
- Implement the `TestMemoize(unittest.TestCase)` class and `test_memoize` method.
- Use `unittest.mock.patch` to mock methods.

### 4. Parameterize and Patch as Decorators
- Write a unit test for `client.GithubOrgClient`.
- Implement the `TestGithubOrgClient(unittest.TestCase)` class and `test_org` method.
- Use `@patch` and `@parameterized.expand`.

### 5. Mocking a Property
- Write a unit test for `GithubOrgClient._public_repos_url`.
- Implement the `test_public_repos_url` method.
- Use `patch` as a context manager.

### 6. More Patching
- Write a unit test for `GithubOrgClient.public_repos`.
- Implement `TestGithubOrgClient.test_public_repos`.
- Use `@patch` and `patch`.

### 7. Parameterize
- Write a unit test for `GithubOrgClient.has_license`.
- Implement `TestGithubOrgClient.test_has_license`.
- Use `@parameterized.expand`.

### 8. Integration Test: Fixtures
- Write an integration test for `GithubOrgClient.public_repos`.
- Implement the `TestIntegrationGithubOrgClient(unittest.TestCase)` class.
- Use `setUpClass` and `tearDownClass`.
- Use `@parameterized_class`.

### 9. Integration Tests
- Write a test for `GithubOrgClient.public_repos`.
- Implement `test_public_repos` and `test_public_repos_with_license`.

## Author

- **@waltertaya**
