from Const import VALIDATION_MESSAGE_RESULT_PREFIX
import json


class MessageBuilder:

    @staticmethod
    def add_txt_to_message(text):
        return {"type": "text", "text": text}

    @staticmethod
    def add_base64_file_to_message(encoded_base64_data):
        return {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_base64_data}"}}

    @staticmethod
    def build_message(prefix_prompt_parts, info_texts, encoded_base64_data, pdf_texts, suffix_prompt_parts):
        message = [{"role": "user", "content": []}]

        for part in prefix_prompt_parts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(part))

        for info_text in info_texts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(info_text))

        for encoded_base64_datum in encoded_base64_data:
            message[0]["content"].append(MessageBuilder.add_base64_file_to_message(encoded_base64_datum))

        for pdf_text in pdf_texts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(pdf_text))

        for part in suffix_prompt_parts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(part))

        return message

    @staticmethod
    def build_validation_message(prefix_prompt_parts, result, suffix_prompt_parts):
        message = [{"role": "user", "content": []}]

        for part in prefix_prompt_parts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(part))

        message[0]["content"].append(MessageBuilder.add_txt_to_message(VALIDATION_MESSAGE_RESULT_PREFIX +
                                                                       json.dumps(result, indent=2)))
        for part in suffix_prompt_parts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(part))

        return message

    @staticmethod
    def build_refinement_validation_message(prompt_parts, result):
        message = [{"role": "user", "content": []}]

        for part in prompt_parts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(part))

        message[0]["content"].append(MessageBuilder.add_txt_to_message(VALIDATION_MESSAGE_RESULT_PREFIX +
                                                                       json.dumps(result, indent=2)))

        return message