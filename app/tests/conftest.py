from pytest import fixture
from starlette.testclient import TestClient


@fixture(scope="function")
def test_client():
    from main import app

    with TestClient(app) as test_client:
        yield test_client
