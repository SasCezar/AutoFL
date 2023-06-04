#!/bin/bash
languages=("java" "python")
grammars_folder="../../resources/grammars"
grammars_out="../../src/grammars"

tc() { set ${*,,} ; echo ${*^} ; }
echo alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
for language in ${languages[@]}; do
  echo antlr4 -Dlanguage=Python3 "$grammars_folder/$language/$(tc "$language")Lexer.g4" -o "$grammars_out/$language/"
  echo antlr4 -Dlanguage=Python3 "$grammars_folder/$language/$(tc "$language")Parser.g4" -o "$grammars_out/$language/"
done