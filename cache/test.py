import base64

import openai
import argparse

from openai import OpenAI

from Config import API_KEY
from Const import TEMPERATURE, MAX_TOKENS


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create Exam Questions")
    parser.add_argument('--num_questions', type=int, help="Number of questions to generate", default=1)
    parser.add_argument('--files', type=str, nargs='+', help="Paths to the images or PDFs", required=False)
    parser.add_argument('--files_txt', type=str, nargs='+', help="Paths to multiple text files", required=False)
    # parser.add_argument('--output', type=str, help="Output format for the questions", required=True, choices=[GIFT, TXT])

    return parser.parse_args()


def encode_file_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def process_files(binary_files, text_files):

    info_texts = [read_text_file(file) for file in text_files]
    encoded_base64_data = [encode_file_to_base64(file) for file in binary_files]

    return info_texts, encoded_base64_data


def build_message(prompt_text, info_texts, encoded_base64_data):

    message = message = [
        {
            "role": "user",
            "content": []
        }
    ]

    message[0]["content"].append(add_txt_to_message(prompt_text))
    for info_text in info_texts:
        message[0]["content"].append(add_txt_to_message(info_text))
    for encoded_base64_datum in encoded_base64_data:
        message[0]["content"].append(add_base64_file_to_message(encoded_base64_datum))

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
            model="gpt-4o-mini",
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
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)


def main():
    args = parse_arguments()
    num_questions = args.num_questions
    files = args.files
    files_txt = args.files_txt

    prompt_text = "wo ist würzburg?"
    info_texts, encoded_base64_data = process_files(files_txt, files)

    message = build_message(prompt_text, info_texts, encoded_base64_data)

    result = send_request_to_openai(message)

    print(result)


if __name__ == "__main__":
    main()
