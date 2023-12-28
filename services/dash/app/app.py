import dash
import flask
import json
import plotly.express as px
import plotly.graph_objects as po
from app.data import get_data


def get_app() -> dash.Dash:
    app = dash.Dash(__name__, server=flask.Flask(__name__))

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
            dash.html.Button("Update", id="button-update-coords"),
            dash.dcc.Graph(id="graph-content"),
        ]
    )

    return app


@dash.callback(
    dash.Output("graph-content", "figure"),
    dash.Input("button-update-coords", "n_clicks"),
    dash.State("input-n-coords", "value"),
)
def update_graph(_, value: int) -> po.Figure:
    df = get_data(n_results=value)
    fig = px.scatter_geo(df, lat="lat", lon="lon")
    return fig
