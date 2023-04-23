import pathlib
import time

import docker
import psycopg2

import alembic.command
import alembic.config


class PostgresDocker:
    def __init__(self):
        self.config = {
            "image": "postgres",
            "name": "library_db_test",
            "detach": True,
            "remove": True,
            "environment": {"POSTGRES_USER": "user", "POSTGRES_PASSWORD": "pass", "POSTGRES_DB": "library_db"},
            "ports": {"5432/tcp": "5432"},
        }
        self.dsn = {"host": "localhost", "user": "user", "password": "pass", "port": "5432", "database": "library_db"}
        self.container = None
        self.base_dir = pathlib.Path(__file__).parents[2]
        self.__read_sql_files()

    def __read_sql_files(self):
        with open(self.base_dir / "tests/config/reset_database.sql", "r", encoding="UTF-8") as sql_file:
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

    def wait_until_ready(self):
        while True:
            try:
                conn = psycopg2.connect(**self.dsn)
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

    def run_migrations(self):
        print("Running migrations")
        alembic_cfg = alembic.config.Config()
        alembic_cfg.set_main_option("script_location", str(self.base_dir / "alembic"))
        alembic.command.upgrade(alembic_cfg, "head")

    def reset(self):
        conn = psycopg2.connect(**self.dsn)
        cursor = conn.cursor()
        print("Running Reset Database")
        cursor.execute(self.reset_database_sql)
        cursor.close()
        conn.commit()
        conn.close()
