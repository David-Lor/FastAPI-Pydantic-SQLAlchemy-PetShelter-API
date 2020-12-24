# FastAPI + Pydantic + SQLAlchemy - "Pet Shelter" REST API Example

This project aims to be an example of a full REST API, created with FastAPI & Pydantic, using async SQLAlchemy to persist the data on a supported database (currently using PostgreSQL).

## Main principles

The main principles intended to follow are:

- Usage of Pydantic models for all request/response bodies
- Usage of Alembic migrations for SQLAlchemy
- Persistence of different data contexts (different tables on a database), with relationships between them
- Code organized in `request handling`, `controller`, `repository`
- Contextual logging (each log record have its request id), using Loguru
- Create the whole OpenAPI documentation with the maximum detail, including full, detailed models for requests, responses and errors.
- Usage of Pydantic BaseSettings to load settings from .env file or environment variables
- Acceptance tests only (live tests using the API and a real database)
- Git Flow:
  - `main` and `develop` branches
  - following [Conventional Commits](https://www.conventionalcommits.org)
  - one branch per feature
  - priorize squash merge (feature branches may have several "WIP-like" commits)

## API description

The API simulates the backend of the management system of a fictional pet shelter. Two entities are persisted - animals and shelters (physical places where the animals live), so a relationship between these two entities is made.
In the future, more entities could be added - like people working at the shelters or people adopting the pets.
