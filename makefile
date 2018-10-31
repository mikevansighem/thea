# A convenience wrapper around commonly used commands

check:
	py.test -v --cov

update-precommit:
	# Autoupdate is disabled because there is an issue running the
	# latest version of black as a pre-commit hook
	#pre-commit autoupdate
	pre-commit install

format:
	black

check-format:
	flake8

# Runs the pre-commit hooks on all files
pre-commit:
	pre-commit run --all-files

run:
	python -m theia

# Add, commit (while ignoring pre-commit hook) and push with a single command
dirty-commit:
	git add .
	git commit -m "$(M)" --no-verify
	git push