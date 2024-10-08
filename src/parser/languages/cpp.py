from pathlib import Path

from tree_sitter import Language, Parser
import tree_sitter_cpp as tscpp
from parser.extensions import Extension
from parser.parser import ParserBase


class CPPParser(ParserBase, lang=Extension.cpp.name):
    """
    CPP specific parser. Uses a generic grammar for multiple versions of CPP. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(tscpp.language())
        self.parser: Parser = Parser(self.language)
        # TODO Fix, doesn't work - It doesn't find the namespaced identifiers
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        ((type_identifier) @type)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set()
