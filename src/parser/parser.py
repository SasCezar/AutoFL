from abc import ABC, abstractmethod

from entity.project import File


class AbstractParser(ABC):
    """
    Abstract class for a programming language parser.
    """
    @abstractmethod
    def parse(self, file: File):
        """

        :param file:
        :return:
        """
        pass