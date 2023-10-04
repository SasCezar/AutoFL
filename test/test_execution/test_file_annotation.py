import unittest
from pathlib import Path
from typing import List

from fastapi.encoders import jsonable_encoder
from hydra import initialize, compose
from hydra.utils import instantiate

from annotation.annotator import Annotator
from ensemble.ensemble import EnsembleBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.file_annotation import FileAnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from utils.instantiators import instantiate_annotators
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        self.taxonomy: KeywordTaxonomy = instantiate(self.cfg.taxonomy)

        self.ensemble: EnsembleBase = instantiate(self.cfg.annotator.ensemble)
        self.annotators: List[Annotator] = instantiate_annotators(self.cfg.annotator.annotators, self.taxonomy)

        self.annotation_pipeline = FileAnnotationPipeline(self.annotators, self.ensemble, self.taxonomy)

        self.identifier_extraction = IdentifierExtractionPipeline(self.cfg.languages_library)
        self.version_strategy: VersionStrategyBase = instantiate(self.cfg.version_strategy)
        self.vcs = VCS()

        self.execution = FileAnnotationExecution(self.identifier_extraction,
                                                 self.annotation_pipeline,
                                                 self.version_strategy,
                                                 self.vcs)
        self.exclude_keys = {'versions': {'__all__': {'files'}}}

    def test_pipeline_java(self):
        project = Project(name='Waikato|weka-3.8',
                          dir_path=f'{self.cfg.test_data_path}/repository/Waikato|weka-3.8',
                          languages=['java'],
                          remote='https://github.com/Waikato/weka-3.8')
        res = self.execution.run(project)
        self.assertEqual(len(res.versions[0].files), 3088)
        print(jsonable_encoder(res.model_dump(exclude=self.exclude_keys)))

    def test_pipeline_python(self):
        project = Project(name='tiangolo|fastapi',
                          dir_path=f'{self.cfg.test_data_path}/repository/tiangolo|fastapi',
                          languages=['python'],
                          remote='https://github.com/tiangolo/fastapi')
        res = self.execution.run(project)
        print(jsonable_encoder(res.model_dump(exclude=self.exclude_keys)))

    def test_pipeline_c(self):
        project = Project(name='tporadowski|redis',
                          dir_path=f'{self.cfg.test_data_path}/repository/tporadowski|redis',
                          languages=['c'],
                          remote='https://github.com/tporadowski/redis')
        res = self.execution.run(project)
        print(jsonable_encoder(res.model_dump(exclude=self.exclude_keys)))


if __name__ == '__main__':
    unittest.main()
