import argparse
import base64
import os

import openai
from openai import OpenAI

from config import API_KEY
from const import GPT_MODEL, MAX_TOKENS, TEMPERATURE


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create a quiz from a markdown file.")
    parser.add_argument('--questions', type=int, required=True, help="Number of questions to create")
    # parser.add_argument('--output', type=str, required=True, choices=[GIFT, TXT],
    #                     help="Output format for the quiz")
    parser.add_argument('--difficulty', type=str, required=False, choices=['leicht', 'mittel', 'schwer'],
                        help="Difficulty of the questions")

    return parser.parse_args()


class ApiConnectionException(Exception):
    pass


# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def gpt_request(prompt):

    client = OpenAI(api_key=API_KEY)

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=GPT_MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
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
    # args = parse_arguments()
    # num_questions = args.questions
    # output_format = args.output
    # difficulty = args.difficulty
    print(gpt_request("wie viel einwohner hat würzburg"))


if __name__ == "__main__":
    main()
