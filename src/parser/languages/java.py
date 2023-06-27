from pathlib import Path

from tree_sitter import Language

from parser.language import Language
from parser.parser import ParserBase


class JavaParser(ParserBase, lang=Language.java.name):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. It uses tree_sitter.
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(library_path, Language.java.name)
        self.parser.set_language(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        ((type_identifier) @type)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set()
