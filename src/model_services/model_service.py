from abc import ABC, abstractmethod

# from .completions_input_dto import CompletionsInputDto
from app.completions_input_dto import CompletionsInputDto
from transformers import Pipeline


class ModelService(ABC):
    pipeline: Pipeline

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def release(self):
        pass

    @abstractmethod
    def generate(self, params: CompletionsInputDto) -> list[dict]:
        pass
