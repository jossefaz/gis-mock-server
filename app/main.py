from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.configuration.configuration_controller import get_mock_config
from app.controllers.metadata.metadata_controller import registry

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/configuration")
def read_root():
    return get_mock_config()


@app.get("/MetaData/getMetaData/{metadata_source}")
def read_item(metadata_source: str):
    return registry[metadata_source]()
