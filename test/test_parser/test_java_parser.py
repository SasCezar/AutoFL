import unittest

from hydra import initialize, compose

from entity.file import File
from parser.parser import ParserFactory


class TestJavaParser(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="main.yaml")

        self.parser = ParserFactory.create_parser('java')
        print(self.parser)
        self.file = File(path='./resources/example_class.java')
        self.gt = ['Lamp', 'isOn', 'turnOn', 'isOn', 'System', 'out', 'println',
                   'isOn', 'turnOff', 'isOn', 'System', 'out', 'println', 'isOn', 'Main',
                   'main', 'args', 'led', 'Lamp', 'halogen',
                   'Lamp', 'led', 'turnOn', 'halogen', 'turnOff']

    def test_identifiers(self):
        identifiers = self.parser.parse(self.file)
        self.assertListEqual(identifiers, self.gt)


if __name__ == '__main__':
    unittest.main()
