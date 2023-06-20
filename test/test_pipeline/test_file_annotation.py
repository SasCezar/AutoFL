import unittest

from hydra import initialize, compose
from hydra.utils import instantiate

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.project import ProjectBuilder, Project
from entity.taxonomy import KeywordTaxonomy
from pipeline.file_annotation import FileAnnotationPipeline


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        self.project: Project = ProjectBuilder().build('Waikato|weka-3.8',
                                                       f'{self.cfg.test_data_path}/repository',
                                                       ['java'],
                                                       'https://github.com/Waikato/weka-3.8')

        self.taxonomy: KeywordTaxonomy = instantiate(self.cfg.taxonomy)
        self.lf: LFBase = instantiate(self.cfg.lf, taxonomy=self.taxonomy)
        print(self.cfg.transformation)
        self.transformation: TransformationBase = instantiate(
            self.cfg.transformation) if self.cfg.transformation._target_ else None
        self.filtering: FilteringBase = instantiate(self.cfg.filtering) if self.cfg.filtering._target_ else None

        self.pipeline = FileAnnotationPipeline(self.lf,
                                               self.filtering,
                                               self.transformation)

    def test_pipeline(self):
        print(self.pipeline.run(self.project).files_annotation)


if __name__ == '__main__':
    unittest.main()
