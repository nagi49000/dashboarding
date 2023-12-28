import dash
import json
import plotly.express as px
from app.data import get_data


def get_app(server=True):
    app = dash.Dash(__name__, server=server)

    @app.server.route("/ping")
    def ping():
        return json.dumps({"status": "ok"})

    app.layout = dash.html.Div(
        [
            dash.html.H1(
                children="Map plotting with Dash", style={"textAlign": "center"}
            ),
            dash.dcc.Input(
                id="input-n-coords",
                type="number",
                min=1,
                placeholder="number of coords to fetch",
            ),
            dash.dcc.Graph(id="graph-content"),
        ]
    )

    @dash.callback(
        dash.Output("graph-content", "figure"), dash.Input("input-n-coords", "value")
    )
    def update_graph(value):
        df = get_data(n_results=value)
        fig = px.scatter_geo(df, lat="lat", lon="lon")
        return fig

    return app
