from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Tuple

from tree_sitter import Parser, Language, Node, Tree

from entity.project import File
from parser.languages import register


class ParserBase(ABC):
    """
    Abstract class for a programming language parser.
    """

    def __init__(self, library_path: Path | str):
        """
        :param library_path: Path to the tree-sitter languages.so file. The file has to contain the
        language parser. See tree-sitter for more details
        """
        self.library_path = library_path
        self.parser = Parser()
        self.language: Language = None
        self.identifiers_pattern: str = ""
        self.identifiers_query = None
        self.keywords = set()

    def parse(self, file: File) -> Tuple[List[str], str]:
        """
        :param file:
        :return:
        """
        code = bytes(file.content, "utf8")
        tree = self.parser.parse(code)
        identifiers_nodes = self.identifiers_query.captures(tree.root_node)
        identifiers = self.get_node_text(code, identifiers_nodes)
        identifiers = [x for x in identifiers if x not in self.keywords]
        package = self.get_package(file.path, code, tree)
        return identifiers, package

    @staticmethod
    def get_node_text(code: bytes, identifiers_nodes: dict[str, list[Node]]) -> List[str]:
        identifiers = []
        for type in identifiers_nodes:
            for node in identifiers_nodes[type]:
                token = code[node.start_byte:node.end_byte]
                identifiers.append(token.decode())

        return identifiers

    def get_package(self, file: str, code: bytes, root: Tree) -> str:
        package = '.'

        return package

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
    def create_parser(cls, name: str, library_path: Path | str, **kwargs) -> ParserBase:
        try:
            return cls.registry[name](library_path)
        except KeyError:
            raise ValueError(f"Unknown parser : {name}")


# Keep here. Allows for the self register of the language specific parser in the language folder
register()
