# AutoFL

Automatic source code file labelling using weak labelling.

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

In order to support more languages, a new language specific parser. We do so by using [tree-sitter](https://tree-sitter.github.io/tree-sitter/) grammars, 
and creating a wrapper around the generated parsers. 

#### Grammars

#### Parser Wrapper

The generated ANTLR4 parsers need to be wrapped in a class to standardize the interface. 
