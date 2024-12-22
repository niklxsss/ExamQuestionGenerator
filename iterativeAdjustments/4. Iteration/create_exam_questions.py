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

    print(prompt_text)
    message = MessageBuilder.build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts)
    result = OpenAIClient.send_request(message)
    OutputSaver.save_output_to_file(result, output_format, separate_answers)

    print(result)


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2

# create_exam_questions --output TXT --files_pdf gie-informatik_uebung_08.pdf --num_questions 5

# create_exam_questions --output PDF --files_images AblaufGrafik.png --files_txt Unit05.txt --files_pdf gie-informatik_uebung_08.pdf --num_questions 15