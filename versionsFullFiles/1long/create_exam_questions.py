from Const import TEMPERATURE, VALIDATION_TEMPERATURE
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from PromptBuilder import PromptBuilder
from Questions import ExamQuestion, ExamQuestions
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

    prefix_prompt_parts_validation = PromptBuilder.create_prefix_prompt(num_questions, difficulty, incorrect_task,
                                                                        info_texts, encoded_base64_data, pdf_texts)
    suffix_prompt_parts_validation = PromptBuilder.create_suffix_prompt(num_questions, difficulty)
    print("[INFO] Prompt created successfully.")

    print("[INFO] Building message for OpenAI API request...")
    message = MessageBuilder.build_message(prefix_prompt_parts_validation, info_texts, encoded_base64_data, pdf_texts,
                                           suffix_prompt_parts_validation)
    print("[INFO] Message built successfully.")

    print("[INFO] Sending question generation request to OpenAI API...")
    result = OpenAIClient.send_request(message, TEMPERATURE, ExamQuestions)
    print("[INFO] Question generation completed successfully.")

    results = []
    total_questions = len(result["questions"])

    for index, exam_question in enumerate(result["questions"], start=1):
        print(f"[INFO] Preparing validation for question {index} of {total_questions}...")

        prefix_prompt_parts_validation = ValidationPromptBuilder.create_prefix_validation_prompt()
        suffix_prompt_parts_validation = ValidationPromptBuilder.create_suffix_validation_prompt()
        print(f"[INFO] Validation prompt created successfully for question {index}.")

        message_validation = MessageBuilder.build_validation_message(
            prefix_prompt_parts_validation, exam_question, suffix_prompt_parts_validation)
        print(f"[INFO] Validation message built successfully for question {index}.")

        print(f"[INFO] Sending validation request for question {index} to OpenAI API...")
        validated_question = OpenAIClient.send_request(message_validation, VALIDATION_TEMPERATURE, ExamQuestion)
        print(f"[INFO] Validation for question {index} completed successfully.")

# Validation loop

        for refinement_round in range(2):
            print(f"[INFO] Starting refinement validation round {refinement_round + 1} for question {index}...")

            prompt_parts_refinement_validation = ValidationPromptBuilder.create_refinement_validation_prompt()
            message_refinement_validation = MessageBuilder.build_refinement_validation_message(
                prompt_parts_refinement_validation, validated_question)

            validated_question = OpenAIClient.send_request(
                message_refinement_validation, VALIDATION_TEMPERATURE, ExamQuestion)

            print(f"[INFO] Refinement validation round {refinement_round + 1} completed for question {index}.")

        results.append(validated_question)
        print(f"[INFO] {index} of {total_questions} questions validated.")

        # "--------------json compare-----------------"

        # if json.dumps(exam_question) == json.dumps(validated_question):
        #     print("No changes detected. Validation process may not be effective.")
        # else:
        #     print("Differences found. Validation made adjustments.")

        print("--output nicht korrigiert-----------------------------------------------------------")
        print(json.dumps(exam_question))
        print("--output nach validation prompt--------------------------------------------------------------------")
        print(json.dumps(validated_question))

    print("[INFO] All questions validated successfully.")

    result_final = {"questions": results}

    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate)
    print("[INFO] Output saved successfully.")

    print("[INFO] Process completed successfully.")

    # if result == result_final:
    #     print("No changes detected. Validation process may not be effective.")
    # else:
    #     print("Differences found. Validation made adjustments.")
    #
    # print("--output, nach erstem durchlauf-----------------------------------------------------------")
    # print(result)
    # print("--output nach validation prompt--------------------------------------------------------------------")
    # print(result_final)


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