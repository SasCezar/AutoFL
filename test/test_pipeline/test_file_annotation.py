import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.project import ProjectBuilder
from pipeline.file_annotation import FileAnnotationPipeline


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        self.project = ProjectBuilder().build('Waikato|weka-3.8',
                                              f'{self.cfg.test_data}/repository',
                                              ['java'],
                                              'https://github.com/Waikato/weka-3.8')

        self.lf: LFBase = instantiate(self.cfg.lf)
        self.transformation: TransformationBase = instantiate(self.cfg.transformation)
        self.filtering: FilteringBase = instantiate(self.cfg.filtering)

        self.pipeline = FileAnnotationPipeline(self.lf,
                                               self.filtering,
                                               self.transformation)

    def test_pipeline(self):
        self.pipeline.run(self.project)


if __name__ == '__main__':
    unittest.main()
