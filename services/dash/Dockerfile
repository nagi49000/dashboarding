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

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD gunicorn app.min_app:server --bind 0.0.0.0:8050 --log-level DEBUG