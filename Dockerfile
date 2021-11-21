ARG PYTHON_VERSION=3.9.7

FROM python:${PYTHON_VERSION}-alpine

ARG POETRY_VERSION=1.1.11

RUN apk update && apk add curl libffi-dev gcc g++ libc-dev openssl-dev
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
ENV PYTHONPATH=/usr/app

WORKDIR /usr/app

# Install dependencies
ENV POETRY_VIRTUALENVS_CREATE=false
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev --no-interaction --no-ansi

# Remove build-only dependencies
RUN apk del libffi-dev gcc g++ libc-dev openssl-dev

# Copy source
COPY . .

ENTRYPOINT poetry run
