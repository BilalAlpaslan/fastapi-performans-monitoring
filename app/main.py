from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
import time
import uvicorn

app = FastAPI()


apm_config = {
    'SERVICE_NAME': 'FastAPI-ElasticAPM',
    'SERVER_URL': 'http://localhost:8200',
    'ENVIRONMENT': 'dev',
    'GLOBAL_LABELS': 'platform=Platform, application=Application'
}
apm = make_apm_client(apm_config)


app.add_middleware(
    ElasticAPM,
    client=apm,
)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/point1")
def point1():
    time.sleep(1)
    return {"message": "Hello World 1"}


@app.get("/point2")
def point2():
    time.sleep(2)
    return {"message": "Hello World 2"}


@app.get("/point3")
def point3():
    time.sleep(3)
    return {"message": "Hello World 3"}


if __name__ == '__main__':
    uvicorn.run(app)
