# Template For Python Projects

This template is based on modified version of this [repo](https://github.com/franneck94/PythonProjectTemplate).

## After developing your code you need to update the README.md with appropriate documentation for your codebase.

### What you get:

- Source code and test code is seperated in different directories.
- External libraries installed and managed by [Pip](https://pypi.org/project/pip/) and [setuptools](https://setuptools.pypa.io/en/latest/) in a pyproject.toml.
- Setup for tests using [Pytest](https://docs.pytest.org/en/stable/) and coverage with [Pytest-Cov](https://github.com/pytest-dev/pytest-cov).
- Continuous testing with [pre-commit](https://github.com/pre-commit/pre-commit).
- Code coverage reports, including automatic upload to [Codecov](https://codecov.io).

## Structure

``` text
├── pyproject.toml
├── ... other config files ...
├── examples (example scripts for running the code)
│   └── ...
├── your_package_name
│   ├── __init__.py
│   ├── main_class.py
│   ├── utils.py
│   └── version.py (contains your code version)
└── tests
    ├── __init__.py
    ├── test_main_class.py
    └── test_utils.py
```

### Commands

```bash
# Before commiting your code to the remote branch you need to make that you pass all of the pre-commit checks by running the following command:
pre-commit run --all-files -v 
```

This command generates a test case code coverage report, which can be found in the `reports` directory. Aim to achieve at least 80% code coverage in your tests.
