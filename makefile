# A convenience wrapper around commonly used commands and commands
# used in continuous integration for testing and deployment.

.PHONY: help run format setup
.DEFAULT_GOAL := help

help: ## Print a help message with the defined commands
	$(info run: starts the main application.)
	$(info setup: runs setup.)
	$(info precommit-install: installs pre-commit hooks.)
	$(info precommit-update: updates versions of pre-commit hooks.)
	$(info commit-dirty: adds commits and pushed without any precommit hooks.)
	$(info format: formats code.)
	$(info check-code Runs all tests.)
	$(info check-format Checks code formatting.)
	$(info setup-and-check: runs setup and checks.)
	$(info docs-show: shows live documentation.")
	$(info docs-preview: shows documentation preview.)
	$(info docs-build: builds deocumentation.)
	# $(info clean: remove all build, test, coverage and Python artifacts.)

run: ## Starts the main application
	python -m theia

# Auto-update is disabled because there is an issue running the
# latest version of black as a pre-commit hook
# pre-commit auto-update
precommit-update: ## Updates and installs pre-commit hooks
	pre-commit install

precommit: ## Runs the pre-commit hooks on all files
	pre-commit run --all-files

commit-dirty: ## Add, commit (while ignoring pre-commit hook) and push with a single command
	git add .
	git commit -m "$(M)" --no-verify
	git push

docs-show: ## Opens live documentation
	CMD /C start https://mikevansighem.github.io/theia/

docs-preview: ## Serves docs locally and opens them in the browser
	CMD /C start http://127.0.0.1:8000
	mkdocs serve


buid:
	poetry check
	poetry build
	poetry publish

	poetry install --extras "mysql pgsql"
	poetry install --no-dev
