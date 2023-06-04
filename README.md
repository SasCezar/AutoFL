# AutoFL

### Development

#### Add Grammars 

For the current version, we are compiling the grammars using ANTLR version 4.9.3. To add more grammars, execute the 
commands in [./scripts/bash/antlr_install.sh](./scripts/bash/antlr_install.sh).

Or use the Docker for ANTLR in  [./docker/antlr/Dockerfile](./docker/antlr/Dockerfile). Check the README in the folder
for more details.

Then use the following commands (in order) to build your grammar:

```shell
antlr4 -Dlanguage=Python3 ParserGrammar.g4 -o outputdir/
antlr4 -Dlanguage=Python3 LexerGrammar.g4 -o outputdir/
```
