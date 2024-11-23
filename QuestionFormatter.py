from datetime import datetime
from tabulate import tabulate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from Const import *


class QuestionFormatter:

    # TXT

    @staticmethod
    def format_output_for_txt(output, content_type=None):
        return "\n\n".join([
            QuestionFormatter._format_txt_entry(q, content_type)
            for q in output[SECTION_QUESTIONS]
        ])

    @staticmethod
    def _format_txt_entry(question, content_type):
        entry_text = f"{LABEL_TASK}{COLON}{question[SECTION_ID]}\n\n"
        if content_type in [None, SECTION_QUESTIONS]:
            entry_text += QuestionFormatter._format_question_txt(question)
        if content_type in [None, SECTION_SOLUTIONS]:
            entry_text += QuestionFormatter._format_solution_txt(question)
        return entry_text.strip() + "\n\n\n"

    @staticmethod
    def _format_question_txt(question):
        content = f"{LABEL_QUESTION}{COLON}\n{question[SECTION_QUESTION_CONTENT][SECTION_QUESTION]}\n\n"
        additional_infos = question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_ADDITIONAL_INFOS)
        if additional_infos:
            infos_text = "\n".join([f"- {info}" for info in additional_infos])
            content += f"{LABEL_ADDITIONAL_INFOS}{COLON}\n{infos_text}\n\n"

        tables = question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_TABLES)
        if tables:
            for table in tables:
                content += f"{LABEL_TABLE}{COLON}{table[SECTION_TABLES_TITLE]}\n"
                content += QuestionFormatter.format_table_txt(table)

        content += f"{LABEL_EXAMPLE}{COLON}\n{question[SECTION_EXAMPLE]}\n\n"

        return content

    @staticmethod
    def _format_solution_txt(question):
        content = f"{LABEL_SOLUTION}{COLON}\n{question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION]}\n\n"

        additional_infos = question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_ADDITIONAL_INFOS)
        if additional_infos:
            infos_text = "\n".join([f"• {info}" for info in additional_infos])
            content += f"{LABEL_ADDITIONAL_SOLUTION_INFOS}{COLON}\n{infos_text}\n\n"

        steps = question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_STEP_BY_STEP)
        if steps:
            steps_text = "\n".join([f"{idx + 1}. {step}" for idx, step in enumerate(steps)])
            content += f"{LABEL_SOLUTION_STEP_BY_STEP}{COLON}\n{steps_text}\n\n"

        state_table = question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION_STATE_TRANSITION_TABLE]
        content += f"{LABEL_TABLE}{COLON}{state_table[SECTION_TABLES_TITLE]}\n"
        content += QuestionFormatter.format_table_txt(state_table)

        example_flow_table = question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]
        content += f"{LABEL_TABLE}{COLON}{example_flow_table[SECTION_TABLES_TITLE]}\n"
        content += QuestionFormatter.format_table_txt(example_flow_table)

        tables = question[SECTION_SOLUTION_CONTENT].get(SECTION_ADDITIONAL_SOLUTION_TABLES)
        if tables:
            for table in tables:
                content += f"{LABEL_TABLE}{COLON}{table[SECTION_TABLES_TITLE]}\n"
                content += QuestionFormatter.format_table_txt(table)

        return content

    @staticmethod
    def format_table_txt(table):
        headers = table[SECTION_TABLES_HEADERS]
        rows = table[SECTION_TABLES_ROWS]
        table_text = tabulate(rows, headers=headers, tablefmt="grid")
        return table_text + "\n\n"

    # PDF

    @staticmethod
    def format_output_for_pdf(output, content_type=None):
        doc_content = []
        styles = QuestionFormatter._get_pdf_styles()

        for question in output[SECTION_QUESTIONS]:
            doc_content.append(Paragraph(f"{LABEL_TASK}{COLON}{question[SECTION_ID]}", styles['heading_style']))
            if content_type in [None, SECTION_QUESTIONS]:
                doc_content.extend(QuestionFormatter._format_question_pdf(question, styles))
            if content_type in [None, SECTION_SOLUTIONS]:
                doc_content.extend(QuestionFormatter._format_solution_pdf(question, styles))
            doc_content.append(Spacer(1, 36))

        return doc_content

    @staticmethod
    def _get_pdf_styles():
        styles = getSampleStyleSheet()
        return {
            'heading_style': ParagraphStyle(name='HeadingStyle', parent=styles['Heading2'], fontSize=16, leading=20,
                                            spaceAfter=15),
            'label_style': ParagraphStyle(name='LabelStyle', parent=styles['Heading4'], fontSize=12, leading=14,
                                          spaceBefore=25),
            'content_style': ParagraphStyle(name='ContentStyle', parent=styles['BodyText'], fontSize=12, leading=14,
                                            spaceBefore=6, spaceAfter=6),
            'bullet_style': ParagraphStyle(name='BulletStyle', parent=styles['BodyText'], fontSize=12, leading=14,
                                           leftIndent=20, spaceBefore=4, spaceAfter=4),
            'step_style': ParagraphStyle(name='StepStyle', parent=styles['BodyText'], fontSize=12, leading=14,
                                         leftIndent=20, spaceBefore=4, spaceAfter=4)
        }

    @staticmethod
    def _format_question_pdf(question, styles):
        content = [
            Paragraph(f"{LABEL_QUESTION}{COLON}", styles['label_style']),
            Paragraph(question[SECTION_QUESTION_CONTENT][SECTION_QUESTION], styles['content_style'])
        ]
        additional_infos = question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_ADDITIONAL_INFOS)
        if additional_infos:
            content.append(Paragraph(f"{LABEL_ADDITIONAL_INFOS}{COLON}", styles['label_style']))
            for info in additional_infos:
                content.append(Paragraph(f"• {info}", styles['bullet_style']))

        tables = question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_TABLES)
        if tables:
            for table in tables:
                content.extend(QuestionFormatter._format_table_pdf(table, styles))

        content.append(Paragraph(f"{LABEL_EXAMPLE}{COLON}", styles['label_style']))
        content.append(Paragraph(question[SECTION_EXAMPLE], styles['content_style']))

        return content

    @staticmethod
    def _format_solution_pdf(question, styles):
        content = [
            Paragraph(f"{LABEL_SOLUTION}{COLON}", styles['label_style']),
            Paragraph(question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION], styles['content_style'])
        ]

        additional_infos = question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_ADDITIONAL_INFOS)
        if additional_infos:
            content.append(Paragraph(f"{LABEL_ADDITIONAL_SOLUTION_INFOS}{COLON}", styles['label_style']))
            for info in additional_infos:
                content.append(Paragraph(f"• {info}", styles['bullet_style']))

        steps = question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_STEP_BY_STEP)
        if steps:
            content.append(Paragraph(f"{LABEL_SOLUTION_STEP_BY_STEP}{COLON}", styles['label_style']))
            for idx, step in enumerate(steps):
                content.append(Paragraph(f"{idx + 1}. {step}", styles['step_style']))

        state_table = question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION_STATE_TRANSITION_TABLE]
        content.extend(QuestionFormatter._format_table_pdf(state_table, styles))

        example_flow_table = question[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]
        content.extend(QuestionFormatter._format_table_pdf(example_flow_table, styles))

        tables = question[SECTION_SOLUTION_CONTENT].get(SECTION_ADDITIONAL_SOLUTION_TABLES)
        if tables:
            for table in tables:
                content.extend(QuestionFormatter._format_table_pdf(table, styles))

        return content

    @staticmethod
    def _format_table_pdf(table, styles):
        content = [Paragraph(f"{LABEL_TABLE}{COLON}{table[SECTION_TABLES_TITLE]}", styles['label_style'])]
        data = [table[SECTION_TABLES_HEADERS]] + table[SECTION_TABLES_ROWS]
        table_obj = Table(data)
        table_obj.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6)
        ]))
        content.append(table_obj)
        content.append(Spacer(1, 10))

        return content

    # JSON

    @staticmethod
    def format_output_for_json(output, content_type=None):
        formatted_json = []

        for q in output[SECTION_QUESTIONS]:
            entry = {SECTION_ID: q[SECTION_ID]}

            if content_type in [None, SECTION_QUESTIONS]:
                entry.update({
                    SECTION_QUESTION: q[SECTION_QUESTION_CONTENT][SECTION_QUESTION],
                    SECTION_QUESTION_ADDITIONAL_INFOS: q[SECTION_QUESTION_CONTENT].get(
                        SECTION_QUESTION_ADDITIONAL_INFOS),
                    SECTION_QUESTION_TABLES: q[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_TABLES),
                    SECTION_EXAMPLE: q[SECTION_EXAMPLE]
                })

            if content_type in [None, SECTION_SOLUTIONS]:
                entry.update({
                    SECTION_SOLUTION: q[SECTION_SOLUTION_CONTENT][SECTION_SOLUTION],
                    SECTION_SOLUTION_ADDITIONAL_INFOS: q[SECTION_SOLUTION_CONTENT].get(
                        SECTION_SOLUTION_ADDITIONAL_INFOS),
                    SECTION_SOLUTION_STEP_BY_STEP: q[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_STEP_BY_STEP),
                    SECTION_SOLUTION_STATE_TRANSITION_TABLE: q[SECTION_SOLUTION_CONTENT][
                        SECTION_SOLUTION_STATE_TRANSITION_TABLE],
                    SECTION_SOLUTION_EXAMPLE_FLOW_TABLE: q[SECTION_SOLUTION_CONTENT][
                        SECTION_SOLUTION_EXAMPLE_FLOW_TABLE],
                    SECTION_ADDITIONAL_SOLUTION_TABLES: q[SECTION_SOLUTION_CONTENT].get(
                        SECTION_ADDITIONAL_SOLUTION_TABLES)
                })

            formatted_json.append(entry)

        return {SECTION_QUESTIONS: formatted_json}

    @staticmethod
    def clean_optional_fields(data):
        for question in data[SECTION_QUESTIONS]:

            if not question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_ADDITIONAL_INFOS):
                question[SECTION_QUESTION_CONTENT].pop(SECTION_QUESTION_ADDITIONAL_INFOS, None)

            if not question[SECTION_QUESTION_CONTENT].get(SECTION_QUESTION_TABLES):
                question[SECTION_QUESTION_CONTENT].pop(SECTION_QUESTION_TABLES, None)

            if not question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_ADDITIONAL_INFOS):
                question[SECTION_SOLUTION_CONTENT].pop(SECTION_SOLUTION_ADDITIONAL_INFOS, None)

            if not question[SECTION_SOLUTION_CONTENT].get(SECTION_SOLUTION_STEP_BY_STEP):
                question[SECTION_SOLUTION_CONTENT].pop(SECTION_SOLUTION_STEP_BY_STEP, None)

            if not question[SECTION_SOLUTION_CONTENT].get(SECTION_ADDITIONAL_SOLUTION_TABLES):
                question[SECTION_SOLUTION_CONTENT].pop(SECTION_ADDITIONAL_SOLUTION_TABLES, None)

        return data

    @staticmethod
    def format_filename(name, file_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{FILE_NAME_PREFIX}{UNDERSCORE}{name}{UNDERSCORE}{timestamp}.{file_type.lower()}"

    @staticmethod
    def assign_ids_to_questions(output):
        for idx, q in enumerate(output[SECTION_QUESTIONS]):
            q[SECTION_ID] = idx + 1
        return output
