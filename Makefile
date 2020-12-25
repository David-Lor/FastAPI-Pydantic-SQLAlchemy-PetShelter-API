.DEFAULT_GOAL := help

install-requirements: ## pip install requirements for app
	pip install -r requirements.txt

run: ## python run app
	python .

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
