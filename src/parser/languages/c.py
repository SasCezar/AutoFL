from pathlib import Path

from tree_sitter import Language

from parser.extensions import Extension
from parser.parser import ParserBase


class CParser(ParserBase, lang=Extension.c.name):
    """
    C specific parser. Uses a generic grammar for multiple versions of c. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(library_path, Extension.c.name)
        self.parser.set_language(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        ((type_identifier) @type)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)\

        self.keywords = {'malloc'}
