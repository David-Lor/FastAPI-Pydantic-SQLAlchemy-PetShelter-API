.DEFAULT_GOAL := help

install-requirements: ## pip install requirements for app
	pip install -r requirements.txt

install-test-requirements: ## pip install requirements for tests
	pip install -r requirements.test.txt

run: ## python run app
	python .

test: ## python run tests
	pytest -sv .

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
