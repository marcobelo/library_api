import pathlib

from dotenv import load_dotenv

base_path = pathlib.Path(__file__).parents[1]
env_path = base_path / "envs/env_test"

load_dotenv(env_path)
