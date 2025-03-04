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

    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_images, files_pdf)

    prompt_text = PromptBuilder.create_prompt(num_questions, difficulty, task_type,info_texts, encoded_base64_data,
                                              pdf_texts)


    message = MessageBuilder.build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts)
    result = OpenAIClient.send_request(message, TEMPERATURE)

    validation_prompt_text = PromptBuilder.create_validation_prompt()
    validation_message = MessageBuilder.build_validation_message(validation_prompt_text, result)
    print(validation_message)

    result_final = OpenAIClient.send_request(validation_message, VALIDATION_TEMPERATURE)
    OutputSaver.save_output_to_file(result_final, output_format, separate_answers)

    print(result)


if __name__ == "__main__":
    main()