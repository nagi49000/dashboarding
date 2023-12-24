FROM python:3.12.1-slim

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -ms /bin/bash appuser

WORKDIR /build

COPY app/requirements.txt ./
RUN pip install -U pip && \
    pip install -r requirements.txt

WORKDIR /home/appuser
COPY --chown=appuser:appuser app app

WORKDIR /home/appuser/app
USER appuser

HEALTHCHECK CMD curl --fail http://localhost:8051/_stcore/health

CMD python -m streamlit run app.py