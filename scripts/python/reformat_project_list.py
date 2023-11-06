import json
from pathlib import Path

import hydra
import pandas as pd
from omegaconf import DictConfig

from entity.project import Project


@hydra.main(config_path="../../config", config_name="main", version_base="1.3")
def reformat(cfg: DictConfig):
    file = Path(cfg.data_path).joinpath('raw/project_list.csv')
    file_out = Path(cfg.data_path).joinpath('raw/project_list.json')
    labels_out = Path(cfg.data_path).joinpath('raw/labels.json')

    df = pd.read_csv(file)
    all_labels = {}
    with open(file_out, 'wt') as outf:
        for name, language, labels in zip(df["full_name"].tolist(), df["language"].tolist(), df["labels"].tolist()):
            labels = eval(labels)
            project = Project(name=name, languages=[language], dev_labels=labels)

            for label in labels:
                if label not in labels:
                    all_labels[label] = len(all_labels)

            outf.write(project.model_dump_json() + '\n')

    with open(labels_out, 'wt') as outf:
        text = json.dumps(all_labels, ensure_ascii=False, indent=4)
        outf.write(text)


if __name__ == '__main__':
    reformat()
