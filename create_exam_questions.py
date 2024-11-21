from Const import TEMPERATURE, VALIDATION_TEMPERATURE
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from PromptBuilder import PromptBuilder


def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_images
    files_txt = args.files_txt
    files_pdf = args.files_pdf
    separate_answers = args.separate_answers
    output_format = args.output
    difficulty = args.difficulty
    task_type = args.task_type

    print(f"[INFO] Number of questions to generate: {num_questions}")
    print(f"[INFO] Difficulty level: {difficulty}")
    print(f"[INFO] Task type: {task_type}")
    print(f"[INFO] Output format: {output_format}")

    if any([files_txt, files_images, files_pdf]):
        print("[INFO] Processing attached files...")
    else:
        print("[INFO] No additional files provided.")

    # Process files
    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_images, files_pdf)
    print("[INFO] Files processed successfully.")

    # Create prompt
    print("[INFO] Creating prompt for question generation...")
    prompt_parts = PromptBuilder.create_prompt(num_questions, difficulty, task_type, info_texts, encoded_base64_data,
                                               pdf_texts)
    print("[INFO] Prompt created successfully.")

    # Build message
    print("[INFO] Building message for OpenAI API request...")
    message = MessageBuilder.build_message(prompt_parts, info_texts, encoded_base64_data, pdf_texts)
    print("[INFO] Message built successfully.")

    # Send request to OpenAI
    print("[INFO] Sending question generation request to OpenAI API...")
    result = OpenAIClient.send_request(message, TEMPERATURE)
    print("[INFO] Question generation completed successfully.")

    # Create validation prompt
    print("[INFO] Creating validation prompt...")
    prompt_parts_validation = PromptBuilder.create_validation_prompt()
    print("[INFO] Validation prompt created successfully.")

    print("[INFO] Building validation message...")
    message_validation = MessageBuilder.build_validation_message(prompt_parts_validation, result)
    print("[INFO] Validation message built successfully.")

    # Send validation request
    print("[INFO] Sending validation request to OpenAI API...")
    result_final = OpenAIClient.send_request(message_validation, VALIDATION_TEMPERATURE)
    print("[INFO] Validation completed successfully.")

    # Save output
    print("[INFO] Saving final output to file...")
    OutputSaver.save_output_to_file(result_final, output_format, separate_answers)
    print("[INFO] Output saved successfully.")

    print("[INFO] Process completed successfully.")

    # print(result)
    # print("-------------------------------------------------------------------------------------------------")
    # print(result_final)


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2

# create_exam_questions --output TXT --files_pdf gie-informatik_uebung_08.pdf --num_questions 5

# create_exam_questions --output PDF --files_images AblaufGrafik.png --files_txt Unit05.txt --files_pdf gie-informatik_uebung_08.pdf --num_questions 15
