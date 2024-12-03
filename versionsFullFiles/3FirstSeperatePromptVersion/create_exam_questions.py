import time
from asyncio import wait

from Const import TEMPERATURE, VALIDATION_TEMPERATURE
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from PromptBuilder import PromptBuilder
from Questions import ExamQuestion, ExamQuestions, ExamQuestionWithExample, ExamQuestionWithExamples, TableContent, \
    SolutionStateTransitionTable, SolutionExampleFlowTable
from SplittedRequests import SplittedRequests
from ValidationPromptBuilder import ValidationPromptBuilder
import json



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
        print("[INFO] No additional files provided.")

    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_images, files_pdf)
    print("[INFO] Files processed successfully.")

    print("[INFO] Creating prompt for question generation...")
    # prompt_parts = PromptBuilder.create_prompt(num_questions, difficulty, incorrect_task, info_texts,
    #                                            encoded_base64_data, pdf_texts)

    prompt_get_question_prompt = PromptBuilder.get_question_prompt(num_questions, difficulty, incorrect_task)
    suffix_prompt_parts_validation = PromptBuilder.create_suffix_prompt(num_questions, difficulty)
    print("[INFO] Prompt created successfully.")

    print("[INFO] Building message for OpenAI API request...")
    message = MessageBuilder.build_message(prompt_get_question_prompt, info_texts, encoded_base64_data, pdf_texts,
                                           suffix_prompt_parts_validation)
    print("[INFO] Message built successfully.")

    print("[INFO] Sending question generation request to OpenAI API...")
    result = OpenAIClient.send_request(message, TEMPERATURE, ExamQuestionWithExamples)
    print("[INFO] Question generation completed successfully.")
    print(result)

    results = []
    total_questions = len(result["questions"])
    for index, exam_question in enumerate(result["questions"], start=1):
        print(f"[INFO] Preparing validation for question {index} of {total_questions}...")

        print(exam_question)

        zustand_prompt = PromptBuilder.get_zustand_prompt()
        message_zustand = MessageBuilder.build_refinement_validation_message1(zustand_prompt, exam_question)
        print(message_zustand)

        print(f"[INFO] Validation message built successfully for question {index}.")

        print(f"[INFO] Sending validation request for question {index} to OpenAI API...")
        zustand_table = OpenAIClient.send_request(message_zustand, VALIDATION_TEMPERATURE, SolutionStateTransitionTable)
        print(f"[INFO] Validation for question {index} completed successfully.")

        print(f"[INFO] Starting refinement validation round 1 for question {index}...")
        print(zustand_table)

        bsp_prompt = PromptBuilder.get_bsp_prompt()

        message_bsp_prompt = MessageBuilder.build_refinement_validation_message1(
            bsp_prompt, json.dumps(exam_question) + json.dumps(zustand_table))

        bsp_table = OpenAIClient.send_request(
            message_bsp_prompt, VALIDATION_TEMPERATURE, SolutionExampleFlowTable)

        print(bsp_table)

        print(f"[INFO] Refinement validation round 1 completed for question {index}.")
        print(f"[INFO] Starting refinement validation round 2 for question {index}...")

        sol_prompt = PromptBuilder.get_sol_prompt
        message_sol_prompt = MessageBuilder.build_refinement_validation_message1(
            sol_prompt, json.dumps(exam_question) + json.dumps(zustand_table) + json.dumps(bsp_table))

        full_question = OpenAIClient.send_request(
            message_sol_prompt, VALIDATION_TEMPERATURE, ExamQuestion)

        print(full_question)

        print(f"[INFO] Refinement validation round 2 completed for question {index}.")

        results.append(full_question)
        print(f"[INFO] {index} of {total_questions} questions validated.")

        # "--------------json compare-----------------"

        # if json.dumps(exam_question) == json.dumps(validated_question):
        #     print("No changes detected. Validation process may not be effective.")
        # else:
        #     print("Differences found. Validation made adjustments.")
        #
        # print("--output nicht korrigiert-----------------------------------------------------------")
        # print(json.dumps(exam_question))
        # print("--output nach validation prompt--------------------------------------------------------------------")
        # print(json.dumps(validated_question))

    print("[INFO] All questions validated successfully.")

    result_final = {"questions": results}
    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate)
    # OutputSaver.save_output_to_file(result, output_format, separate)
    print("[INFO] Output saved successfully.")

    print("[INFO] Process completed successfully.")

    if result == result_final:
        print("No changes detected. Validation process may not be effective.")
    else:
        print("Differences found. Validation made adjustments.")

    print("--output, nach erstem durchlauf-----------------------------------------------------------")
    print(result)
    print("--output nach validation prompt--------------------------------------------------------------------")
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