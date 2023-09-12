from abc import ABC
from typing import List, Union

import numpy as np


class EnsembleBase(ABC):
    def __init__(self):
        pass

    def __call__(self, annotations: List[Union[np.array, List]], *args, **kwargs):
        self.run(annotations)

    def run(self, annotations: List[Union[np.array, List]]):
        pass
