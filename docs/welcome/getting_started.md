# 🤔 Getting started

For an end user it might be a bit early to get started however
if you really want to give Thea a try already follow the instructions
below.

!!! note
    In case you would like to contribute head over to the
    [contributing](https://mikevansighem.github.io/thea/contibuting) section
    of our documentation. And follow the developer installation instructions.

## Installation prerequisites

To run Thea you will need Python 3.6 or higher installed on your machine.
To get it we recommend you follow this guide from 
[Real Python](https://realpython.com/installing-python/).
However the quick version is that you should go to 
the [Python website](https://www.python.org/downloads/), download the latests 
version and keep clicking next in the installer.

### Supported platforms

Thea aims to make the program available on most platforms, check the table
below if your version is supported. If you would like us to support more 
versions/platforms submit an enhancement request on 
[Github]((https://github.com/mikevansighem/thea/issues)).


|               | Python 3.6         | Python 3.7          | Python 3.8         |
|:--------------|:------------------:|:-------------------:|:------------------:|
| Windows x86   | :white_check_mark: | :white_check_mark:  | :construction:     |
| Windows x64   | :white_check_mark: | :white_check_mark:  | :construction:     |
| Linux         | :white_check_mark: | :white_check_mark:  | :construction:     |
| OSX           | :white_check_mark: | :white_check_mark:  | :white_check_mark: |

!!! note
    We are testing against the development branch of Python 3.8.
    Currently tests on OSX are passing but we do not guaranty it will 
    work for you as well.

## Installing Thea

To install Thea we will use the command line. On Windows open the `start`
menu, search for `cmd` and hit the `enter` key. In the command line window
type:

```bash
pip install thea
```

Hit the `enter` key and Thea together with other dependencies
will be downloaded and installed.

## Launching Thea

To launch Thea navigate to the root of the repository and run:

```bash
python -m thea
```

If everything went well you should be ready to start controlling your 
using Thea model-layout.
