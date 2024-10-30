from pydantic import BaseModel


class ExamQuestion(BaseModel):
    question: str
    example: str
    answer: str
