from fastapi.testclient import TestClient
from mixer.backend.sqlalchemy import Mixer
from pytest import fixture

from src.main import CreateApp
from tests.config import CustomGenFactory, PostgresDocker, make_sync_session

postgres_docker = PostgresDocker()


@fixture(scope="session", autouse=True)
def __fixture_database():
    postgres_docker.run()
    postgres_docker.wait_until_ready()
    postgres_docker.run_migrations()
    yield
    postgres_docker.stop()


@fixture(scope="function", autouse=True)
def __fixture_reset_database():
    postgres_docker.reset()


@fixture(scope="session", name="api_client")
def __fixture_fastapi_client():
    create_app = CreateApp()
    base_url = "http://localhost:8000"
    with TestClient(create_app.execute(), base_url=base_url) as api_client:
        yield api_client


@fixture(scope="session", name="db_session")
def __fixture_db_session():
    with make_sync_session()() as session:
        yield session


@fixture(scope="session", name="mixer")
def __fixture_mixer():
    return Mixer(session=make_sync_session()(), factory=CustomGenFactory)
