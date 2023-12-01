from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from hydra import initialize, compose
from hydra.utils import instantiate
from omegaconf import OmegaConf

from api.run_analysis import RunAnalysis
from dataloader.postgres_dataloader import PostgresProjectLoader
from entity.analysis import Analysis
from entity.project import Project
from writer.postgres import PostgresWriter

app = FastAPI()


@app.post("/label/files")
async def label_files(analysis: Analysis):

    with initialize(version_base='1.3', config_path="../../config/"):
        overrides = []
        #overrides = [f'{key}={value}' for key, value in analysis.config.items()] if analysis.config else []
        cfg = compose(config_name="main.yaml")#, overrides=overrides)

    print(cfg)
    annot_cfg = OmegaConf.to_container(cfg.annotator, resolve=True)
    print(annot_cfg)
    project = Project(name=analysis.name,
                      remote=analysis.remote,
                      dir_path=f'{cfg.data_path}/repository/{analysis.name}',
                      languages=analysis.languages,
                      cfg=annot_cfg)

    dataloader: PostgresProjectLoader | None = None
    if cfg.dataloader is not None:
        dataloader: PostgresProjectLoader = instantiate(cfg.dataloader)

    writer: PostgresWriter | None = None
    if cfg.writer is not None:
        writer: PostgresWriter = instantiate(cfg.writer)

    cached = False
    try:
        if dataloader:
            annotations = dataloader.load_single(project.name, annot_cfg)
            cached = True
    except:
        print("Error loading project from database")

    if not cached:
        execution = RunAnalysis(cfg)
        annotations = execution.run(project)

    annotations.cfg = annot_cfg
    if writer and not cached:
        writer.write(annotations)

    result = {'result': jsonable_encoder(annotations.model_dump())}
    return JSONResponse(content=result)


@app.get("/")
async def main():
    return {'Message': "Done"}
