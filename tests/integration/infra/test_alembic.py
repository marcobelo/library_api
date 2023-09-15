import alembic.command
import alembic.config
from src.config.environemnt import env


class TestAlembic:
    def test_check_if_everything_is_generated(self):
        alembic_cfg = alembic.config.Config()
        alembic_cfg.set_main_option("script_location", str(env.base_path / "alembic"))
        alembic.command.check(alembic_cfg)
