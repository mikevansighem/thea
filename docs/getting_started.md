# 🤔 Getting started

Currently Theia is in early development so it has not much use for an
end-user but if you would like to try it out anyway follow the instructions
below.

## Installation

Before installing check you have a supported platform and python version.
If you don't submit an issue on [Github]((https://github.com/mikevansighem/theia/issues)) 
requesting support. 

### Supported platforms

Theia aims to make the program available on most platforms, check the table
below if your version is supported.

|               | Python 3.6         | Python 3.7          |
|:--------------|:------------------:|:-------------------:|
| Windows x86   | :white_check_mark: | :white_check_mark:  |
| Windows x64   | :white_check_mark: | :white_check_mark:  |
| Linux         | :white_check_mark: | :white_check_mark:  |
| OSX           | :white_check_mark: | :white_check_mark:  |


### Quick installation

```bash
pip install theia
```

### Developer installation

For the developer installation we assume you have [git](https://git-scm.com/)
installed. If you don't do that first. To start clone the repository 
to your local machine:

```bash
git clone https://github.com/mikevansighem/theia.git
```

Next install in a virtual environment using poetry:

```bash
pip install poetry
poetry install theia
```

Or optionally with the requirements for building documentation:

```bash
pip install poetry --extras "docs"
```

## Launching Theia

To launch Theia navigate to the root of the repository and run:

```bash
python -m theia
```

If everything went well you should be ready to start controlling your 
using Theia model-layout.
