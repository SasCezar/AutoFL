import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from hydra import initialize, compose
from hydra.utils import instantiate
from omegaconf import OmegaConf
from sqlalchemy import create_engine

from api.run_analysis import RunAnalysis
from dataloader.postgres_dataloader import PostgresProjectLoader
from entity.analysis import Analysis
from entity.project import Project

app = FastAPI()


@app.post("/label/files")
async def label_files(analysis: Analysis):

    with initialize(version_base='1.3', config_path="../../config/"):
        overrides = []
        #overrides = [f'{key}={value}' for key, value in analysis.config.items()] if analysis.config else []
        cfg = compose(config_name="main.yaml", overrides=overrides)
    annot_cfg = OmegaConf.to_container(cfg.annotator, resolve=True) if cfg else {}
    project = Project(name=analysis.name,
                      remote=analysis.remote,
                      dir_path=f'{cfg.data_path}/repository/{analysis.name}',
                      languages=analysis.languages)

    dataloader: PostgresProjectLoader | None = None
    if cfg.dataloader is not None:
        dataloader: PostgresProjectLoader = instantiate(cfg.dataloader)

    annotations = None
    if dataloader:
        annotations = dataloader.load_single(project.name, annot_cfg)

    if not annotations:
        execution = RunAnalysis(cfg)

        annotations = execution.run(project)
    #exclude_keys = {'versions': {'__all__': {'files'}}}
    #result = {'result': jsonable_encoder(annotations.dict(exclude=exclude_keys))}
    result = {'result': jsonable_encoder(annotations.dict())}
    return JSONResponse(content=result)


@app.get("/")
async def main():
    return {'Message': "Done"}
