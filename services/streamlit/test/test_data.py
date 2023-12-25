from app.data import get_data


def test_run_import():
    n_row = 30
    df = get_data(n_results=n_row)
    assert len(df) == n_row
    assert list(df.columns) == ["lat", "lon"]
    for row in df.iterrows():
        # latitude should be in [-90, 90] degrees
        assert -90.0 <= row[0] <= 90.0
        # longitude should be in [-180, 180] degrees
        assert -180.0 <= row[0] <= 180.0
