from antlr4 import CommonTokenStream

from entity.project import File
from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser
from parser.parser import AbstractParser


class ParserJava(AbstractParser):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. The parser is generated using antlr4.
    """

    def parse(self, file: File):
        lexer = JavaLexer(file.content)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        is_syntax_errors = tree.parser._syntaxErrors  # Binary
        return tree.toStringTree(recog=parser), is_syntax_errors