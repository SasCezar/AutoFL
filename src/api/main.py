from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.analysis import Analysis
from entity.project import ProjectBuilder

app = FastAPI()


@app.post("/label/files")
async def label_files(analysis: Analysis):
    project = ProjectBuilder().build('Waikato|weka-3.8', '/home/sasce/PycharmProjects/AutoFL/test/resources/repository',
                                     ['java'], 'https://github.com/Waikato/weka-3.8')

    analysis.project = project
    exclude_keys = {'project': {'files': {'__all__': {'content', 'identifiers'}}}}
    analysis = {'Key': 'Value', 'BodyDICT': analysis.json(exclude=exclude_keys)}
    return JSONResponse(content=analysis)


@app.get("/")
async def main():
    return {'Message': "Done"}

