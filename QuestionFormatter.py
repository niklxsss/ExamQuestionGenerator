from datetime import datetime

from Const import *


class QuestionFormatter:
    @staticmethod
    def format_output_for_txt(output, content_type=None):
        if content_type == SECTION_QUESTIONS:
            return "\n\n".join([
                f"Aufgabe: {q[SECTION_ID]}\n"
                f"Question: {q[SECTION_QUESTION]}\n"
                f"Example: {q[SECTION_EXAMPLE]}"
                for q in output[SECTION_QUESTIONS]
            ])
        elif content_type == SECTION_ANSWERS:
            return "\n\n".join([
                f"Aufgabe: {q[SECTION_ID]}\n"
                f"Answer: {q[SECTION_ANSWER]}"
                for q in output[SECTION_QUESTIONS]
            ])

        return "\n\n".join([
            f"Aufgabe: {q[SECTION_ID]}\n"
            f"Question: {q[SECTION_QUESTION]}\n"
            f"Example: {q[SECTION_EXAMPLE]}\n"
            f"Answer: {q[SECTION_ANSWER]}"
            for q in output[SECTION_QUESTIONS]
        ])

    @staticmethod
    def format_output_for_pdf(output, content_type=None):
        return QuestionFormatter.format_output_for_txt(output, content_type)

    @staticmethod
    def format_output_for_json(output, content_type=None):
        if content_type == SECTION_QUESTIONS:
            questions = [
                {
                    SECTION_ID: q[SECTION_ID],
                    SECTION_QUESTION: q[SECTION_QUESTION],
                    SECTION_EXAMPLE: q[SECTION_EXAMPLE]
                }
                for q in output[SECTION_QUESTIONS]
            ]
            return {SECTION_QUESTIONS: questions}

        elif content_type == SECTION_ANSWERS:
            answers = [
                {
                    SECTION_ID: q[SECTION_ID],
                    SECTION_ANSWER: q[SECTION_ANSWER]
                }
                for q in output[SECTION_QUESTIONS]
            ]
            return {SECTION_ANSWERS: answers}

        return {SECTION_QUESTIONS: output}

    @staticmethod
    def format_filename(name, file_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{FILE_NAME_PREFIX}{UNDERSCORE}{name}{UNDERSCORE}{timestamp}.{file_type.lower()}"

    @staticmethod
    def assign_ids_to_questions(output):
        for idx, q in enumerate(output[SECTION_QUESTIONS]):
            output[SECTION_QUESTIONS][idx] = {
                SECTION_ID: idx + 1,
                SECTION_QUESTION: q[SECTION_QUESTION],
                SECTION_EXAMPLE: q[SECTION_EXAMPLE],
                SECTION_ANSWER: q[SECTION_ANSWER]
            }
        return output
