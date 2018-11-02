# 🚨 Testing and CI

## Code testing
All our code tests are located in `/tests` and implemented using 
[pytest](https://docs.pytest.org/en/latest/goodpractices.html). To run 
the use: 

```bash
make check-code
```

## Formating checks

In addition to tests for functionality of the code we have checks for the
formatting of the code. For this we use [Flake8](http://flake8.pycqa.org/en/latest/)
extended with [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings) 
and [pep8-naming](https://github.com/PyCQA/pep8-naming). To run the formatting
checks use:

```bash
make check-format
```

## Pre-commit hooks

In order to ease the development of functioning and nicely formatted code
we use pre-commit hooks managed by [pre-commit](https://pre-commit.com).
To get setup with our recommended pre-commit hooks navigate to the root of 
this repository and run:

```bash
make precommit-install
```

This takes care of the setup of all the pre-commit hooks defined in
 `.pre-commit-config.yaml`. Upon your next commit your code will be formatted,
 and checked for linting errors. 

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
| Testing on OSX			| :construction:		|						|
| Coverage for Codacy       | :white_check_mark: 	|						|
| Building documentation	| :white_check_mark: 	|						|
| Deploying documentation	| :white_check_mark: 	|						|

!!! note
    Testing on OSX using Travis-CI is planned.

To help improve the quality of our code further it is analyzed by 
[Codacy](https://app.codacy.com/project/mikevansighem/theia/dashboard) 
which displays linting, security, formatting and coverage results 
in a easy to use interface.
