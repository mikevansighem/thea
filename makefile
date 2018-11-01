# A convenience wrapper around commonly used commands and commands
# used in continuous integration for testing and deployment.

# Starts the main application
run:
	python -m theia

# Updates and installs pre-commit hooks
update-precommit:
	# Auto-update is disabled because there is an issue running the
	# latest version of black as a pre-commit hook
	#pre-commit auto-update
	pre-commit install

# Runs the pre-commit hooks on all files
pre-commit:
	pre-commit run --all-files

# Add, commit (while ignoring pre-commit hook) and push with a single command
dirty-commit:
	git add .
	git commit -m "$(M)" --no-verify
	git push

# Formats code and documentation
format:
	black

# Install requirements
setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Runs all tests
check-code:
	py.test -v --cov

# Check code and documentation formatting
check-format:
	flake8

# Run setup and run tests
setup-and-check: setup check-code
	# Later we will enforce flake8
	#check-format
	coverage xml
	python-codacy-coverage -r coverage.xml

# Serves docs locally and opens them in the browser
docs-show:
	CMD /C start http://127.0.0.1:8000
	mkdocs serve

# Build documentation
docs-build:
	pip install -r requirements-docs.txt
	mkdocs build --verbose --clean --strict
