# PLEASE BE NICE AND LIST SECTIONS IN ALPHABETICAL ORDER!
REPO_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: clean

ifeq ($(UPGRADE),yes)
	UPDATE_FLAG = ""
else
	UPDATE_FLAG = --no-update
endif


# Put it first so that "make" without argument is like "make help".
help:
	@echo "Commands available:"
	@echo
	@echo "    clean: Removed compiled Python files."
	@echo "    lint: Run all code lint and style tests. Note: Ensure all tests pass before submitting a PR!"
	@echo "    test: Run all tests."
	@echo "    test-clrs-only: Run CLRS tests only."
	@echo "    test-leet-only: Run Leet Code tests only."

## Delete all compiled Python files.
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

########## LINTING ##########
# Run various linting, style, etc.
lint:
	isort .
	black .
	flake8 .
	mypy src/ --ignore-missing-imports
	pylint src/

########## TESTING ##########
# Run all tests and get coverage report.
test:
	export PYTHONPATH=$(REPO_DIR)/src:PYTHONPATH && \
	pytest -v --cov-report term-missing --cov=src/ tests/

test-clrs-only:
	export PYTHONPATH=$(REPO_DIR)/src:PYTHONPATH && \
	pytest -v --cov-report term-missing --cov=src/ tests/ --clrs_only

test-leet-only:
	export PYTHONPATH=$(REPO_DIR)/src:PYTHONPATH && \
	pytest -v --cov-report term-missing --cov=src/ tests/ --leet_only