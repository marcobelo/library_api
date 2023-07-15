import os
import pathlib

from dotenv import load_dotenv

from src.config.exception import MissingEnvironmentException


class Environment:
    def __init__(self):
        self.base_path = self.__get_base_path()
        self.__load_env_file()
        self.db_user = self.__get_env("DB_USER")
        self.db_pass = self.__get_env("DB_PASS")
        self.db_host = self.__get_env("DB_HOST")
        self.db_port = self.__get_env("DB_PORT")
        self.db_name = self.__get_env("DB_NAME")
        self.db_sync_url = self.__get_db_url()
        self.db_async_url = self.__get_db_url(async_url=True)
        self.db_dsn = self.__get_db_dsn()

        self.page_size = int(self.__get_env("PAGE_SIZE"))
        self.page_min_size = int(self.__get_env("PAGE_MIN_SIZE"))
        self.page_max_size = int(self.__get_env("PAGE_MAX_SIZE"))

    @staticmethod
    def __get_base_path() -> pathlib:
        return pathlib.Path(__file__).parents[2]

    def __load_env_file(self):
        environment = os.getenv("ENVIRONMENT", "DEV")
        running_tests = os.getenv("RUNNING_TESTS", False)
        if environment == "DEV":
            env_path = self.base_path / "envs/env_test"
            load_dotenv(env_path)
        elif not running_tests and environment == "Other envs: uat, stage, prod...":
            pass

    @staticmethod
    def __get_env(env_name: str) -> str:
        env_value = os.getenv(env_name)
        if not env_value:
            raise MissingEnvironmentException("Missing Environment for env=%s" % env_name)
        return env_value

    def __get_db_url(self, async_url: bool = False) -> str:
        prefix = "postgresql+asyncpg://" if async_url else "postgresql://"
        return f"{prefix}{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    def __get_db_dsn(self) -> dict:
        return {
            "user": self.db_user,
            "password": self.db_pass,
            "host": self.db_host,
            "port": self.db_port,
            "database": self.db_name,
        }


env = Environment()
