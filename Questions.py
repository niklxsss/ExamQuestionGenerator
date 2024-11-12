from pydantic import BaseModel
from typing import List, Optional


class TableContent(BaseModel):
    title: str
    headers: List[str]
    rows: List[List[str]]


class QuestionContent(BaseModel):
    question: str
    optional_question_additional_infos: Optional[List[str]] = None
    optional_question_tables: Optional[List[TableContent]]
    # // relevant für fehlerhafte turingmaschinen


class SolutionContent(BaseModel):
    solution: str
    optional_solution_additional_infos: Optional[List[str]] = None
    optional_solution_step_by_step: Optional[List[str]] = None
    optional_solution_tables: Optional[List[TableContent]]


class ExamQuestion(BaseModel):
    question_content: QuestionContent
    optional_example: Optional[str] = None
    solution_content: SolutionContent


class ExamQuestions(BaseModel):
    questions: List[ExamQuestion]
