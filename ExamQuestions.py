from pydantic import BaseModel
from typing import List
from ExamQuestion import ExamQuestion


class ExamQuestions(BaseModel):
    questions: List[ExamQuestion]
