from pathlib import Path
from typing import Dict, List

from tree_sitter import Language, Tree, Parser, Node
import tree_sitter_java as tsjava
from parser.extensions import Extension
from parser.parser import ParserBase


class JavaParser(ParserBase, lang=Extension.java.name):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(tsjava.language())
        self.parser: Parser = Parser(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        ((type_identifier) @type)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set()

        self.package_pattern = """
                               (package_declaration ((
                                                    scoped_identifier scope: (
                                                        scoped_identifier scope: (identifier) name: (identifier)
                                                    ) 
                                                    name: (identifier)
                                                    )) @package
                               )
                             """

        self.package_query = self.language.query(self.package_pattern)

    def get_package(self, file: Path, code: bytes, tree: Tree) -> str:
        package = self.package_query.captures(tree.root_node)
        if package:
            return self.get_node_text(code, package)[0]

        return '.'
