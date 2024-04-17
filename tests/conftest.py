import pytest
from src.app import create_app


@pytest.fixture
def app():
    app = create_app('development')
    return app


@pytest.fixture
def client(app):
    return app.test_client()
