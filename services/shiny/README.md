# Shiny app

This simple app pulls down data from an API and displays the obtained lat-long coordinates on a map.

Tests and build can be run with `docker-compose build`, and the service brought up with `docker-compose up`. The app should be available on `http://localhost:8080`.

### Other notes

[This account](https://posit.co/blog/why-shiny-for-python/) on the shiny website describes the differences of shiny with streamlit and dash.

Shiny stores the state on the server, requiring websockets and sticky sessions. Shiny's docs recommend using [shiny-server](https://shiny.posit.co/py/docs/deploy.html) as it is optimized for shiny; however shiny-server naturally runs as a systemd service. On those grounds, the implementation here uses Gunicorn with a single worker (so that only one Python process is directly running the app, allowing the shiny server to manage multiple connections). Whilst Shiny (open source) is single-process and single-thread, it does support async.

At the time of writing, it appears that the devs for shiny were having [difficulty with sticky sessions](https://shiny.posit.co/py/docs/deploy.html#heroku) working on PaaS or Cloud infra. The account also gives a good overview of states on a server and why they need sticky sessions.