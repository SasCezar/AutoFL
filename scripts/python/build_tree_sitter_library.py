from os.path import join

import hydra
from omegaconf import DictConfig
from tree_sitter import Language


@hydra.main(config_path="../../config", config_name="main", version_base="1.3")
def build_library(cfg: DictConfig):
    languages = ['java', 'python', 'cpp', 'c-sharp', 'c']
    repositories = [join(cfg.grammars_path, f'tree-sitter-{pl}') for pl in languages]
    Language.build_library(
        # Store the library in the `build` directory
        cfg.languages_library,

        # Include one or more languages
        repositories
    )


if __name__ == '__main__':
    build_library()
