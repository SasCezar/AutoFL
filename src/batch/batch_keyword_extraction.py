from functools import partial
from typing import List

import hydra
from hydra.utils import instantiate
from joblib import delayed, Parallel
from more_itertools import chunked
from omegaconf import DictConfig, OmegaConf

from dataloader.dataloader import DataLoaderBase
from entity.project import Project
from execution.keyword_extraction import KeywordExtractionExecution
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.keyword_extraction import KeywordExtractionPipeline
from pipeline.pipeline import BatchPipeline
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase
from writer.writer import WriterBase


@hydra.main(config_path="../../config", config_name="runs", version_base="1.3")
def extract_keywords(cfg: DictConfig):
    dataloader: DataLoaderBase = instantiate(cfg.dataloader)
    keyword_cfg = OmegaConf.to_container(cfg.annotator, resolve=True) if cfg else {}
    projects: List[Project] = dataloader.find_projects(keyword_cfg)

    keyword_extractor = instantiate(cfg.keyword_extraction)
    keyword_extraction = KeywordExtractionPipeline(keyword_extractor)

    identifier_extraction = IdentifierExtractionPipeline(cfg.languages_library)
    version_strategy: VersionStrategyBase = instantiate(cfg.version_strategy)
    vcs = VCS()

    execution = KeywordExtractionExecution(
        identifier_extraction, keyword_extraction, version_strategy, vcs
    )

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


if __name__ == "__main__":
    extract_keywords()
