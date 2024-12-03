from Const import VALIDATION_MESSAGE_RESULT_PREFIX
import json


class MessageBuilder:

    @staticmethod
    def add_txt_to_content(text):
        """
        Erstellt ein Textobjekt mit dem Typ 'text'.
        """
        return {"type": "text", "text": text}

    @staticmethod
    def add_base64_file_to_content(encoded_base64_data):
        """
        Erstellt ein Bildobjekt mit dem Typ 'image_url'.
        """
        return {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_base64_data}"}}

    @staticmethod
    def add_message(role, content_parts):
        """
        Erstellt eine Nachricht mit der spezifischen Rolle und den gegebenen Inhalten.
        """
        return {"role": role, "content": content_parts}

    @staticmethod
    def build_message(system_prompt, prefix_prompt_parts, info_texts, encoded_base64_data, pdf_texts, suffix_prompt_parts):
        """
        Baut die Nachrichtenstruktur:
        - Wenn `combine=True`, werden Abschnitte mit demselben `role` unter einem gemeinsamen `content` kombiniert.
        - Wenn `combine=False`, wird jeder Abschnitt als eigene Nachricht gesendet.
        """
        messages = [MessageBuilder.add_message("system", [MessageBuilder.add_txt_to_content(system_prompt)])]

        # Prefix-Prompts hinzufügen
        for part in prefix_prompt_parts:
            messages.append(MessageBuilder.add_message("user", [MessageBuilder.add_txt_to_content(part)]))

        # Info-Texte hinzufügen
        for info_text in info_texts:
            messages.append(MessageBuilder.add_message("user", [MessageBuilder.add_txt_to_content(info_text)]))

        # Base64-kodierte Bilddaten hinzufügen
        for encoded_base64_datum in encoded_base64_data:
            messages.append(MessageBuilder.add_message("user", [MessageBuilder.add_base64_file_to_content(encoded_base64_datum)]))

        # PDF-Texte hinzufügen
        for pdf_text in pdf_texts:
            messages.append(MessageBuilder.add_message("user", [MessageBuilder.add_txt_to_content(pdf_text)]))

        # Suffix-Prompts hinzufügen
        for part in suffix_prompt_parts:
            messages.append(MessageBuilder.add_message("user", [MessageBuilder.add_txt_to_content(part)]))


        return messages
