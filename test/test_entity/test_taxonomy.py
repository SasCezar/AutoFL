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
        self.assertEqual(len(self.taxonomy), 4)
        self.assertEqual(len(self.taxonomy.name_to_label), len(self.taxonomy.id_to_label))

    def test_access(self):
        self.assertEqual(self.taxonomy.name_to_label['3D computer graphics'].index, 0)
        self.assertEqual(self.taxonomy.id_to_label[0].name, '3D computer graphics')
        self.assertEqual(self.taxonomy.id_to_label[3].name, 'Bidirectional recurrent neural networks')


if __name__ == '__main__':
    unittest.main()
