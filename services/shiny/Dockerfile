FROM python:3.12.1-slim AS builder

RUN apt-get update && \
    # curl for healthcheck
    apt-get install -y curl htop && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -ms /bin/bash appuser

WORKDIR /build

COPY requirements.txt ./
RUN pip install -U pip && \
    pip install -r requirements.txt

WORKDIR /home/appuser
COPY --chown=appuser:appuser app app

FROM builder AS tester

COPY --chown=appuser:appuser requirements-test.txt requirements-test.txt
RUN pip install -r requirements-test.txt
COPY --chown=appuser:appuser test test
RUN python -m flake8 --max-line-length=120 && \
    python -m black --check . && \
    python -m pytest --cov=./app  --cov-report=term-missing

FROM builder AS prod

USER appuser

CMD gunicorn -k uvicorn.workers.UvicornWorker app.run_app:app --workers 1 --bind 0.0.0.0:3838 --log-level DEBUG
