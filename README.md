# FastAPI + Pydantic + SQLAlchemy - "Pet Shelter" REST API Example

This project aims to be an example of a full REST API, created with FastAPI & Pydantic, using async SQLAlchemy to persist the data on a supported database (currently using PostgreSQL).

## Main principles

The main principles intended to follow are:

- Usage of Pydantic models for all request/response bodies
- Usage of Alembic migrations for SQLAlchemy
- Persistence of different data entities (different tables on a database), with relationships between them
- Request-handling codebase organized in `request handling`, `controller`, `repository`
- Contextual logging (each log record have its request id), using Loguru
- Create the whole OpenAPI documentation with the maximum detail, including full, detailed models for requests, responses and errors.
- Usage of Pydantic BaseSettings to load settings from .env file or environment variables
- Acceptance tests only (live tests using the API and a real database)
- Git Flow:
  - usage of [main](https://github.com/David-Lor/FastAPI-Pydantic-SQLAlchemy-PetShelter-API/tree/main) and [develop](https://github.com/David-Lor/FastAPI-Pydantic-SQLAlchemy-PetShelter-API/tree/develop) branches
  - one branch per feature/bug/issue
  - following [Conventional Commits](https://www.conventionalcommits.org) (on main/develop branches only)
  - priorize squash merge (feature branches may have several "WIP-like" commits, that do not follow Conventional Commits)

## API description

The API simulates the backend of the management system of a fictional pet shelter, providing endpoint to perform CRUD operations.
Two entities are persisted - animals and shelters (physical places where the animals live), so a relationship between these two entities is made.
In the future, more entities could be added - like people working at the shelters or people adopting the pets.

## Getting started

### Requirements

- Python >= 3.6
- Requirements listed in [requirements.txt](requirements.txt)
- Virtual env or Conda/Miniconda env recommended

### Running the API

```bash
make install-requirements
make run
```

### Running the tests

```bash
make install-test-requirements
make test
```

## Changelog

TODO
