FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN pip install poetry

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
