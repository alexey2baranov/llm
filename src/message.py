import string


class Message():
    role: str
    content: str

    def __str__(self) -> str:
        return f'{{role: {self.role}, content: {self.content}}}'
