from typing import Union, List

from fastapi import FastAPI

app = FastAPI()


@app.get("/label/files")
async def label_files(name: str, remote: str, languages: Union[str, List[str]], *args, **kwargs):
    labelled_files = []
    return labelled_files


@app.get("/")
async def main():
    return {'Message': "Done"}

