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


class SolutionContent(BaseModel):
    solution: str
    optional_solution_additional_infos: Optional[List[str]] = None
    optional_solution_step_by_step: Optional[List[str]] = None
    solution_state_transition_table: TableContent
    solution_example_flow_table: TableContent
    optional_additional_solution_tables: Optional[List[TableContent]] = None


class ExamQuestion(BaseModel):
    question_content: QuestionContent
    example: str
    solution_content: SolutionContent


class ExamQuestions(BaseModel):
    questions: List[ExamQuestion]
