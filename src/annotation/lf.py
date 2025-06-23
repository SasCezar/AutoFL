from abc import ABC

import numpy as np

from entity.taxonomy import TaxonomyBase


class LFBase(ABC):
    """
    Abstract labelling function. Uses to annotate
    """

    def __init__(self, taxonomy: TaxonomyBase):
        """
        Taxonomy containing labels to annotate the examples with.
        :param taxonomy:
        """
        self.taxonomy = taxonomy
        self.content = True

    def annotate(self, name: str, content: str) -> np.array:
        """
        Annotate an example given the file name and it's content.
        :param name: Source file name
        :param content: Content of the file (usually identifiers)
        :return:
        """
        pass
