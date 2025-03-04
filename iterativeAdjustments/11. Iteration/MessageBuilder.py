import json

from PromptBuilder import PromptBuilder
from ValidationPromptBuilder import ValidationPromptBuilder


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
    def create_task_message(num_questions, difficulty, info_texts, encoded_base64_data, pdf_texts, incorrect_task):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_task_system_prompt(any([info_texts, encoded_base64_data, pdf_texts])))]
        )

        info_files_prompt = MessageBuilder.add_message(
            "user",
            [
                *(
                    item
                    for info_text in info_texts
                    for item in [
                    MessageBuilder.add_txt_to_content(PromptBuilder.get_txt_prompt()),
                    MessageBuilder.add_txt_to_content(info_text),
                ]
                ),

                *(
                    item
                    for encoded_base64_datum in encoded_base64_data
                    for item in [
                    MessageBuilder.add_txt_to_content(PromptBuilder.get_bas64_prompt()),
                    MessageBuilder.add_base64_file_to_content(encoded_base64_datum)
                ]
                ),

                *(
                    item
                    for pdf_text in pdf_texts
                    for item in [
                    MessageBuilder.add_txt_to_content(PromptBuilder.get_pdf_texts_prompt()),
                    MessageBuilder.add_txt_to_content(pdf_text)
                ]
                ),
            ])

        all_messages = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_all_task_prompt(num_questions,difficulty, incorrect_task))]
        )

        quality_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_task_quality_prompt())]
        )

        messages.append(system_prompt)
        messages.append(info_files_prompt)
        messages.append(all_messages)
        messages.append(quality_prompt)


        return messages

    @staticmethod
    def create_state_transition_table_message(question_content):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_state_transition_table_system_prompt())
            ]
        )

        task_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_state_transition_table_task_prompt(question_content)),
            ]
        )

        requirements_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_state_transition_table_requirements_prompt())
            ]
        )

        request_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_state_transition_table_request_prompt())
            ]
        )

        quality_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_state_transition_table_quality_prompt())]
        )

        messages.append(system_prompt)
        messages.append(task_prompt)
        messages.append(requirements_prompt)
        messages.append(request_prompt)
        messages.append(quality_prompt)

        return messages

    @staticmethod
    def create_example_flow_table_message(question_content, state_transition_table_content):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_example_flow_table_system_prompt())]
        )

        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_example_flow_table_task_prompt(question_content, state_transition_table_content)),
            ]
        )

        requirements_request_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_example_flow_table_requirements_prompt()),
                MessageBuilder.add_txt_to_content(PromptBuilder.get_example_flow_table_request_prompt())
            ]
        )

        quality_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_example_flow_table_quality_prompt())]
        )

        messages.append(system_prompt)
        messages.append(base_prompt)
        messages.append(requirements_request_prompt)
        messages.append(quality_prompt)

        return messages

    @staticmethod
    def create_solution_message(validated_task_and_tables):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_solution_system_prompt())]
        )

        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(PromptBuilder.get_solution_requirements_prompt()),
                MessageBuilder.add_txt_to_content(PromptBuilder.get_solution_request_prompt(validated_task_and_tables)),
            ]
        )

        quality_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(PromptBuilder.get_solution_quality_prompt())]
        )

        messages.append(system_prompt)
        messages.append(base_prompt)
        messages.append(quality_prompt)

        return messages

    @staticmethod
    def create_validation_message(question_content, state_transition_table_content, example_flow_table_content):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(
                ValidationPromptBuilder.get_validation_system_prompt())]
        )

        task_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    ValidationPromptBuilder.get_analysis_prompt(question_content)),
                MessageBuilder.add_txt_to_content(
                    ValidationPromptBuilder.get_state_transition_table_prompt(state_transition_table_content)),
                MessageBuilder.add_txt_to_content(
                    ValidationPromptBuilder.get_example_flow_table_prompt(example_flow_table_content)),
            ]
        )

        messages.append(system_prompt)
        messages.append(task_prompt)

        return messages


    @staticmethod
    def create_validation_state_transition_table_message(task_parts):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(ValidationPromptBuilder.get_validation_system_prompt_state_transition_table())]
        )

        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(ValidationPromptBuilder.get_validation_user_prompt_state_transition_tableee(task_parts)),
                # MessageBuilder.add_txt_to_content(
                #     ValidationPromptBuilder.get_validation_user_prompt_state_transition_tablee(task_parts)),
            ]
        )

        task_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    ValidationPromptBuilder.get_validation_user_prompt_state_transition_tablee(task_parts)),
            ]
        )

        messages.append(system_prompt)
        messages.append(base_prompt)
        # messages.append(task_prompt)

        return messages


    @staticmethod
    def create_validation_example_flow_table_message(task_parts):
        messages = []

        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(ValidationPromptBuilder.get_validation_system_prompt_example_flow_table())]
        )

        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(ValidationPromptBuilder.get_validation_user_prompt_example_flow_table(task_parts)),
            ]
        )

        task_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    ValidationPromptBuilder.get_validation_user_prompt_example_flow_tablee(task_parts)),
            ]
        )

        messages.append(system_prompt)
        # messages.append(base_prompt)
        messages.append(task_prompt)

        return messages
