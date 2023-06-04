from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api.analysis import Analysis

app = FastAPI()


@app.post("/label/files")
async def label_files(analysis: Analysis):
    analysis = {'Key': 'Value', 'Body': analysis}
    return JSONResponse(content=analysis)


@app.get("/")
async def main():
    return {'Message': "Done"}

