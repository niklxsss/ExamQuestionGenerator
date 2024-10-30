import argparse

from Const import TXT_FORMAT, PDF_FORMAT, JSON_FORMAT


class InputArgumentParser:

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Create Exam Questions")
        parser.add_argument('--num_questions', type=int, default=1, help="Number of questions to generate")
        parser.add_argument('--files_images', type=str, nargs='+', default=[], help="Paths to image files")
        parser.add_argument('--files_txt', type=str, nargs='+', default=[], help="Paths to text files")
        parser.add_argument('--files_pdf', type=str, nargs='+', default=[], help="Paths to pdf files")
        parser.add_argument('--separate_answers', action='store_true', help="Save answers in a separate file")
        parser.add_argument('--output', type=str, required=True, choices=[TXT_FORMAT, PDF_FORMAT, JSON_FORMAT],
                            help="Output format for questions")
        return parser.parse_args()
