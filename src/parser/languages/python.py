import re

from entity.project import File
from grammars.python.PythonLexer import PythonLexer
from grammars.python.PythonParser import PythonParser

from parser.parser import ParserBase


class ParserPython(ParserBase, lang='python'):
    """
    Python code parser. The lexer and parser have been generated using a version agnostic python grammar for antlr4.
    """

    def __init__(self):
        super().__init__()
        self.lexer = PythonLexer
        self.parser = PythonParser
        self.identifiers_re = re.compile(r"name (\w*)")
        self.root = lambda x: x.file_input()

    def parse(self, file: File):
        ast = self._parse(file.content.strip().replace(r'\n\s+', r'\n'))
        print(ast)
        identifiers = self.identifiers_re.findall(str(ast))

        return identifiers
