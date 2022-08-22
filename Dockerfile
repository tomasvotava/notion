FROM registry.gitlab.com/tomasvotava/python:3.10-slim
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /code
ADD pyproject.toml .
ADD poetry.lock .
RUN poetry install --no-dev
ADD . .

ENTRYPOINT ["python"]

