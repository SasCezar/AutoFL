import unittest
from pathlib import Path

from fastapi.encoders import jsonable_encoder
from hydra import initialize, compose
from hydra.utils import instantiate

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.file_annotation import FileAnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        name = 'Waikato|weka-3.8'
        self.project = Project(name=name,
                               dir_path=Path(f'{self.cfg.test_data_path}/repository/{name}'),
                               languages=['java'],
                               remote='https://github.com/Waikato/weka-3.8')

        self.taxonomy: KeywordTaxonomy = instantiate(self.cfg.taxonomy)
        self.lf: LFBase = instantiate(self.cfg.lf, taxonomy=self.taxonomy)

        self.transformation: TransformationBase = instantiate(self.cfg.transformation
                                                              ) if self.cfg.transformation._target_ else None
        self.filtering: FilteringBase = instantiate(self.cfg.filtering) if self.cfg.filtering._target_ else None

        self.annotation = FileAnnotationPipeline(self.lf,
                                                 self.filtering,
                                                 self.transformation)

        self.identifier_extraction = IdentifierExtractionPipeline(self.cfg.languages_library)
        self.version_strategy: VersionStrategyBase = instantiate(self.cfg.version_strategy)
        self.vcs = VCS()

        self.execution = FileAnnotationExecution(self.identifier_extraction,
                                                 self.annotation,
                                                 self.version_strategy,
                                                 self.vcs)

    def test_pipeline(self):
        res = self.execution.run(self.project)
        exclude_keys = {'versions': {'__all__': {'files'}}}
        print( jsonable_encoder(res.dict(exclude=exclude_keys)))
        lengths = [len(x.identifiers) for x in res.versions[0].files]
        print(lengths)


if __name__ == '__main__':
    unittest.main()
