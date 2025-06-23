import json
from pathlib import Path

import hydra
from omegaconf import DictConfig
import pandas as pd


@hydra.main(config_path="../../config", config_name="main", version_base="1.3")
def reformat(cfg: DictConfig):
    file = Path(cfg.data_path).joinpath('raw/project_list.json')
    file_out = Path(cfg.data_path).joinpath('raw/project_list.csv')

    projects = []
    with open(file, 'r') as f:
        for line in f:
            data = json.loads(line)
            projects.append([data["full_name"], data["language"], data["topics"]])
    df = pd.DataFrame(projects, columns=["full_name", "language", "labels"])
    df.to_csv(file_out, index=False)

if __name__ == '__main__':
    reformat()
