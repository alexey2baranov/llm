import logging

from server.completions_input_dto import CompletionsInputDto
from server.message import Message
from server.model_service import ModelService
from transformers import pipeline


class TestModelService(ModelService):
    def init(self):
        logging.debug("init model")
        pass

    def generate(self, params: CompletionsInputDto) -> list[dict]:
        result = [{"generated_text": "generated text 1"}, {"generated_text": "generated text 2"}]
        logging.debug(result)
        return result
