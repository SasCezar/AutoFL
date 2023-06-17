import re

from entity.file import File
from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser
from parser.parser import ParserBase


class ParserJava(ParserBase, lang='java'):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. The parser is generated using antlr4.
    """

    def __init__(self):
        super().__init__()
        self.parser = JavaParser
        self.lexer = JavaLexer
        self.identifiers_re = re.compile(r"identifier (\w*)")

    def parse(self, file: File):
        ast = self._parse(file.content)
        identifiers = self.identifiers_re.findall(str(ast))

        return identifiers
