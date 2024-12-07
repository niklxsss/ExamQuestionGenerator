import json
import time

import openai

from openai import OpenAI
from Config import *
from Const import *


class OpenAIClient:

    @staticmethod
    def send_request(message, temperature, response_format):
        time.sleep(1)
        client = OpenAI(api_key=API_KEY)

        try:
            response = client.beta.chat.completions.parse(
                model=GPT_MODEL,
                max_tokens=MAX_TOKENS,
                temperature=temperature,
                messages=message,
                response_format=response_format
            )
            return json.loads(response.choices[0].message.content)

        except openai.APIConnectionError as e:
            print("The server could not be reached:", e.__cause__)
            exit()
        except openai.RateLimitError as e:
            print("Rate limit error:", e.status_code, e.response)
            # print("Rate Limit Error:", e)
            # print("Details:", e.headers if hasattr(e, 'headers') else "Keine Header-Details verfügbar")
            # print("Retry-After:", e.headers.get("Retry-After", "Nicht angegeben"))
            exit()
        except openai.APIStatusError as e:
            print("API returned a non-200 status code:", e.status_code, e.response)
            exit()
