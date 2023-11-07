import glob
import json
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Union

import pandas as pd


@dataclass
class LabelBase(ABC):
    index: int
    name: str


@dataclass
class KeywordLabel(LabelBase):
    index: int
    name: str
    keywords: Dict[str, set]
    weights: Dict[str, Dict[str, float]]


class TaxonomyBase(ABC):
    """
    Class defining the taxonomy of the project. Each taxonomy has a path, a mapping between the label name and the label
    index and a mapping between the label index and the label name.
    """
    def __init__(self, path: Union[str, Path]):
        self.path = path
        self.name_to_label: Dict[str, LabelBase] = {}
        self.id_to_label: Dict[int: LabelBase] = {}
        self.n = 0

    @abstractmethod
    def load(self):
        pass

    def __getitem__(self, item: str | int):
        if isinstance(item, str):
            return self.name_to_label[item]
        else:
            return self.id_to_label[item]

    def __len__(self):
        return len(self.name_to_label)

    def __iter__(self):
        return self

    def __next__(self) -> LabelBase:
        if self.n < len(self):
            label = self.id_to_label[self.n]
            self.n += 1
            return label
        else:
            self.n = 0
            raise StopIteration

    def __str__(self):
        return str([self.name_to_label[x] for x in self.name_to_label])


class KeywordTaxonomy(TaxonomyBase):
    """
    Class defining a taxonomy with keywords and weights for each label.
    """
    def __init__(self, path: Union[str, Path], keywords_path: Union[str, Path]):
        super().__init__(path)
        self.keywords_path: str = keywords_path
        self.load()

    def load(self):
        """
        Loads the taxonomy labels with the keywords and weights
        :return:
        """
        with open(self.path, 'rt') as inf:
            labels = json.load(inf)

        keywords_folders = []
        keywords = defaultdict(dict)
        weights = defaultdict(dict)
        for folder in keywords_folders:
            keywords_files = [Path(x) for x in glob.glob(f"{self.keywords_path}/{folder}/*.csv")]
            for file in keywords_files:
                kw_weight = list(zip(pd.read_csv(file)['keyword'], pd.read_csv(file)['tfidf']))
                keywords[folder][file.stem] = set([kw for kw, _ in kw_weight])
                for kw, w in kw_weight:
                    weights[folder][file.stem][kw] = w

        for folder in keywords_folders:
            for name, idx in labels.items():
                    label = KeywordLabel(index=idx, name=name, keywords=keywords[folder][name], weights=weights[folder][name])
                    self.name_to_label[name] = label
                    self.id_to_label[idx] = label
