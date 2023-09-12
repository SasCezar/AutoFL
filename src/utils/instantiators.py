from typing import List

from hydra.utils import instantiate
from loguru import logger
from omegaconf import DictConfig

from annotation.annotator import Annotator


def instantiate_annotators(annotators_cfg: DictConfig, taxonomy):
    annotators: List[Annotator] = []

    for name, cb_conf in annotators_cfg.items():
        if isinstance(cb_conf, DictConfig):
            logger.info(f"Instantiating annotator <{name}>")
            lf = instantiate(cb_conf['lf'], taxonomy=taxonomy)
            filtering = instantiate(cb_conf['filtering']) if cb_conf['filtering']['_target_'] else None
            transformation = instantiate(cb_conf['transformation']) if cb_conf['transformation']['_target_'] else None
            annotators.append(Annotator(lf, filtering, transformation))

    return annotators
