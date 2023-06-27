import unittest
from pathlib import Path

from hydra import initialize, compose

from entity.file import File
from parser.parser import ParserFactory, ParserBase


class TestPythonParser(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        file_path = Path(self.cfg.test_data_path).joinpath(Path('parser/keyword.py'))
        content = self.load_file(file_path)
        self.file = File(path=file_path, language='python', content=content)
        self.parser: ParserBase = ParserFactory.create_parser(self.file.language, self.cfg.languages_library)
        self.gt = ['collections', 'Counter', 'numpy', 'np', 'multiset', 'Multiset', 'entity',
                   'taxonomy', 'KeywordLabel', 'annotation', 'LFBase', 'KeywordLF', 'LFBase',
                   'annotate', 'name', 'str', 'content', 'str', 'np', 'array',
                   'node_labels', 'np', 'zeros', 'len', 'taxonomy', '_label', 'taxonomy',
                   'label', 'KeywordLabel', '_label', 'intersection', 'list', 'label', 'keywords', 'intersection',
                   'Multiset', 'content', 'split', 'intersection', 'Counter', 'intersection', 'node_labels', 'label',
                   'index', 'sum', 'intersection', 'k', 'label', 'weights', 'k', 'k', 'intersection', 'keys',
                   'norm', 'np', 'sum', 'node_labels', 'node_vec', 'node_labels', 'norm', 'norm', 'np', 'zeros',
                   'len', 'taxonomy', 'node_vec']

    def test_identifiers(self):
        identifiers = self.parser.parse(self.file)
        self.assertListEqual(identifiers, self.gt)

    @staticmethod
    def load_file(path):
        with open(path, 'rt') as inf:
            return "".join(inf.readlines())


if __name__ == '__main__':
    unittest.main()
