import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from dataloader.gitranking import GitRankingCSVDataLoader


class TestGitRanking(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml", overrides=["dataloader=gitranking"])

    def test_load(self):
        dataloader: GitRankingCSVDataLoader = instantiate(self.cfg.dataloader)
        projects = dataloader.load()
        self.assertEqual(len(projects), 48029)

    def test_filter(self):
        dataloader: GitRankingCSVDataLoader = instantiate(self.cfg.dataloader, languages=['Java'])
        projects = dataloader.load()
        self.assertEqual(len(projects), 3048)
