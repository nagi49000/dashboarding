from app.app import get_map_with_coords


def test_get_map_with_coords():
    n_rows = 7
    ax = get_map_with_coords(n_rows)
    # 0th entry is worldmap points, 1st entry is scatter data as masked_array
    coords = ax._children[1].get_offsets().data
    assert len(coords) == n_rows
    for row in coords:
        assert len(row) == 2
        assert -180.0 <= row[0] <= 180.0  # long
        assert -90.0 <= row[1] <= 90.0  # lat
