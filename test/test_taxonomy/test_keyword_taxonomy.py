import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from entity.taxonomy import KeywordTaxonomy


class TestKeywordTaxonomy(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        self.taxonomy: KeywordTaxonomy = instantiate(self.cfg.taxonomy)

    def test_load(self):
        print(self.taxonomy)
