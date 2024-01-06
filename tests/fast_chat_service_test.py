import logging
import unittest
from email import message

from fastapi.testclient import TestClient
from server.completions_input_dto import CompletionsInputDto, MessageDto

from ..src.medel_services.fast_chat_service import FastChatService
from ..src.message import Message


class TestFastChatService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)
        cls.model_service = FastChatService()
        cls.model_service.init()

    def test_generate(self):
        messages = [
            MessageDto(
                role="system",
                content="A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions",
            ),
            MessageDto(
                role="user", content="What are the key differences between renewable and non-renewable energy sources?"
            ),
        ]
        result = self.model_service.generate(CompletionsInputDto(messages=messages, temperature=0.7))

        # chat.append(ChatItem('assistant', generated[0]["generated_text"]))
        # chat.append(ChatItem(
        #     'user', 'Which type will be more popular in the next 10 years. Give reasons for your answer.'))

        # generated = self.model_service.generate(chat)
        # logging.info(generated)

        # self.assertEqual(response.status_code, 200)
        # self.assertRegex(response.json()[0]["generated_text"], r'You\s+are')
