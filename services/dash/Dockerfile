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

RUN apt-get update && \
    # install a load of stuff for installing chrome and a webdriver
    apt-get install -y jq unzip gnupg wget && \
    apt-get update && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    # get latest version of webdriver
    curl --silent https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq '.channels.Stable.downloads.chromedriver[].url' | grep 'linux' > chromedriver-latest-url.txt && \
    # dl and install webdriver
    xargs -n 1 curl -o chromedriver-latest.zip < chromedriver-latest-url.txt && \
    unzip chromedriver-latest.zip && \
    install -m 755 chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
COPY --chown=appuser:appuser requirements-test.txt requirements-test.txt
RUN pip install -r requirements-test.txt
COPY --chown=appuser:appuser test test
RUN python -m flake8 --max-line-length=120 && \
    python -m black --check . && \
    python -m pytest --cov=./app --cov-report=term-missing --headless

FROM builder AS prod

USER appuser

CMD gunicorn app.run_app:server --workers 4 --bind 0.0.0.0:80 --log-level DEBUG
