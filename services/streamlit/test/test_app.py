import pytest
from streamlit.testing.v1 import AppTest
from pathlib import Path


@pytest.fixture
def test_app():
    at = AppTest.from_file(str(Path("..") / "app" / "app.py"))
    at.run(timeout=10)
    assert not at.exception
    return at


def test_app_start(test_app):
    assert len(test_app.session_state.coords) == 10


def test_app_update_coords(test_app):
    assert len(test_app.session_state.coords) == 10
    # list of element classes to access in AppTest
    # https://docs.streamlit.io/library/api-reference/app-testing
    # enter the new value in the box
    test_app.text_input(key="n_new_coords_textbox").input("5").run()
    assert test_app.text_input(key="n_new_coords_textbox").value == "5"
    assert test_app.session_state.n_new_coords == "5"
    # click the update button to update the coords
    test_app.button(key="update_coords_button").click().run()
    assert len(test_app.session_state.coords) == 5
