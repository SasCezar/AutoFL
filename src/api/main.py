from typing import Union, List

from fastapi import FastAPI

from entity.project import Project

app = FastAPI()


@app.get("/analyze")
async def analyze(name: str, remote: str, languages: Union[str, List[str]], dir_path: str='.'):
    project = Project()