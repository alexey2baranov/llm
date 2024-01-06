from typing import List, Optional

from pydantic import BaseModel


class MessageDto(BaseModel):
    role: str
    content: str


class CompletionsInputDto(BaseModel):
    model: Optional[str] = None
    messages: List[MessageDto]
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    max_tokens: Optional[float] = None
    frequency_penalty: Optional[float] = None
