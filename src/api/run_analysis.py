from typing import List

from hydra.utils import instantiate
from omegaconf import DictConfig

from annotation.annotator import Annotator
from ensemble.ensemble import EnsembleBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.annotation import AnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.package_annotation import PackageAnnotationPipeline
from pipeline.project_annotation import ProjectAnnotationPipeline
from utils.instantiators import instantiate_annotators
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class RunAnalysis:
    def __init__(self, cfg: DictConfig):
        self.taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)

        self.ensemble: EnsembleBase = instantiate(cfg.annotator.ensemble)
        self.annotators: List[Annotator] = instantiate_annotators(cfg.annotator.annotators, self.taxonomy)

        self.identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)

        self.file_annotation = FileAnnotationPipeline(self.annotators, self.ensemble, self.taxonomy)

        self.package_annotation = PackageAnnotationPipeline() if cfg.package_annotation else None
        self.project_annotation = ProjectAnnotationPipeline() if cfg.project_annotation else None

        self.version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
        self.vcs = VCS()

        self.execution = AnnotationExecution(self.identifier_extraction,
                                             self.file_annotation,
                                             self.package_annotation,
                                             self.project_annotation,
                                             self.version_strategy,
                                             self.vcs)

    def run(self, project: Project):
        return self.execution.run(project)
