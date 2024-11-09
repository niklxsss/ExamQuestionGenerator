import json

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from QuestionFormatter import *


class OutputSaver:

    @staticmethod
    def save_output_to_json(output, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(output, file, ensure_ascii=False, indent=4)

    @staticmethod
    def save_output_to_txt(output, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(output)

    @staticmethod
    def save_output_to_pdf(output, filename):
        doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
        doc.build(output)

    @staticmethod
    def save_output_to_file(result, file_type, separate_answers=False):
        if isinstance(result, str):
            result = json.loads(result)

        output = QuestionFormatter.clean_optional_fields(result)
        output = QuestionFormatter.assign_ids_to_questions(output)

        if separate_answers:
            question_filename = QuestionFormatter.format_filename(FILE_NAME_QUESTIONS, file_type)
            solutions_filename = QuestionFormatter.format_filename(FILE_NAME_SOLUTIONS, file_type)

            if file_type.upper() == JSON_FORMAT:
                OutputSaver.save_output_to_json(QuestionFormatter.format_output_for_json(output, SECTION_QUESTIONS),
                                                question_filename)
                OutputSaver.save_output_to_json(QuestionFormatter.format_output_for_json(output, SECTION_SOLUTIONS),
                                                solutions_filename)

            elif file_type.upper() == TXT_FORMAT:
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(output, SECTION_QUESTIONS),
                                               question_filename)
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(output, SECTION_SOLUTIONS),
                                               solutions_filename)

            elif file_type.upper() == PDF_FORMAT:
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(output, SECTION_QUESTIONS),
                                               question_filename)
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(output, SECTION_SOLUTIONS),
                                               solutions_filename)

            print(f"Output saved to {question_filename} and {solutions_filename}")
        else:
            filename = QuestionFormatter.format_filename(FILE_NAME_QUESTIONS_AND_SOLUTIONS, file_type)

            if file_type.upper() == JSON_FORMAT:
                OutputSaver.save_output_to_json(output, filename)
            elif file_type.upper() == TXT_FORMAT:
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(output), filename)
            elif file_type.upper() == PDF_FORMAT:
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(output), filename)
            print(f"Output saved to {filename}")
