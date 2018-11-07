# 🚨 Testing and CI
To help us find errors we have a number of tests and checks. Which we can 
run locally but will also run on our continuous integration (CI) system.
For any of the commands in this section to work we assume you have installed
Theia according to the 
[developer installation](https://mikevansighem
.github.io/theia/getting_started/#developer-installation) 
instructions.

## Code testing
All our code tests are located in `/tests` and implemented using 
[pytest](https://docs.pytest.org/en/latest/goodpractices.html). To run 
on your main python installation use: 

```bash
pytest
```

If you would like coverage information as well use:

```bash
py.test --cov
```

## Formating checks

In addition to tests for functionality of the code we have checks for the
formatting of the code. For this we use [Flake8](http://flake8.pycqa.org/en/latest/)
extended with [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings) 
and [pep8-naming](https://github.com/PyCQA/pep8-naming). To run the formatting
checks use:

```bash
flake8
```

## Tox

To test against multiple python versions and manage all test environments 
we use [tox](https://tox.readthedocs.io/en/latest/).
To run the entire test suite including formatting and typing checks use:

```bash
tox
```

## Pre-commit hooks

In order to ease the development of functioning and nicely formatted code
we use pre-commit hooks managed by [pre-commit](https://pre-commit.com).
To get setup with our recommended pre-commit hooks navigate to the root of 
this repository and run:

```bash
pre-commit install
```

This takes care of the setup of all the pre-commit hooks defined in
 `.pre-commit-config.yaml`. Upon your next commit your code will be formatted,
 and checked for linting errors. To run the pre-commit hooks manually use:

```bash 
pre-commit run --all-files
```

!!! warning
    If the commit fails due to one of the formatting tools you can simply 
    retry the commit. Most likely your commit will pass now. If a formatter 
    needs to make a change the pre-commit checks are always considered to 
    be failed even if the formatting has been fixed now.

## Continuous integration

To ease the load on our developers we have set up an extensive continuous 
integration (CI) system. It takes care of building, testing and deployment 
of code and the documentation. To enable multi-platform testing we had to 
use both [Travis-CI](https://travis-ci.com/mikevansighem/theia) and 
[AppVeyor](https://ci.appveyor.com/project/mikevansighem/theia/branch/master) 
To see which service is used to perform what tasks refer to the table below. 

|							| Travis-CI				| AppVeyor				|
|:--------------------------|:---------------------:|:---------------------:|
| Testing on Windows		|					 	| :white_check_mark: 	|
| Testing on Linux		    | :white_check_mark: 	|					  	|
| Testing on OSX			| :white_check_mark:    |						|
| Minimum coverage          | :white_check_mark: 	|						|
| Formatting (flake8)       | :white_check_mark:    |                       |
| Formatting (black)        | :white_check_mark:    |                       |
| Typing (mypy)             | :construction:        |                       |
| Building documentation	| :white_check_mark: 	|						|
| Deploying documentation	| :white_check_mark: 	|						|
| Deploying on PyPi         | :construction:        |                       |

!!! note
    Type checking using myp and deploying to PyPi are not implemented yet.

To help improve the quality of our code further it is analyzed by 
[Codacy](https://app.codacy.com/project/mikevansighem/theia/dashboard) 
which displays linting, security, formatting and coverage results 
in a easy to use interface.
