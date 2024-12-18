from pydantic import BaseModel
from typing import List, Optional

# Stand, erste verwendung einer Strukur mit Tabellen

from pydantic import BaseModel
from typing import List, Optional


class QuestionContent(BaseModel):
    question: str
    additional_infos: Optional[List[str]] = None


class TableContent(BaseModel):
    title: str
    headers: List[str]
    rows: List[List[str]]


class SolutionContent(BaseModel):
    solution: str
    additional_solution_infos: Optional[List[str]] = None
    step_by_step_solution: Optional[List[str]] = None
    tables: Optional[List[TableContent]]


class ExamQuestion(BaseModel):
    question_content: QuestionContent
    example: Optional[str] = None
    solution_content: SolutionContent


class ExamQuestions(BaseModel):
    questions: List[ExamQuestion]
