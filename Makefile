PYTHON := python
PYTHON3 := python3
PIP := pip
POETRY := poetry
CD := cd
MAIN_SCRIPT := src
PROJECT_NAME := call_me_maybe
VENV := .VENV
REQUIREMENTS := requirements
UV := uv
RUN := run

help:
	@echo "Available commands:"
	@echo " make setup                            - Creat virtual environment and install build tools"
	@echo " make install                          - Install project dependencies"
	@echo " make run                              - Execute the main script"
	@echo " make debug                            - Run the main script in debug mode (pdb)"
	@echo " make clean                            - Remove temporary files and caches"
	@echo " make fclean                           - Remove temporary files, caches and virtual environmnet"
	@echo " make lint                             - Run flake8 amd mypy with standard checks"
	@echo " make lint-strict                      - Rune flake8 and mypy with strict mode"
	@echo " make help                             - show this help message"


install:
	$(PIP) install --update pip setuptools wheel || true
	$(PIP) install -r requirements.txt || echo "Warning: some packages from requirements.txt failed to install"
	$(CD) llm_sdk && $(POETRY) install

run:
	@$(UV) $(RUN) $(PYTHON) -m src

debug:
	$(PYTHON3) -m pdb $(MAIN_SCRIPT) $(FILE)

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name *.egg-info -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	rm -rf build/ dist/ 2>/dev/null || true

fclean:
	@rm -rf $(VENV) 2>/dev/null || true

lint:
	flake8 . --exclude=.git,.VENV,venv,env,test_vm,build,dist,.mypy_cache,.pytest_cache,__pycache__,dependencies,src,*.egg-info
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs --exclude='(build|dist|venv|env|dependencies|src)'

lint-strict:
	flake8 . --exclude=.git,.venv,venv,env,test_vm,build,dist,.mypy_cache,.pytest_cache,__pycache__,dependencies,src,*.egg-info
	mypy . --strict --exclude='(build|dist|venv|env|dependencies|src)'


setup:
	@rm -rf $(VENV) 2>/dev/null || true
	$(PYTHON3) -m venv $(VENV) --without-pip
	curl -sS https://bootstrap.pypa.io/get-pip.py | $(VENV)/bin/python
	$(VENV)/bin/pip install --upgrade pip setuptools wheel build
	@echo ""
	@echo "Virtual environment created in $(VENV)/"
	@echo "To activate it, run:"
	@echo "  source $(VENV)/bin/activate"

.DEFAULT_GAOL := help

.PHONY: install run debug clean fclean lint lint-strict build help setup