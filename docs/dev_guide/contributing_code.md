# 💼 Working on code

If you would like to contribute code to Thea we are happy to welcome you.
Underneath you will find a guide with useful information and tutorials
for contributing to the project.

## Installation

To start contributing code to Thea you will need `git` which can be 
installed from the [git website](https://git-scm.com/). 
Also you will need `poetry` which you can get using:

```bash
# basic developer installation
pip install poetry 

# include dependencies for building documentation
poetry install --extra "docs" 
```

You will first need to clone the repository using git and place yourself in its directory:

```bash
git clone git@github.com:mikevansighem/thea.git
cd thea
```

Next, you will need to install the (developer) dependencies of thea.

```bash
poetry install
```

Check that everything is working on your machine before you make changes.

```bash
pytest -v
```

### Pre-commit hooks

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

## Adding your code

Once installation is complete it is off to the races. 
Do what ever you want to Theia.

### Coding style

The code style we use is ["Black"](https://github.com/ambv/black), but
don't worry about that to much as long as you have the provided
[pre-commit hooks]() installed there is nothing for you to do. Black
takes over the minutiae of hand-formatting. One thing Black cannot solve
is your variable naming. Please keep these according to
[PEP-8](https://www.python.org/dev/peps/pep-0008/).

### Dependency management

For packaging of Thea we rely on [poetry](https://poetry.eustace.io/).
Resulting in slightly different dependency management than traditional
Python packages. We do not use a `requirements.txt` file but instead use
`pyproject.toml`. To learn more about this file format head over to the 
documentation of [poetry](https://poetry.eustace.io/). However most that
isn't really important as long as you remember the following commands.

```bash
# adding a dependency
poetry add dependancy_name

# removing a dependency
poetry remove dependancy_name

# updating current installation
poetry update
```

### Committing

Each time you make a notable change to your code you are wise to commit it 
to your branch of Thea. 

```bash
git commit -m ":emoji: Meaningfull message"
```

Preferably you did this using a meaningful commit message 
including an appropriate emoji. To learn more about why we like emoji in 
our commit messages head over [here]()

### Testing

Hopefully your newly committed feature has tests. If not we won't be that 
harsh on you currently we are more interested in evolving Thea rapidly
rather then stability. To learn more about how we test Thei and where to 
store your tests head over to the [testing]() section.

## Pull-request process

If you like to see your code to be added to Thei you need to create a 
pull request. 
This can be done from [Github](https://github.com/mikevansighem/thea/pulls).
Once you create a pull-request your code code will be checked by our
CI system. To find out which checks are being run head over to the
[testing](http://127.0.0.1:8000/dev_guide/testing_and_ci/) page.
If all the checks pass one of the core-contributers will accept you
pull-request and merge it with the master branch to be deployed in the next
release.
