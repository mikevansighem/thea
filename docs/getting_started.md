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
| OSX           | :construction:     | :construction:      |

### Basic installation

For the basic installation we assume you have [git](https://git-scm.com/)
installed. If you don't do that first. To start clone the repository 
to your local machine:

```bash
git clone https://github.com/mikevansighem/theia.git
```

Next install the requirements:

```bash
pip install -r requirements.txt
```

!!! Failure
    One of the dependencies namely PyEphem, does not provide binaries for Windows
    Resulting in a failure while installing `requirements.txt`. To fix this
    go to [LFD](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyephem)
    and download a binary for your platform. Install it using 
    `pip install ephem‑3.7.6.1-<YOUR_VERSION>.whl`. After which you should 
    rerun `pip install -r requirements.txt`

Optionally the developer requirements:

```bash
pip install -r requirements-dev.txt
pip install -r requirements-docs.txt
```

### Make

Trough out the documentation we make use of [Make](https://www.gnu.org/software/make/)
to run various commands. If you would like to install it head over to the
[GNU Make website](https://www.gnu.org/software/make/).

## Launching Theia

To launch Theia navigate to the root of the repository and run:

```bash
python -m theia
```

If everything went well you should be ready to start controlling your 
using Theia model-layout.
