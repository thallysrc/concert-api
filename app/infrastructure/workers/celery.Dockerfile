# ----------------------------
# Builder
# ----------------------------
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code

WORKDIR /code

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry==1.5.1 && \
    poetry config virtualenvs.create false

# Copy project metadata (from backend/)
COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install --no-root && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes


