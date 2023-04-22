
# Getting Started With Testing in Python

A brief demonstration of unit testing with Pytest and Unittest.


## Installation

Install python dependencies with pip.

```bash
  cd Python-TDD
  pip install  -r requeriments.txt
```
    
## Running Tests

Pytest - To run tests, run the following command.

```bash
  python3 -m pytest test_main.py
```

Pytest - To create report html, run the following command.

```bash
  python3 -m pytest --cov-report html --cov .
```

Unittest - To run tests, run the following command.

```bash
  python3 unittest_main.py
```

Unittest - To create report html, run the following command.

```bash
  python3 -m coverage report
```
