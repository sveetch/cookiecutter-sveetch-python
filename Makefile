PYTHON_INTERPRETER=python3
VENV_PATH=.venv

PYTHON_BIN=$(VENV_PATH)/bin/python
PIP_BIN=$(VENV_PATH)/bin/pip
FLAKE_BIN=$(VENV_PATH)/bin/flake8
PYTEST_BIN=$(VENV_PATH)/bin/pytest
COOKIECUTTER_BIN=$(VENV_PATH)/bin/cookiecutter

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo
	@echo "  clean               -- to clean EVERYTHING (Warning)"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo "  clean-install       -- to clean Python side installation"
	@echo "  clean-dist          -- to remove distributed directory"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo
	@echo "  project             -- to create a new project"
	@echo

clean-pycache:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear Python cache <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-install:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear installation <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-install

clean-dist:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning distributed directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf dist
.PHONY: clean-dist

clean: clean-install clean-pycache
.PHONY: clean

venv:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install virtual environment <---$(FORMATRESET)\n"
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# Uncomment these two lines if you want development install support on old
	# distributions (<2020)
	#$(PIP_BIN) install --upgrade pip
	#$(PIP_BIN) install --upgrade setuptools
.PHONY: venv

install: venv
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install everything for development <---$(FORMATRESET)\n"
	@echo ""
	$(PIP_BIN) install -r requirements/base.txt
	$(PIP_BIN) install -r requirements/dev.txt
.PHONY: install

project:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating new project <---$(FORMATRESET)\n"
	@echo ""
	@mkdir -p dist
	@$(COOKIECUTTER_BIN) -o dist .
.PHONY: project
