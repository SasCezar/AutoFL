import keyword
from pathlib import Path

from tree_sitter import Language, Parser
import tree_sitter_python as tsp
from parser.extensions import Extension
from parser.parser import ParserBase


class PythonParser(ParserBase, lang=Extension.python.name):
    """
    Python specific parser. Uses a generic grammar for multiple versions of python. Uses tree_sitter to get the AST
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(tsp.language())
        self.parser: Parser = Parser(self.language)
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        """
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        self.keywords = set(keyword.kwlist)  # Use python's built in keyword list
        self.keywords.update(['self', 'cls'])
