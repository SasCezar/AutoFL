import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from hydra import initialize, compose

from api.run_analysis import RunAnalysis
from entity.analysis import Analysis
from entity.project import Project

app = FastAPI()


@app.post("/label/files")
async def label_files(analysis: Analysis):

    with initialize(version_base='1.3', config_path="../../config/"):
        overrides = []
        #overrides = [f'{key}={value}' for key, value in analysis.config.items()] if analysis.config else []
        cfg = compose(config_name="main.yaml", overrides=overrides)

    project = Project(name=analysis.name,
                      remote=analysis.remote,
                      dir_path=f'{cfg.data_path}/repository/{analysis.name}',
                      languages=analysis.languages)

    execution = RunAnalysis(cfg)

    annotations = execution.run(project)
    #exclude_keys = {'versions': {'files': {'__all__': {'content', 'identifiers'}}}}
    exclude_keys = {'versions': {'__all__': {'files'}}}
    result = {'result': jsonable_encoder(annotations.dict(exclude=exclude_keys))}
    return JSONResponse(content=result)


@app.get("/")
async def main():
    return {'Message': "Done"}
