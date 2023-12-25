import pytest
from streamlit.testing.v1 import AppTest
from pathlib import Path


@pytest.fixture
def test_app():
    at = AppTest.from_file(str(Path("..") / "app" / "app.py"))
    at.run(timeout=10)
    return at


def test_app_start(test_app):
    assert not test_app.exception
    assert len(test_app.session_state.coords) == 10
