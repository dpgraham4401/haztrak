# Builder
FROM python:3.13-slim AS builder
LABEL authors="dpgraham4401@gmail.com"

COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    UV_PYTHON_DOWNLOADS=0 \
    UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1

#RUN apt install libffi-dev gcc libc-dev curl
RUN apt-get update && \
    apt-get install -y libffi-dev gcc libc-dev curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev

# App
FROM python:3.13-slim-bookworm

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0:8000", "--workers", "2", "-k", "uvicorn_worker.UvicornWorker", "trak.main.asgi:app"]
