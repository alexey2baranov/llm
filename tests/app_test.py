import logging
import unittest

from fastapi.testclient import TestClient
from server.test_model_service import TestModelService

from ..src.app import app
from ..src.di_container.container import container
from ..src.medel_services.fast_chat_service import FastChatService


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)
        cls.client = TestClient(app)
        container.model_service = TestModelService()
        container.model_service.init()

    def test_generate(self):
        response = self.client.post(
            "/completions",
            json={
                "model": "lmsys/fastchat-t5-3b-v1.0",
                "messages": [
                    {
                        "role": "system",
                        "content": "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.",
                    },
                    {
                        "role": "user",
                        "content": "What are the key differences between renewable and non-renewable energy sources?",
                    },
                ],
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.json()[0]["generated_text"], r"renewable|generated text")
