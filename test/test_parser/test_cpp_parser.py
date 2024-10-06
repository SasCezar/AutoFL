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

        file_path = Path(self.cfg.test_data_path).joinpath(Path('parser/bodyPartConnectorCaffe.cpp'))
        content = self.load_file(file_path)
        rel_path = str(file_path.relative_to(self.cfg.test_data_path))
        self.file = File(path=rel_path, language=Extension.cpp.name, content=content)
        self.parser: ParserBase = ParserFactory.create_parser(self.file.language, self.cfg.languages_library)
        self.gt = []

    def test_identifiers(self):
        # TODO
        identifiers, _ = self.parser.parse(self.file)
        self.assertEqual(len(identifiers), len(self.gt))
        self.assertSetEqual(set(identifiers), set(self.gt))


    def test_packages(self):
        # TODO
        # _, packages = self.parser.parse(self.file)
        # self.assertListEqual(packages, self.gt_packages)
        pass

    @staticmethod
    def load_file(path):
        with open(path, 'rt') as inf:
            return "".join(inf.readlines())


if __name__ == '__main__':
    unittest.main()
