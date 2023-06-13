from pathlib import Path


class File:
    def __init__(self, path: Path | str):
        if isinstance(path, str):
            path = Path(path)
        self.path = path
        self.content = self._load_content()
        self.language = path.suffix

    def _load_content(self) -> str:
        with open(self.path, 'rt') as inf:
            content = ' '.join(inf.readlines())

        return content
