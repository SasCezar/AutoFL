from abc import ABC, abstractmethod
from collections import deque

from tree_sitter import Parser, Tree

from entity.project import File


class AbstractParser(ABC):
    """
    Abstract class for a programming language parser.
    """

    def __init__(self):
        self.parser = Parser()

    @abstractmethod
    def parse(self, file: File):
        """

        :param file:
        :return:
        """
        pass