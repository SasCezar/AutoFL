import unittest

from hydra import initialize, compose


class TestGitRankingTaxonomy(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="main.yaml")

    def test_load(self):
        print(self.cfg)
        self.assertTrue(True)

    def test_save(self):
        print('Fail', self.cfg)
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
