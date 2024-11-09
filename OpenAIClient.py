import openai

from openai import OpenAI
from Config import *
from Const import *
from Questions import ExamQuestions


class OpenAIClient:

    @staticmethod
    def send_request(message) -> ExamQuestions:
        client = OpenAI(api_key=API_KEY)

        try:
            response = client.beta.chat.completions.parse(
                model=GPT_MODEL,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                messages=message,
                response_format=ExamQuestions,

            )
            return response.choices[0].message.content

        except openai.APIConnectionError as e:
            print("The server could not be reached:", e.__cause__)
        except openai.RateLimitError as e:
            print("Rate limit error:", e.status_code, e.response)
        except openai.APIStatusError as e:
            print("API returned a non-200 status code:", e.status_code, e.response)
