```python
import json
from pathlib import Path
from typing import Iterator, Dict, Any

import hydra
from omegaconf import DictConfig
from datasets import Dataset, Features, Value, Sequence


def gen_file_examples(data_dir: str) -> Iterator[Dict[str, Any]]:
    """
    Yield one example per file from all project JSONs in data_dir.
    """
    for json_path in Path(data_dir).glob("*.json"):
        proj = json.loads(json_path.read_text(encoding="utf-8"))

        # Required fields: direct indexing for guaranteed presence
        project = proj["name"]
        remote = proj["remote"]
        languages = proj["languages"]

        for version in proj["versions"]:
            commit_id = version["commit_id"]
            commit_num = version["commit_num"]
            commit_date = version["commit_date"]

            for file_info in version["files"].values():
                annotation = file_info['annotation']

                yield {
                    "project": project,
                    "remote": remote,
                    "languages": languages,
                    "commit_id": commit_id,
                    "commit_num": commit_num,
                    "commit_date": commit_date,
                    "file_path": file_info["path"],
                    "language": file_info["language"],
                    "content": file_info["content"],
                    "identifiers": file_info.get("identifiers", []),
                    **annotation,
                }


@hydra.main(config_path="../../config", config_name="main", version_base="1.3")
def convert_to_hf(cfg: DictConfig):
    data_folder = cfg.data_path

    # Define explicit Features schema
    features = Features({
        "project":     Value("string"),
        "remote":      Value("string"),
        "languages":   Sequence(Value("string")),
        "commit_id":   Value("string"),
        "commit_num":  Value("int32"),
        "commit_date": Value("string"),
        "file_path":   Value("string"),
        "language":    Value("string"),
        "content":     Value("string"),
        "identifiers": Sequence(Value("string")),
        "distribution":   Sequence(Value("float32")),
        "unannotated":    Value("int32"),
        "raw_annotation": Sequence(Value("float32")),
    })

    ds = Dataset.from_generator(
        lambda: gen_file_examples(data_folder),
        features=features
    )
    print(ds)


if __name__ == "__main__":
    convert_to_hf()

