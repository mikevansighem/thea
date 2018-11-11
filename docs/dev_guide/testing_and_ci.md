# 🚨 Testing and CI

To help us find errors we have a number of tests and checks. Which we can 
run locally but will also run on our continuous integration (CI) system.
For any of the commands in this section to work we assume you have installed
Thea according to the 
[developer installation]() 
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
we use [tox](https://tox.readthedocs.io/en/latest/). To install:

```bash
pip install tox
```

To run the entire test suite including formatting and typing checks use:

```bash
tox
```

## Continuous integration

To ease the load on our developers we have set up an extensive continuous 
integration (CI) system. It takes care of building, testing and deployment 
of code and the documentation. To enable multi-platform testing we had to 
use both [Travis-CI](https://travis-ci.com/mikevansighem/thea) and 
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
| Deploying on PyPi         | :white_check_mark:    |                       |
| Building executable       |                       | :construction:        |
| Deploying executable      |                       | :construction:        |

!!! note
    Type checking using mypy and building an executable are not functional yet.

To help improve the quality of our code further it is analyzed by 
[Codacy](https://app.codacy.com/project/mikevansighem/thea/dashboard) 
which displays linting, security, formatting and coverage results 
in a easy to use interface.
