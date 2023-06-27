import logging
from abc import ABC
from pathlib import Path
from typing import List, Tuple

from tree_sitter import Parser, Language, Node

from entity.project import File
from parser.languages import register

logger = logging.getLogger(__name__)


class ParserBase(ABC):
    """
    Abstract class for a programming language parser.
    """

    def __init__(self, languages: Path | str):
        self.languages = languages
        self.parser = Parser()
        self.language: Language = None
        self.identifiers_pattern: str = ""
        self.identifiers_query = None
        self.keywords = set()

    def parse(self, file: File) -> List[str]:
        """
        :param file:
        :return:
        """
        code = bytes(file.content, "utf8")
        tree = self.parser.parse(code)
        identifiers_nodes = self.identifiers_query.captures(tree.root_node)
        identifiers = self.parse_identifiers(code, identifiers_nodes)
        identifiers = [x for x in identifiers if x not in self.keywords]
        return identifiers

    @staticmethod
    def parse_identifiers(code, identifiers_nodes: List[Tuple[Node, str]]) -> List[str]:
        identifiers = []
        for node, _ in identifiers_nodes:
            token = code[node.start_byte:node.end_byte]
            identifiers.append(token.decode())

        return identifiers

    def __init_subclass__(cls, lang: str):
        ParserFactory.register(lang, parser_class=cls)


class ParserFactory:
    """ The factory class for creating parsers"""

    registry = {}
    """ Internal registry for available parsers """

    @classmethod
    def register(cls, lang: str, parser_class: ParserBase):
        cls.registry[lang] = parser_class

    @classmethod
    def create_parser(cls, name: str, library_path: Path | str, **kwargs) -> 'ParserBase':
        try:
            return cls.registry[name](library_path)
        except KeyError:
            raise ValueError(f"Unknown parser : {name}")


# Keep here. Allows for the self register of the language specific parser in the language folder
register()
