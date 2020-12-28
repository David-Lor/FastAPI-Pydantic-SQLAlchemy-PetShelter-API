.DEFAULT_GOAL := help

install-requirements: ## pip install requirements for app
	pip install -r requirements.txt

install-test-requirements: ## pip install requirements for tests
	pip install -r requirements.test.txt

run: ## python run app
	python .

test: ## python run tests
	pytest -sv .

sql-migrate: ## run sqlalchemy alembic migrations to head
	alembic upgrade head

sql-generate-migration: ## generate a new migration step with sqlalchemy alembic (database must be running and updated to the latest available migration step; migration name is asked interactively)
	@echo "Enter migration name: "
	@read MIGRATION_NAME && alembic revision --autogenerate -m "$$MIGRATION_NAME"

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
