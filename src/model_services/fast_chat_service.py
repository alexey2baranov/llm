import logging

from app.completions_input_dto import CompletionsInputDto
from model_services.model_service import ModelService
from transformers import pipeline


class FastChatService(ModelService):
    def init(self):
        self.pipeline = pipeline(
            "text2text-generation",
            model="lmsys/fastchat-t5-3b-v1.0",
        )

    def generate(self, params: CompletionsInputDto) -> list[dict]:
        assert self.pipeline.tokenizer is not None

        # prompt = self.pipeline.tokenizer.apply_chat_template(
        #     [{'role': item.role, 'content': item.content} for item in params.messages], tokenize=False,
        #     add_generation_prompt=True
        # )

        prompt = " ".join(
            [
                *[
                    message.content
                    if message.role == "system"
                    else f"### Human: {message.content}"
                    if message.role == "user"
                    else f"### Assistant: {message.content}"
                    for message in params.messages
                ],
                "### Assistant:",
            ]
        )

        assert isinstance(prompt, str)

        logging.debug(prompt)

        result = self.pipeline(
            prompt,
            max_new_tokens=params.max_tokens or 512,
            num_return_sequences=1,
            do_sample=True,
            temperature=params.temperature,
            top_p=params.top_p,
        )

        logging.debug(result)

        return result  # type: ignore
