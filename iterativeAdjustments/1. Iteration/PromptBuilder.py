class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, files_txt, files_images, files_pdf):
        prompt = PromptBuilder.getBasePrompt(num_questions)

        attachment_prompt = ""
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_txt)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_pdf)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Bild-Datei", files_images)

        if attachment_prompt.strip():
            attachment_prompt_prefix = "\n\nZusätzliche Informationen zu den Aufgaben:\n\n"
            prompt += attachment_prompt_prefix + attachment_prompt

        return prompt

    @staticmethod
    def getBasePrompt(num_questions):
        return f"Sie sind KI-Lehrassistent mit Schwerpunkt Informatik. Generieren Sie genau {num_questions} " \
               f"anspruchsvolle, anwendungsbezogene Prüfungsaufgaben zu Turingmaschinen mit jeweils dem angegebenen " \
               f"Format." \
               f"Wenn eine Frage oder Lösung keine zusätzlichen Hinweise oder schrittweisen Anweisungen benötigt, " \
               f"lassen Sie diese Felder leer." \
               f"Format:" \
               f"- question: [Die eigentliche Frage]" \
               f"- additional_infos (optional): [Nur falls benötigt]" \
               f"- example (optional): [Nur falls notwendig für das Verständnis]" \
               f"- solution: [Die Lösung]" \
               f"- additional_solution_infos: (optional): [Nur falls benötigt]" \
               f"- step_by_step_solution (optional): [Nur falls benötigt]" \
               f"- tables (optional): [Nur falls benötigt für Zustandstabelle]"

    @staticmethod
    def get_attachment_prompt(datei_name, files):
        if files:
            return f"Die angehängte(n) {datei_name} enthalten zusätzliche Inhalte zur Turingmaschine. " \
                   f"Nutzen Sie diese Inhalte, um die Übungen entsprechend zu gestalten.\n\n"
        return ""