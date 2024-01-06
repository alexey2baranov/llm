from contextlib import asynccontextmanager

from app.completions_input_dto import CompletionsInputDto
from app.completions_output_dto import CompletionsOutputDto
from di_container.container import container
from fastapi import FastAPI
from openai import OpenAI
from transformers import AutoModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    container.model_service.init()
    yield
    container.model_service.release()


app = FastAPI(lifespan=lifespan)


@app.post("/completions", response_model=CompletionsOutputDto)
async def generate(body: CompletionsInputDto):
    return container.model_service.generate(body)


AutoModel()
OpenAI()
