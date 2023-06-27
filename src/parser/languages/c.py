from pathlib import Path

from tree_sitter import Language

from parser.language import Language
from parser.parser import ParserBase


class CParser(ParserBase, lang=Language.c.name):
    """
    C specific parser. Uses a generic grammar for multiple versions of c. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(library_path, Language.c.name)
        self.parser.set_language(self.language)
        self.identifiers_pattern: str = """
                                       
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set()
