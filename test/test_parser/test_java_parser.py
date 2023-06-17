import unittest
from pathlib import Path

from hydra import initialize, compose

from entity.file import File
from parser.parser import ParserFactory, ParserBase


class TestJavaParser(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        self.parser: ParserBase = ParserFactory.create_parser('java')
        file_path = Path(self.cfg.test_data_path).joinpath(Path('example_class.java'))
        content = self.load_file(file_path)
        self.file = File(path=file_path, language='java', content=content)

        self.gt = ['Lamp', 'isOn', 'turnOn', 'isOn', 'System', 'out', 'println',
                   'isOn', 'turnOff', 'isOn', 'System', 'out', 'println', 'isOn', 'Main',
                   'main', 'args', 'led', 'Lamp', 'halogen',
                   'Lamp', 'led', 'turnOn', 'halogen', 'turnOff']

    def test_identifiers(self):
        identifiers = self.parser.parse(self.file)
        self.assertListEqual(identifiers, self.gt)

    @staticmethod
    def load_file(path):
        with open(path, 'rt') as inf:
            return " ".join(inf.readlines())


if __name__ == '__main__':
    unittest.main()
