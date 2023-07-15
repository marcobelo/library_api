from faker import Faker

from tests.config import create_mixer


class BaseFakeFactory:
    fk = Faker()
    mx = create_mixer()
