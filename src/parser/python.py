from entity.project import File
from grammars.python.PythonLexer import PythonLexer
from grammars.python.PythonParser import PythonParser
from parser.parser import AbstractParser
from antlr4 import *


class ParserPython(AbstractParser):
    """
    Python code parser. The lexer and parser have been generated using a version agnostic python grammar for antlr4.
    """

    def parse(self, file: File):
        lexer = PythonLexer(file.content)
        stream = CommonTokenStream(lexer)
        parser = PythonParser(stream)
        tree = parser.file_input()
        file.tree = tree
        return file

