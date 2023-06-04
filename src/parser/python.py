from entity.project import File
from parser.parser import AbstractParser


class ParserPython(AbstractParser):
    """
    Python code parser. The lexer and parser have been generated using a version agnostic python grammar for antlr4.
    """

    def parse(self, file: File):
        pass
