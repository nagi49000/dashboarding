from app.data import get_data


def test_run_import():
    df = get_data(n_results=3)
    assert len(df) == 3
    assert list(df.columns) == ["lat", "lon"]
