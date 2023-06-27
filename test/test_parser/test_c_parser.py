import unittest
from pathlib import Path

from hydra import initialize, compose

from entity.file import File
from parser.extensions import Extension
from parser.parser import ParserFactory, ParserBase


class TestPythonParser(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        file_path = Path(self.cfg.test_data_path).joinpath(Path('parser/cgraphics.c'))
        content = self.load_file(file_path)
        self.file = File(path=file_path, language=Extension.c.name, content=content)
        self.parser: ParserBase = ParserFactory.create_parser(self.file.language, self.cfg.languages_library)
        self.gt = []

    def test_identifiers(self):
        identifiers = self.parser.parse(self.file)
        print(identifiers)
        print(self.gt)
        self.assertListEqual(identifiers, self.gt)

    @staticmethod
    def load_file(path):
        with open(path, 'rt') as inf:
            return "".join(inf.readlines())


if __name__ == '__main__':
    unittest.main()
