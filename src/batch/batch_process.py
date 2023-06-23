import hydra
from hydra.utils import instantiate
from joblib import delayed, Parallel
from more_itertools import chunked
from omegaconf import DictConfig

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.taxonomy import KeywordTaxonomy
from execution.file_annotation import FileAnnotationExecution
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.pipeline import BatchPipeline


@hydra.main(config_path="../conf", config_name="runs", version_base="1.3")
def extract(cfg: DictConfig):
    loader = instantiate(cfg.loader)
    projects = loader.load()

    taxonomy: KeywordTaxonomy = instantiate(cfg.taxonomy)
    lf: LFBase = instantiate(cfg.lf, taxonomy=taxonomy)

    transformation: TransformationBase = instantiate(
        cfg.transformation) if cfg.transformation._target_ else None
    filtering: FilteringBase = instantiate(cfg.filtering) if cfg.filtering._target_ else None

    annotation = FileAnnotationPipeline(lf,
                                        filtering,
                                        transformation)

    identifier_extraction = IdentifierExtractionPipeline()
    version_strategy = None

    execution = FileAnnotationExecution(identifier_extraction, annotation, version_strategy)

    pipeline: BatchPipeline = instantiate(cfg.batch_pipeline)

    if cfg.workers > 1:
        splits = list(chunked(projects, cfg.workers))
        Parallel(n_jobs=cfg.workers)(delayed(pipeline.run)(x) for x in splits)
    else:
        pipeline.run(projects)


if __name__ == '__main__':
    extract()
