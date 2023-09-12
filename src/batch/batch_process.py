from typing import List

import hydra
from hydra.utils import instantiate
from joblib import delayed, Parallel
from more_itertools import chunked
from omegaconf import DictConfig

from annotation import LFBase
from annotation.annotator import Annotator
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from ensemble.ensemble import EnsembleBase
from entity.project import Project
from entity.taxonomy import KeywordTaxonomy
from execution.file_annotation import FileAnnotationExecution
from loader.loader import LoaderBase
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.pipeline import BatchPipeline
from utils.instantiators import instantiate_lfs
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


@hydra.main(config_path="../../config", config_name="runs", version_base="1.3")
def extract(cfg: DictConfig):
    loader: LoaderBase = instantiate(cfg.loader)
    projects: List[Project] = loader.load()

    taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)
    lfs: List[LFBase] = instantiate_lfs(cfg.lfs, taxonomy)
    ensemble: EnsembleBase = instantiate(cfg.Ensemble)
    annotator: Annotator = Annotator(lfs, ensemble)
    transformation: TransformationBase = instantiate(cfg.transformation) if cfg.transformation._target_ else None
    filtering: FilteringBase = instantiate(cfg.filtering) if cfg.filtering._target_ else None

    annotation = FileAnnotationPipeline(annotator,
                                        filtering,
                                        transformation)

    identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)
    version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
    vcs = VCS()

    execution = FileAnnotationExecution(identifier_extraction,
                                        annotation,
                                        version_strategy,
                                        vcs)

    pipeline: BatchPipeline = BatchPipeline(execution,
                                            "",
                                            exclude='')

    if cfg.workers > 1:
        splits = list(chunked(projects, cfg.workers))
        Parallel(n_jobs=cfg.workers)(delayed(pipeline.run)(x) for x in splits)
    else:
        pipeline.run(projects)


if __name__ == '__main__':
    extract()
