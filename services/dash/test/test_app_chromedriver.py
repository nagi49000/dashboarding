from app.app import get_app


def test_update_graph_in_server(dash_duo):
    dash_duo.start_server(get_app())
