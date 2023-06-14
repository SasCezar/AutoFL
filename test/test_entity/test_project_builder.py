import unittest

from hydra import initialize, compose

from entity.project import ProjectBuilder


class TestProjectBuilder(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="main.yaml")

        self.builder = ProjectBuilder()

    def test_build(self):
        project = self.builder.build('Waikato|weka-3.8',
                                     '/home/sasce/PycharmProjects/AutoFL/test/resources/repository',
                                     ['java'],
                                     'https://github.com/Waikato/weka-3.8')

        self.assertEqual(len(project.files), 3088)
        self.assertEqual(str(project.files[0].path), 'weka/src/test/java/weka/AllTests.java')


if __name__ == '__main__':
    unittest.main()
