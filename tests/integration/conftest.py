from fastapi.testclient import TestClient
from pytest import fixture

from src.main import CreateApp


@fixture(scope="session", name="api_client")
def __fixture_fastapi_client():
    create_app = CreateApp()
    base_url = "http://localhost:8000"
    with TestClient(create_app.execute(), base_url=base_url) as api_client:
        yield api_client
