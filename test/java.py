import re

from antlr4 import *

from grammars.java.JavaLexer import JavaLexer
from grammars.java.JavaParser import JavaParser


def main():
    input_stream = InputStream("""// Your First Program

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}""")
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    is_syntax_errors = tree.parser._syntaxErrors  # Binary
    return tree.toStringTree(recog=parser), is_syntax_errors


if __name__ == '__main__':
    ast, is_syntax_errors = main()
    print(ast)
    id_re = re.compile("identifier \w*")
    a = id_re.findall(str(ast))
    print(len(a))
    print(list(a))