import argparse

from Const import *


class InputArgumentParser:

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Create Exam Questions")
        parser.add_argument('--num_questions', type=int, default=1, help="Number of questions to generate")
        parser.add_argument('--files_images', type=str, nargs='+', default=[], help="Paths to image files")
        parser.add_argument('--files_txt', type=str, nargs='+', default=[], help="Paths to text files")
        parser.add_argument('--files_pdf', type=str, nargs='+', default=[], help="Paths to pdf files")
        parser.add_argument('--separate_answers', action='store_true', help="Save answers in a separate file")
        parser.add_argument('--difficulty', type=str, choices=[DIFFICULTY_EASY, DIFFICULTY_MEDIUM,
                                                               DIFFICULTY_CHALLENGING,
                                                               # DIFFICULTY_ADVANCED, DIFFICULTY_EXTREME
                                                               ],
                            default=DIFFICULTY_MEDIUM, help="Difficulty level of the questions")
        parser.add_argument('--task_type', type=str, choices=[TASK_TYPE_INCORRECT_TASK],
                            help="")
        parser.add_argument('--output', type=str, required=True, choices=[TXT_FORMAT, PDF_FORMAT, JSON_FORMAT],
                            help="Output format for questions")
        return parser.parse_args()
