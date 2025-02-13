from Const import TASK_GENERATION_TEMPERATURE, EXAMPLE_FLOW_TEMPERATURE, STATE_TRANSITION_TEMPERATURE, \
    SOLUTION_TEMPERATURE, SECTION_QUESTIONS
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from Questions import ExamQuestion, ExamQuestionsWithExamples, SolutionStateTransitionTable, \
    SolutionExampleFlowTable


def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_image = args.files_image
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

    if any([files_txt, files_image, files_pdf]):
        print("[INFO] Processing attached files...")
    else:
        print("[INFO] No additional files provided. Proceeding without external inputs.")

    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_image, files_pdf)

    print(f"[INFO] Processed {len(info_texts)} text files, {len(encoded_base64_data)} image files, and "
          f"{len(pdf_texts)} PDF files.")

    print("[INFO] Creating task generation message...")
    message_task = MessageBuilder.create_task_message(
        num_questions, difficulty, info_texts, encoded_base64_data, pdf_texts, incorrect_task)
    print("[INFO] Task generation message created successfully.")

    print("[INFO] Sending request to OpenAI API for task generation...")
    generated_tasks = OpenAIClient.send_request(message_task, TASK_GENERATION_TEMPERATURE, ExamQuestionsWithExamples)
    print(f"[INFO] Received {len(generated_tasks[SECTION_QUESTIONS])} generated task(s).")

    complete_tasks = []
    total_tasks = len(generated_tasks[SECTION_QUESTIONS])

    for index, question_content in enumerate(generated_tasks[SECTION_QUESTIONS], start=1):
        print(f"[INFO] Creating question {index} of {total_tasks}...")
        print(f"[INFO] Creating state transition table for question {index}...")
        state_transition_table_message = MessageBuilder.create_state_transition_table_message(question_content)

        state_transition_table_content = OpenAIClient.send_request(
            state_transition_table_message, STATE_TRANSITION_TEMPERATURE, SolutionStateTransitionTable)
        print(f"[INFO] State transition table created successfully for question {index}.")
        print(f"[INFO] Creating example flow table for question {index}...")
        example_flow_table_message = MessageBuilder.create_example_flow_table_message(
            question_content, state_transition_table_content)

        example_flow_table_content = OpenAIClient.send_request(
            example_flow_table_message, EXAMPLE_FLOW_TEMPERATURE, SolutionExampleFlowTable)
        print(f"[INFO] Example flow table created successfully for question {index}.")
        print(f"[INFO] Generating complete solution for question {index}...")
        solution_message = MessageBuilder.create_solution_message(question_content, state_transition_table_content,
                                                                  example_flow_table_content)
        complete_task = OpenAIClient.send_request(solution_message, SOLUTION_TEMPERATURE, ExamQuestion)
        print(f"[INFO] Complete solution generated successfully for question {index}.")
        complete_tasks.append(complete_task)
        print(f"[INFO] Question {index} of {total_tasks} processed")

    print("[INFO] All questions processed successfully.")
    result_final = {"questions": complete_tasks}
    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate)
    print("[INFO] Output saved successfully.")
    print("[INFO] Process completed successfully.")


if __name__ == "__main__":
    main()
