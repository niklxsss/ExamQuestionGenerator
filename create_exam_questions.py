from Const import TASK_GENERATION_TEMPERATURE, ADDITIONAL_TASK_GENERATION_TEMPERATURE, VALIDATION_TEMPERATURE
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from Questions import ExamQuestion, ExamQuestionWithExamples, TableContent, SolutionStateTransitionTable, \
    SolutionExampleFlowTable


def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_images
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
    print(
        f"[INFO] Processed {len(info_texts)} text files, {len(encoded_base64_data)} image files, and {len(pdf_texts)} PDF files.")

    # Build initial task message
    print("[INFO] Creating task generation message...")
    message_task = MessageBuilder.create_task_message(
        num_questions, difficulty, info_texts, encoded_base64_data, pdf_texts)
    print("[INFO] Task generation message created successfully.")

    # Generate initial tasks
    print("[INFO] Sending request to OpenAI API for task generation...")
    generated_tasks = OpenAIClient.send_request(message_task, TASK_GENERATION_TEMPERATURE, ExamQuestionWithExamples)
    print(f"[INFO] Received {len(generated_tasks['questions'])} generated task(s).")

    complete_tasks = []
    total_tasks = len(generated_tasks["questions"])
    for index, question_content in enumerate(generated_tasks["questions"], start=1):
        print(f"[INFO] Validating question {index} of {total_tasks}...")

        # Print the initial question content for debugging
        # print(f"[DEBUG] Question content: {question_content}")

        # Generate state transition table
        print(f"[INFO] Creating state transition table for question {index}...")
        state_transition_table_message = MessageBuilder.create_state_transition_table_message(
            str(question_content))
        state_transition_table_content = OpenAIClient.send_request(
            state_transition_table_message, ADDITIONAL_TASK_GENERATION_TEMPERATURE, SolutionStateTransitionTable)
        print(f"[INFO] State transition table created successfully for question {index}.")

        # Generate example flow table
        print(f"[INFO] Creating example flow table for question {index}...")
        example_flow_table_message = MessageBuilder.create_example_flow_table_message(
            str(question_content) + str(state_transition_table_content))
        example_flow_table_content = OpenAIClient.send_request(
            example_flow_table_message, ADDITIONAL_TASK_GENERATION_TEMPERATURE, SolutionExampleFlowTable)
        print(f"[INFO] Example flow table created successfully for question {index}.")

        # Generate complete solution
        print(f"[INFO] Generating complete solution for question {index}...")
        solution_message = MessageBuilder.create_solution_message(
            str(question_content) + str(state_transition_table_content) + str(example_flow_table_content))
        complete_task = OpenAIClient.send_request(
            solution_message, ADDITIONAL_TASK_GENERATION_TEMPERATURE, ExamQuestion)
        print(f"[INFO] Complete solution generated successfully for question {index}.")

        # noch prints einfügen
        # validation_message = MessageBuilder.create_validation_message(str(complete_task))
        # complete_validated_task = OpenAIClient.send_request(
        #     validation_message, VALIDATION_TEMPERATURE, ExamQuestion)
        # complete_tasks.append(complete_validated_task)

        complete_tasks.append(complete_task)
        print(f"[INFO] Question {index} of {total_tasks} processed and validated.")

    print("[INFO] All questions processed and validated successfully.")

    result_final = {"questions": complete_tasks}
    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate)
    # OutputSaver.save_output_to_file(result, output_format, separate)
    print("[INFO] Output saved successfully.")

    print("[INFO] Process completed successfully.")

    # if result == result_final:
    #     print("No changes detected. Validation process may not be effective.")
    # else:
    #     print("Differences found. Validation made adjustments.")

    # print("--output, nach erstem durchlauf-----------------------------------------------------------")
    # # print(result)
    # print("--output nach validation prompt--------------------------------------------------------------------")
    print(result_final)


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