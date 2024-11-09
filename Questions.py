from pydantic import BaseModel
from typing import List, Optional


class QuestionContent(BaseModel):
    question: str
    additional_infos: Optional[List[str]] = None


class SolutionContent(BaseModel):
    solution: str
    step_by_step_solution: Optional[List[str]] = None


class ExamQuestion(BaseModel):
    question_content: QuestionContent
    example: Optional[str] = None
    solution_content: SolutionContent


class ExamQuestions(BaseModel):
    questions: List[ExamQuestion]
