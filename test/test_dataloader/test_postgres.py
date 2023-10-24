import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from dataloader.postgres_dataloader import PostgresProjectLoader
from entity.project import Project, Version


class TestPostgres(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml", overrides=["dataloader=postgres"])

    def test_load_project_name(self):
        dataloader: PostgresProjectLoader = instantiate(self.cfg.dataloader)
        projects = dataloader.find_projects()
        self.assertGreater(len(list(projects)), 0)

    def test_load_project(self):
        dataloader: PostgresProjectLoader = instantiate(self.cfg.dataloader)
        project_names = list(dataloader.find_projects())
        projects = list(dataloader.load(project_names))
        self.assertGreater(len(projects), 0)
        self.assertIsInstance(projects[0], Project)
        self.assertGreater(len(projects[0].versions), 0)
        self.assertIsInstance(projects[0].versions[0], Version)
