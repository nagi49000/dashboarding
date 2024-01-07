# Dash app

This simple app pulls down data from an API and displays the obtained lat-long coordinates on a map.

Tests and build can be run with `docker-compose build`, and the service brought up with `docker-compose up`. The app should be available on `http://localhost:8080`.

### Other notes

The dash app is served via Flask on Gunicorn. Dash appears to mostly be built on top of Flask, meaning that Dash can only be served through WSGI; no ASGI or asyncio behaviour is available. Flask handles this by using threading. It does not appear that the developers are looking to introduce any async support (some devs seem to have tried to get Quart working with Dash, but Quart support does not appear to be standard with Dash at the time of writing. States in Dash are handled client side (so that the server is stateless). The client communicates with the server over HTTP(S). This permits good horizontal scaling with multiple workers on a server, and multiple servers behind reverse-proxies or load-balancers etc. For large amounts of data, one can set up Dash to perform [server-side caching](https://community.plotly.com/t/show-and-tell-server-side-caching/42854), although the caching will be limited to the process and server.

Whilst the set up of serving via Flask is a little old-school (e.g. no async support, writing out Flask endpoints explicitly etc.), the stack has been around for a while and has developed a number of good production features. Reliable horizontal scalability is an important one. Another important aspect is the maturity of testing tools, e.g. [dash testing](https://dash.plotly.com/testing) which support standard unit testing of functions, running Flask test clients, and selenium integration into pytest (via the fixture `dash_duo` - very cool) to run UI tests as a part of pytest.

### Azure hosting

Create a container repo in Azure (Basic should be useful for most basic operations). To set up access/logins from the command line run `az login` then `az acr login --name <name of image registry>`. The dash app image can then ge tagged and pushed to the image registry in Azure with
```
docker tag dash_dash-app <name of image registry>.azurecr.io/samples/dash_dash-app
docker push <name of image registry>.azurecr.io/samples/dash_dash-app
```
