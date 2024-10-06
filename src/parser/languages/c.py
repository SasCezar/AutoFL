from pathlib import Path

from tree_sitter import Language, Parser
import tree_sitter_c as tsc
from parser.extensions import Extension
from parser.parser import ParserBase


class CParser(ParserBase, lang=Extension.c.name):
    """
    C specific parser. Uses a generic grammar for multiple versions of c. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(tsc.language())
        self.parser: Parser = Parser(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        ((type_identifier) @type)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = {'malloc'}
