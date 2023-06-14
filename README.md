# AutoFL

Automatic source code file labelling using weak supervision.

## Usage

Run docker the docker compose file [docker-compose.yaml](docker-compose.yaml) by executing:
```shell
docker compose up
```
in the project folder.

Then you can analyze a project by making a request to the endpoint:
```shell

```

## Development

### Add New Languages 

In order to support more languages, a new language specific parser. We do so by using ANTLR4 grammars, and creating a
wrapper around the generated parsers. 

#### Grammars
For the current version, we are compiling the grammars using ANTLR version 4.9.3. To add more grammars, execute the 
commands in [./scripts/bash/antlr_install.sh](./scripts/bash/antlr_install.sh).

Or use the Docker for ANTLR in  [./docker/antlr/Dockerfile](./docker/antlr/Dockerfile). 
Check the [README](./docker/antlr/README.md) in the folder for more details.

Then use the following commands (in order) to build your grammar:

```shell
antlr4 -Dlanguage=Python3 ParserGrammar.g4 -o outputdir/
antlr4 -Dlanguage=Python3 LexerGrammar.g4 -o outputdir/
```

#### Parser Wrapper

The generated ANTLR4 parsers need to be wrapped in a class to standardize the interface. 
