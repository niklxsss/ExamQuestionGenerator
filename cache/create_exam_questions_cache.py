import base64
import openai
import argparse
import pdfplumber

from openai import OpenAI
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from Config import API_KEY
from Const import *
from Prompt import PROMPT


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create Exam Questions")
    parser.add_argument('--num_questions', type=int, help="Number of questions to generate", default=1)
    parser.add_argument('--files_images', type=str, nargs='+', help="Paths to multiple images", default=[])
    parser.add_argument('--files_txt', type=str, nargs='+', help="Paths to multiple text files", default=[])
    parser.add_argument('--files_pdf', type=str, nargs='+', help="Paths to multiple pdf files", default=[])
    parser.add_argument('--output', type=str, help="Output format for the questions", required=True, choices=[TXT_FORMAT, PDF_FORMAT])
    return parser.parse_args()


def encode_file_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_pdf_as_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n\n"
    return text


def process_files(files_text, files_images, files_pdf):

    info_texts = [read_text_file(file) for file in files_text]
    encoded_base64_data = [encode_file_to_base64(file) for file in files_images]
    pdf_texts = [read_pdf_as_text(file) for file in files_pdf]

    return info_texts, encoded_base64_data, pdf_texts


def build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts):

    message = message = [
        {
            "role": "user",
            "content": []
        }
    ]

    message[0]["content"].append(add_txt_to_message(prompt_text))

    for info_text in info_texts:
        message[0]["content"].append(add_txt_to_message(info_text))
        print(info_text)
    for encoded_base64_datum in encoded_base64_data:
        message[0]["content"].append(add_base64_file_to_message(encoded_base64_datum))
        print(encoded_base64_datum)
    for pdf_text in pdf_texts:
        message[0]["content"].append(add_txt_to_message(pdf_text))
        print(pdf_text)

    return message


def add_txt_to_message(prompt):
    return {
        "type": "text",
        "text": prompt
    }


def add_base64_file_to_message(encoded_base64_data):
    return {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{encoded_base64_data}",
        }
    }


def send_request_to_openai(message):
    client = OpenAI(api_key=API_KEY)

    try:
        response = client.chat.completions.create(
            model=GPT_MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            messages=message

        )
        return response.choices[0].message.content

    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)
    except openai.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
        print(e.status_code)
        print(e.response)
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)


def save_output_to_file(output, file_type):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"TuringMaschineAufgaben_{timestamp}.{file_type.lower()}"

    if file_type.upper() == TXT_FORMAT:
        save_output_to_txt(output, filename)
    elif file_type.upper() == PDF_FORMAT:
        save_output_to_pdf(output, filename)
    else:
        raise ValueError("Unsupported file type. Choose 'TXT' or 'PDF'.")

    print(f"Output saved to {filename}")


def save_output_to_txt(output, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output)


def save_output_to_pdf(output_text, filename):
    doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    content = []

    for line in output_text.splitlines():
        content.append(Paragraph(line, style))
        content.append(Spacer(1, 12))

    doc.build(content)


def main():
    args = parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_images
    files_txt = args.files_txt
    files_pdf = args.files_pdf
    output_format = args.output

    # prompt_text = "Was ist auf dem bild zusehen? Und um was geht es in dem text? Bitte beantworte beide Fragen"
    prompt_text = "generiere mir ähnliche aufgaben zur turingmaschine!"
    # prompt_text = PROMPT
    info_texts, encoded_base64_data, pdf_texts = process_files(files_txt, files_images, files_pdf)

    message = build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts)
    # print(message)

    result = send_request_to_openai(message)
    print(result)

    save_output_to_file(result, output_format)


if __name__ == "__main__":
    main()

# create_exam_questions --files_txt Unit05.txt --files AblaufGrafik.png

# create_exam_questions --files Unbenannt.PNG




# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2