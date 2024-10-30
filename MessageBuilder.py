class MessageBuilder:

    @staticmethod
    def add_txt_to_message(prompt):
        return {"type": "text", "text": prompt}

    @staticmethod
    def add_base64_file_to_message(encoded_base64_data):
        return {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_base64_data}"}}

    @staticmethod
    def build_message(prompt_text, info_texts, encoded_base64_data, pdf_texts):
        message = [{"role": "user", "content": []}]
        message[0]["content"].append(MessageBuilder.add_txt_to_message(prompt_text))

        for info_text in info_texts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(info_text))

        for encoded_base64_datum in encoded_base64_data:
            message[0]["content"].append(MessageBuilder.add_base64_file_to_message(encoded_base64_datum))

        for pdf_text in pdf_texts:
            message[0]["content"].append(MessageBuilder.add_txt_to_message(pdf_text))

        return message
