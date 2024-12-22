import json

from Const import VALIDATION_TEMPERATURE, SECTION_QUESTIONS, SECTION_SOLUTION_STATE_TRANSITION_TABLE, \
    SECTION_SOLUTION_EXAMPLE_FLOW_TABLE, SECTION_EXAMPLE, SECTION_QUESTION_CONTENT
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from Questions import ExamQuestion, ExamQuestionWithExamples, SolutionStateTransitionTable, \
    SolutionExampleFlowTable, ExamQuestionWithExampleAndTables


def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_image
    files_txt = args.files_txt
    files_pdf = args.files_pdf
    separate = args.separate
    output_format = args.output
    difficulty = args.difficulty
    incorrect_task = args.incorrect_task

    print(f"[INFO] Number of questions to generate: {num_questions}")
    print(f"[INFO] Difficulty level: {difficulty}")
    print(f"[INFO] incorrect task: {incorrect_task}")
    print(f"[INFO] Output format: {output_format}")

    if any([files_txt, files_images, files_pdf]):
        print("[INFO] Processing attached files...")
    else:
        print("[INFO] No additional files provided. Proceeding without external inputs.")

    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_images, files_pdf)

    print(f"[INFO] Processed {len(info_texts)} text files, {len(encoded_base64_data)} image files, and "
          f"{len(pdf_texts)} PDF files.")

    print("[INFO] Creating task generation message...")
    message_task = MessageBuilder.create_task_message(
        num_questions, difficulty, info_texts, encoded_base64_data, pdf_texts, incorrect_task)
    print("[INFO] Task generation message created successfully.")

    print("[INFO] Sending request to OpenAI API for task generation...")
    generated_tasks = OpenAIClient.send_request(message_task, VALIDATION_TEMPERATURE, ExamQuestionWithExamples)
    print(f"[INFO] Received {len(generated_tasks[SECTION_QUESTIONS])} generated task(s).")

    complete_tasks = []
    total_tasks = len(generated_tasks[SECTION_QUESTIONS])
    for index, question_content in enumerate(generated_tasks[SECTION_QUESTIONS], start=1):
        print(f"[INFO] Creating question {index} of {total_tasks}...")

        print(f"[INFO] Creating state transition table for question {index}...")
        state_transition_table_message = MessageBuilder.create_state_transition_table_message(question_content)

        state_transition_table_content = OpenAIClient.send_request(
            state_transition_table_message, VALIDATION_TEMPERATURE, SolutionStateTransitionTable)
        print(f"[INFO] State transition table created successfully for question {index}.")

        print(f"[INFO] Starting validation process for state transition table of question {index}...")
        state_transition_table_validation_message = MessageBuilder.create_validation_state_transition_table_message(
            str(question_content) + str(state_transition_table_content))

        state_transition_table_content_validated = OpenAIClient.send_request(
            state_transition_table_validation_message, VALIDATION_TEMPERATURE, SolutionStateTransitionTable)
        print(f"[INFO] State transition table validated and corrected for question {index}.")

        print(f"[INFO] Creating example flow table for question {index}...")
        example_flow_table_message = MessageBuilder.create_example_flow_table_message(
            question_content, state_transition_table_content)

        example_flow_table_content = OpenAIClient.send_request(
            example_flow_table_message, VALIDATION_TEMPERATURE, SolutionExampleFlowTable)
        print(f"[INFO] Example flow table created successfully for question {index}.")

        print(f"[INFO] Starting validation process for example flow table of question {index}...")
        example_flow_table_validation_message = MessageBuilder.create_validation_example_flow_table_message(
            str(question_content) + str(state_transition_table_content_validated) + str(example_flow_table_content))

        example_flow_table_content_validated = OpenAIClient.send_request(
            example_flow_table_validation_message, VALIDATION_TEMPERATURE, SolutionExampleFlowTable)

        # table_validation_message = MessageBuilder.create_validation_message(question_content, state_transition_table_content, example_flow_table_content)
        # validated_task_and_tables = OpenAIClient.send_request(
        #     table_validation_message, VALIDATION_TEMPERATURE, ExamQuestionWithExampleAndTables)
        print(f"[INFO] Example flow table validated and corrected for question {index}.")

        print(f"[INFO] Generating complete solution for question {index}...")
        # solution_message = MessageBuilder.create_solution_message(
        #     str(question_content) + str(state_transition_table_content_validated) +
        #     str(example_flow_table_content_validated))

        exam_question = ExamQuestionWithExampleAndTables(
            question_content=question_content[SECTION_QUESTION_CONTENT],
            example=question_content[SECTION_EXAMPLE],
            solution_state_transition_table=state_transition_table_content_validated[SECTION_SOLUTION_STATE_TRANSITION_TABLE],
            solution_example_flow_table=example_flow_table_content_validated[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]
        )
        solution_message = MessageBuilder.create_solution_message(exam_question)

        complete_task = OpenAIClient.send_request(
            solution_message, VALIDATION_TEMPERATURE, ExamQuestion)
        print(f"[INFO] Complete solution generated successfully for question {index}.")

        complete_tasks.append(complete_task)

        # #Testing
        # compare_tables_and_print_differences(
        #     "Zustandsübergangstabelle",
        #     state_transition_table_content["solution_state_transition_table"],
        #     validated_task_and_tables["solution_state_transition_table"]
        # )
        #
        # compare_tables_and_print_differences(
        #     "Beispielablauftabelle",
        #     example_flow_table_content["solution_example_flow_table"],
        #     validated_task_and_tables["solution_example_flow_table"]
        # )

        print(f"[INFO] Question {index} of {total_tasks} processed and validated.")

    print("[INFO] All questions processed and validated successfully.")

    result_final = {"questions": complete_tasks}

    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate)
    print("[INFO] Output saved successfully.")

    print("[INFO] Process completed successfully.")


def compare_tables_and_print_differences(table_name, original_table, validated_table):
    """
    Vergleicht zwei Tabellen und gibt Unterschiede aus.

    :param table_name: Name der Tabelle (z.B. "Zustandsübergangstabelle" oder "Beispielablauftabelle").
    :param original_table: Originale Tabelle vor der Validierung.
    :param validated_table: Validierte Tabelle nach der Korrektur.
    """
    if original_table == validated_table:
        print(f"No changes detected in {table_name}. Validation process may not be effective.")
    else:
        print(f"Differences found in {table_name}. Validation made adjustments.")

    print(f"--output, {table_name} vor Korrektur----------------------------------------------------------------------")
    print(json.dumps(original_table))
    print(f"--output, {table_name} nach validation prompt-------------------------------------------------------------")
    print(json.dumps(validated_table))


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2

# create_exam_questions --output TXT --files_pdf gie-informatik_uebung_08.pdf --num_questions 5

# create_exam_questions --output PDF --files_images AblaufGrafik.png --files_txt Unit05.txt --files_pdf gie-informatik_uebung_08.pdf --num_questions 15

# JSON compare:
# https://jsonviewer.stack.hu/
# https://jsondiff.com/