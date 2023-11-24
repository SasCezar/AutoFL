# AutoFL

Automatic source code file annotation using weak labelling.

## Setup
Clone the repository and the UI submodule [autofl-ui](https://github.com/SasCezar/autofl-ui) by running the following command:
```bash
git clone --recursive git@github.com:SasCezar/AutoFL.git AutoFL
```

### Optional Setup 
To make use of certain feature like semantic based labelling functions, you need to download the model.
For example, for **w2v-so**, you can download the model from [here](https://github.com/vefstathiou/SO_word2vec), and place it in the [data/models/w2v-so](data/models/w2v-so) folder, or a custom
path that you can use in the configs.

## Usage

Run docker the docker compose file [docker-compose.yaml](docker-compose.yaml) by executing:
```shell
docker compose up
```
in the project folder.

### API Endpoint
You can analyze the files of project by making a request to the endpoint:
```shell

```
For example, to analyze the files of [](), you can make the following request:
```shell
curl -X POST "http://l
```

### UI

We also offer a web UI that is available at the following page (when running locally):
[http://0.0.0.0:8501](http://0.0.0.0:8501)

![UI](resources/ui-screenshots/landing-page.png)

[//]: # (For more details, check the [UI repo]&#40;https://github.com/SasCezar/autofl-ui&#41;)

## Functionalities

- Annotation (UI/API/Script)
  - File
  - Package (**UI-only** - API/Script)
  - Project (**UI-only** - API/Script)
- Batch Analysis (Script Only)
- Temporal Analysis (**TODO**)
- Classification (**TODO**)

## Supported Languages

- Java
- Python (untested)
- C (untested)
- C++ (untested)
- C# (untested)

## Development

### Add New Languages 

In order to support more languages, a new language specific parser is needed. 
We can create one quickly by using [tree-sitter](https://tree-sitter.github.io/tree-sitter/),
and a custom parser.

#### Parser
The parser needs to be in the [parser/languages](./src/parser/languages) folder. 
It has to extend the ```BaseParser``` class, which has the following interface.

```python
class ParserBase(ABC):
    """
    Abstract class for a programming language parser.
    """

    def __init__(self, library_path: Path | str):
        """
        :param library_path: Path to the tree-sitter languages.so file. The file has to contain the
        language parser. See tree-sitter for more details
        """
        ...
```
And the language specific class has to contain the logic to parse the language to get the identifiers.
For example for Python, the class will look like this:

```python
class PythonParser(ParserBase, lang=Extension.python.name):  # The lang argument is used to register the parser in the ParserFactory class.
    """
    Python specific parser. Uses a generic grammar for multiple versions of python. Uses tree_sitter to get the AST
    """

    def __init__(self, library_path: Path | str):
        super().__init__(library_path)
        self.language: Language = Language(library_path, Extension.python.name)   # Creates the tree-sitter language for python
        self.parser.set_language(self.language)                                   # Sets tree-sitter parser to parse the language
        
        # Pattern used to match the identifiers, it depends on the Lanugage. Check tree-sitter
        self.identifiers_pattern: str = """
                                        ((identifier) @identifier)
                                        """
        
        # Creates the query used to find the identifiers in the AST produced by tree-sitter
        self.identifiers_query = self.language.query(self.identifiers_pattern)

        # Keyword that will be ignored, in this case, the language specific keywords as the query extracts them as well. 
        self.keywords = set(keyword.kwlist)  # Use python's built in keyword list
        self.keywords.update(['self', 'cls'])
```

A custom class that does not rely on [tree-sitter](https://github.com/tree-sitter/tree-sitter) can be also used, however, there are more methods from ParserBase that need to be
changed. Check the implementation of [ParserBase](src/parser/parser.py).

## Disclaimer

The project is still in development, and it might not work as expected in some cases.
It has been developed and tested on Ubuntu 22.04, while it uses Docker, it might not work on other operating systems as 
intended.

In case of any problems, please open an issue, make a pull request, or contact me at ```c.a.sas@rug.nl```.


## Cite

If you use this work please cite us:

### Paper
```text
@misc{sas2023multigranular,
      title={Multi-granular Software Annotation using File-level Weak Labelling}, 
      author={Cezar Sas and Andrea Capiluppi},
      year={2023},
      eprint={2311.11607},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```
**Note**: The code used in the paper is available in the [https://github.com/SasCezar/CodeGraphClassification](https://github.com/SasCezar/CodeGraphClassification) repository. 
However, this tool is more up to date and is easier to use, configurable, and a more production level code.

### Tool 
```text
@software{Sas_AutoFL_2023,
          author = {Sas, Cezar and Capiluppi, Andrea},
          month = sep,
          title = {{AutoFL}},
          url = {https://github.com/SasCezar/AutoFL},
          version = {0.1.1},
          year = {2023}
}
```