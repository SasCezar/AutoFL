from pathlib import Path

from tree_sitter import Language, Parser
import tree_sitter_c_sharp as tscs
from parser.extensions import Extension
from parser.parser import ParserBase


class CSharpParser(ParserBase, lang=Extension.c_sharp.name):
    """
    CSharp specific parser. Uses a generic grammar for multiple versions of CSharp. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(tscs.language())
        self.parser: Parser = Parser(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set()
