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

    prompt_parts = PromptBuilder.create_prompt(num_questions, difficulty, task_type, info_texts, encoded_base64_data,
                                               pdf_texts)

    message = MessageBuilder.build_message(prompt_parts, info_texts, encoded_base64_data, pdf_texts)
    result = OpenAIClient.send_request(message, TEMPERATURE)

    prompt_parts_validation = PromptBuilder.create_validation_prompt()
    message_validation = MessageBuilder.build_validation_message(prompt_parts_validation, result)
    result_final = OpenAIClient.send_request(message_validation, VALIDATION_TEMPERATURE)
    OutputSaver.save_output_to_file(result_final, output_format, separate_answers)

    print(result)
    print("-------------------------------------------------------------------------------------------------")
    print(result_final)


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2

# create_exam_questions --output TXT --files_pdf gie-informatik_uebung_08.pdf --num_questions 5

# create_exam_questions --output PDF --files_images AblaufGrafik.png --files_txt Unit05.txt --files_pdf gie-informatik_uebung_08.pdf --num_questions 15
