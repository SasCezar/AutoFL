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
from utils.instantiators import instantiate_annotators
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class RunAnalysis:
    def __init__(self, cfg: DictConfig):
        self.taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)

        self.ensemble: EnsembleBase = instantiate(cfg.aggregator)
        self.annotators: List[Annotator] = instantiate_annotators(cfg.annotators, self.taxonomy)

        self.annotation_pipeline = FileAnnotationPipeline(self.annotators, self.ensemble)

        self.identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)
        self.version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
        self.vcs = VCS()

        self.execution = FileAnnotationExecution(self.identifier_extraction,
                                                 self.annotation_pipeline,
                                                 self.version_strategy,
                                                 self.vcs)

    def run(self, project: Project):
        return self.execution.run(project)
