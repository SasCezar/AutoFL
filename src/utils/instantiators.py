from typing import List

from hydra.utils import instantiate
from loguru import logger
from omegaconf import DictConfig

from annotation import LFBase


def instantiate_lfs(lfs_cfg: DictConfig, taxonomy):
    lfs: List[LFBase] = []

    for _, cb_conf in lfs_cfg.items():
        if isinstance(cb_conf, DictConfig) and "_target_" in cb_conf:
            logger.info(f"Instantiating callback <{cb_conf._target_}>")
            lfs.append(instantiate(cb_conf, taxonomy=taxonomy))

    return lfs
