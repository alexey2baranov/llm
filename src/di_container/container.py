import logging

from model_services.fast_chat_service import FastChatService
from model_services.model_service import ModelService


class Container:
    model_service: ModelService

    def __init__(self):
        self.env = {
            # 'model_name': 'lmsys/fastchat-t5-3b-v1.0'
            # 'model_name': 'HuggingFaceH4/zephyr-7b-alpha'
            # 'model_name': "gpt2"
            # 'model_name': "deberain/gpt-neo-125M-fine-tuned-on-ChatGPT-tweets"
            # 'model_name': 'rwl4/gpt2-medium-chat'
            # 'model_name': 'distilgpt2'
            # 'model_name': 'lmsys/fastchat-t5-3b-v1.0'
        }


container = Container()

# configuration

logging.basicConfig(level=logging.DEBUG)

container.model_service = FastChatService()
