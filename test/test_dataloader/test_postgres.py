import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from dataloader.postgres_dataloader import PostgresProjectLoader


class TestPostgres(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml", overrides=["dataloader=postgres"])

    def test_load(self):
        dataloader: PostgresProjectLoader = instantiate(self.cfg.dataloader)
        projects = dataloader.find_projects()
        print(projects)


    def test_filter(self):
        dataloader: PostgresProjectLoader = instantiate(self.cfg.dataloader)
        projects = dataloader.load()
        self.assertEqual(len(projects), 3048)
