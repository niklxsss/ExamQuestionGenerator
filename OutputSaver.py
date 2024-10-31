import json

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from QuestionFormatter import *

class OutputSaver:

    @staticmethod
    def save_output_to_json(data, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def save_output_to_txt(output, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(output)

    @staticmethod
    def save_output_to_pdf(formatted_content, filename):
        doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
        doc.build(formatted_content)

    @staticmethod
    def save_output_to_file(output, file_type, separate_answers=False):
        if isinstance(output, str):
            output = json.loads(output)

        output = QuestionFormatter.assign_ids_to_questions(output)

        if separate_answers:
            answers_filename = QuestionFormatter.format_filename(FILE_NAME_ANSWERS, file_type)
            question_filename = QuestionFormatter.format_filename(FILE_NAME_QUESTIONS, file_type)

            if file_type.upper() == JSON_FORMAT:
                OutputSaver.save_output_to_json(QuestionFormatter.format_output_for_json(
                    output, SECTION_QUESTIONS), question_filename)
                OutputSaver.save_output_to_json(QuestionFormatter.format_output_for_json(
                    output, SECTION_ANSWERS), answers_filename)
            elif file_type.upper() == TXT_FORMAT:
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(
                    output, SECTION_QUESTIONS), question_filename)
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(
                    output, SECTION_ANSWERS), answers_filename)
            elif file_type.upper() == PDF_FORMAT:
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(
                    output, SECTION_QUESTIONS), question_filename)
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(
                    output, SECTION_ANSWERS), answers_filename)

            print(f"Output saved to {question_filename} and {answers_filename}")
        else:
            filename = QuestionFormatter.format_filename(FILE_NAME_QUESTIONS_AND_ANSWERS, file_type)

            if file_type.upper() == JSON_FORMAT:
                OutputSaver.save_output_to_json(output, filename)
            elif file_type.upper() == TXT_FORMAT:
                OutputSaver.save_output_to_txt(QuestionFormatter.format_output_for_txt(output), filename)
            elif file_type.upper() == PDF_FORMAT:
                OutputSaver.save_output_to_pdf(QuestionFormatter.format_output_for_pdf(output), filename)

            print(f"Output saved to {filename}")

