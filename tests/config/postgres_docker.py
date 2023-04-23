import time

import docker
import psycopg2

import alembic.command
import alembic.config
from src.config.environemnt import env


class PostgresDocker:
    def __init__(self):
        self.config = {
            "image": "postgres",
            "name": "library_db_test",
            "detach": True,
            "remove": True,
            "environment": {"POSTGRES_USER": env.db_user, "POSTGRES_PASSWORD": env.db_pass, "POSTGRES_DB": env.db_name},
            "ports": {"5432/tcp": env.db_port},
        }
        self.container = None
        self.__read_sql_files()

    def __read_sql_files(self):
        with open(env.base_path / "tests/config/reset_database.sql", "r") as sql_file:
            print("Reading Reset Database sql file")
            self.reset_database_sql = sql_file.read()

    def run(self):
        print("Connecting to docker engine")
        docker_client = docker.from_env()
        for container in filter(lambda x: x.name == "library_db_test", docker_client.containers.list()):
            container.stop()
            print("Stop library_db_test")
        self.container = docker_client.containers.run(**self.config)
        print("Running postgres on docker container")

    @staticmethod
    def wait_until_ready():
        while True:
            try:
                conn = psycopg2.connect(**env.db_dsn)
                conn.close()
                print("Postgres ready!")
                break
            except psycopg2.OperationalError:
                print("Waiting for PostgreSQL to start up...")
                time.sleep(1)

    def stop(self):
        if self.container:
            print("Stopping container")
            self.container.stop()

    @staticmethod
    def run_migrations():
        print("Running migrations")
        alembic_cfg = alembic.config.Config()
        alembic_cfg.set_main_option("script_location", str(env.base_path / "alembic"))
        alembic.command.upgrade(alembic_cfg, "head")

    def reset(self):
        conn = psycopg2.connect(**env.db_dsn)
        cursor = conn.cursor()
        print("Running Reset Database")
        cursor.execute(self.reset_database_sql)
        cursor.close()
        conn.commit()
        conn.close()
