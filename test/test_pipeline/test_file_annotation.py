import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from entity.project import ProjectBuilder
from annotation import LFBase
from parser.parser import ParserFactory
from pipeline.annotation import FileAnnotationPipeline


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="main.yaml")

        self.project = ProjectBuilder().build('Waikato|weka-3.8', '/home/sasce/PycharmProjects/AutoFL/test/resources/repository',
                                               ['java'], 'https://github.com/Waikato/weka-3.8')

        self.parser = ParserFactory.create_parser('java')
        self.lf: LFBase = instantiate(self.cfg.lf)
        self.pipeline = FileAnnotationPipeline(self.lf)

    def test_pipeline(self):
        self.pipeline.run(self.project)


if __name__ == '__main__':
    unittest.main()
