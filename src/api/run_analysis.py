from typing import List

from hydra.utils import instantiate
from omegaconf import DictConfig

from annotation import LFBase
from annotation.annotator import Annotator
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from ensemble.ensemble import EnsembleBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.file_annotation import FileAnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from utils.instantiators import instantiate_lfs
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class RunAnalysis:
    def __init__(self, cfg: DictConfig):
        self.taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)
        self.lfs: List[LFBase] = instantiate_lfs(cfg.lfs, self.taxonomy)
        self.ensemble: EnsembleBase = instantiate(cfg.aggregator)
        self.annotator: Annotator = Annotator(self.lfs, self.ensemble)

        self.transformation: TransformationBase = instantiate(cfg.transformation
                                                              ) if cfg.transformation._target_ else None
        self.filtering: FilteringBase = instantiate(cfg.filtering) if cfg.filtering._target_ else None

        self.annotation = FileAnnotationPipeline(self.annotator,
                                                 self.filtering,
                                                 self.transformation)

        self.identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)
        self.version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
        self.vcs = VCS()

        self.execution = FileAnnotationExecution(self.identifier_extraction,
                                                 self.annotation,
                                                 self.version_strategy,
                                                 self.vcs)

    def run(self, project: Project):
        return self.execution.run(project)
