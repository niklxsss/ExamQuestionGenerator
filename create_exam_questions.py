from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver


def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_images
    files_txt = args.files_txt
    files_pdf = args.files_pdf
    separate_answers = args.separate_answers
    output_format = args.output

    prompt_text = """Sie sind KI-Lehrassistent mit Schwerpunkt Informatik. Generieren Sie genau 3 anspruchsvolle, 
    anwendungsbezogene Prüfungsaufgaben zu Turingmaschinen mit jeweils dem übergebenen Format:"""

    info_texts, encoded_base64_data, pdf_texts = FileProcessor.process_files(files_txt, files_images, files_pdf)
    message = MessageBuilder.build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts)

    result = OpenAIClient.send_request(message)
    print(result)

    OutputSaver.save_output_to_file(result, output_format, separate_answers)


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2
