import hydra
from hydra.utils import instantiate
from joblib import delayed, Parallel
from more_itertools import chunked
from omegaconf import DictConfig

from pipeline.pipeline import BatchPipeline


@hydra.main(config_path="../conf", config_name="runs", version_base="1.3")
def extract(cfg: DictConfig):
    loader = instantiate(cfg.loader)
    projects = loader.load()

    pipeline: BatchPipeline = instantiate(cfg.batch_pipeline)

    if cfg.workers > 1:
        splits = list(chunked(projects, cfg.workers))
        Parallel(n_jobs=cfg.workers)(delayed(pipeline.run)(x) for x in splits)
    else:
        pipeline.run(projects)


if __name__ == '__main__':
    extract()
