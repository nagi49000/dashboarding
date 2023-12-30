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

FROM builder AS prod

USER appuser

# HEALTHCHECK CMD curl --fail http://localhost:8050/ping

CMD gunicorn -k uvicorn.workers.UvicornWorker app.min_app:app --workers 1 --bind 0.0.0.0:3838 --log-level DEBUG
