import pytest
from app.app import get_app, update_graph


@pytest.fixture()
def client():
    return get_app().server.test_client()


def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.text == '{"status": "ok"}'


def test_update_graph():
    n_coord = 23
    fig = update_graph(n_coord)
    assert len(fig.data[0].lat) == n_coord
    for lat in fig.data[0].lat:
        assert -90.0 <= lat <= 90.0
    assert len(fig.data[0].lon) == n_coord
    for lon in fig.data[0].lon:
        assert -180.0 <= lat <= 180.0
