from functools import partial
from typing import List

import hydra
from hydra.utils import instantiate
from joblib import delayed, Parallel
from more_itertools import chunked
from omegaconf import DictConfig, OmegaConf

from annotation.annotator import Annotator
from dataloader.dataloader import DataLoaderBase
from ensemble.ensemble import EnsembleBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.annotation import AnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.package_annotation import PackageAnnotationPipeline
from pipeline.pipeline import BatchPipeline
from pipeline.project_annotation import ProjectAnnotationPipeline
from utils.instantiators import instantiate_annotators
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase
from writer.writer import WriterBase


@hydra.main(config_path="../../config", config_name="runs", version_base="1.3")
def annotate(cfg: DictConfig):
    dataloader: DataLoaderBase = instantiate(cfg.dataloader)
    annot_cfg = OmegaConf.to_container(cfg.annotator, resolve=True)
    projects: List[Project] = dataloader.find_projects(annot_cfg)
    taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)
    ensemble: EnsembleBase = instantiate(cfg.annotator.ensemble)
    annotators: List[Annotator] = instantiate_annotators(cfg.annotator.annotators, taxonomy)

    file_annotation = FileAnnotationPipeline(annotators,
                                             ensemble,
                                             taxonomy,
                                             cfg=annot_cfg)

    package_annotation = PackageAnnotationPipeline() if cfg.package_annotation else None
    project_annotation = ProjectAnnotationPipeline() if cfg.project_annotation else None

    identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)
    version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
    vcs = VCS()

    execution = AnnotationExecution(identifier_extraction,
                                    file_annotation,
                                    package_annotation,
                                    project_annotation,
                                    version_strategy,
                                    vcs)

    pipeline = partial(run, execution, cfg)

    if cfg.n_workers > 1:
        splits = list(chunked(projects, cfg.workers))
        Parallel(n_jobs=cfg.workers)(delayed(pipeline)(x) for x in splits)
    else:
        pipeline(projects)


def run(execution, cfg, projects):
    dataloader: DataLoaderBase = instantiate(cfg.dataloader)
    writer: WriterBase = instantiate(cfg.writer)
    pipeline: BatchPipeline = BatchPipeline(execution, dataloader, writer)

    pipeline.run(projects)


if __name__ == '__main__':
    annotate()
