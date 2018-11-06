# Notepad

## Quick todo
-   Environment factory with location presets.
-   Lunar: face https://pylunar.readthedocs.io/en/latest/usage.html
-   Handle warnings in logging
-   Main calls CLI, CLI maps directly to calls to Theia world and its stores
-   Disable logging from other modules

## Release as PyPi package
-   [ ] Test on OSX
-   [ ] Version tags
-   [ ] Build exe file
-   [ ] add simple check if main runs
-   [ ] https://github.com/tox-dev/tox/blob/master/tox.ini
-   [ ] add support https://codecov.io/gh/tox-dev/tox/pull/954?src=pr&el=h1

### Notes on release PyPi
-   update with https://stackoverflow.com/questions/39341486/how-to-prevent-travis-from-deploying-twice
-   Better makefile (see cookiecutter and cards)
-   https://github.com/PyCQA/flake8/blob/master/.appveyor.yml
- Read: https://wrongsideofmemphis.wordpress.com/2018/10/28/package-and-deploy-a-python-module-in-pypi-with-poetry-tox-and-travis/
- fix tox coverage
- poetry version command
- more emoji

## Notes
-   timezone according to IANA timezone
-   https://pypi.org/project/pycountry/ for country handling

## Snippets
### Location preset
location = Location(latitude=52.370216, longitude=4.895168, tz='Europe/Amsterdam', altitude=-2, name='Amsterdam')
location.country = 'The Netherlands'

## Longterm todo
-   Lunar: GHI, DNI, DHI
-   List of environment settings and variables including units and allowed ranges.
-   Use mypy
-   Markdown linter in precommit
-   add https://github.com/PyCQA/bandit
-   Toga or qt gui
-   https://www.researchgate.net/post/Please_i_would_like_to_knwo_how_to_convert_lux_to_W_m2
