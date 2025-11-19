# ----------------------------
# Builder
# ----------------------------
FROM python:3.13-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code

WORKDIR /code

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry==1.5.1 && \
    poetry config virtualenvs.create false

# Copy project metadata (from backend/)
COPY pyproject.toml poetry.lock /code/

RUN poetry install --only main --no-interaction --no-ansi

# ----------------------------
# Development
# ----------------------------
FROM builder AS development

WORKDIR /code

COPY . /code

CMD ["uvicorn", "app.main:get_app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--factory"]

# ----------------------------
# Production
# ----------------------------
FROM python:3.13-slim AS production

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code

WORKDIR /code

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . /code

CMD ["uvicorn", "app.main:get_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
