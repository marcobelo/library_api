FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.4.2

WORKDIR /code
COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY ./alembic /code/alembic
COPY ./alembic_insertions /code/alembic_insertions
COPY ./alembic.ini /code/alembic.ini
COPY ./envs /code/envs

COPY ./src /code/src
