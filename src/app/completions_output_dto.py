from typing import List

from pydantic import BaseModel


class MessageDto(BaseModel):
    role: str
    content: str


class ChoiceDto(BaseModel):
    message: MessageDto
    finish_reason: str
    index: int


class CompletionsOutputDto(BaseModel):
    choices: List[ChoiceDto]
