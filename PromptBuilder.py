# Each exercise should be presented with the following structure:
# 1. **Problem Description**: Describe the scenario or computational problem, including details like the initial state, tape configuration, and transitions.
# 2. **Objective**: Specify what the student must achieve (e.g., configure a Turing Machine to perform a certain task or derive an output from a given input).
# 3. **Requirements and Constraints**: Outline any specific requirements, such as tape alphabet limitations, head movement restrictions, or state transition limitations.
# 4. **Expected Output**: Describe the expected outcome or the final state configuration that indicates the task was performed correctly.
#
# Include multiple types of exercises, such as:
# - Configuring a Turing Machine to recognize a specific language or pattern.
# - Designing a Turing Machine to perform arithmetic operations (e.g., addition, subtraction).
# - Creating a Turing Machine to solve a problem involving binary numbers, such as binary counting or binary addition.
# - Analyzing a given Turing Machine setup and predicting the output based on specific inputs.
#
# Make sure each exercise is sufficiently challenging and tests the student's knowledge of Turing Machine applications.
# """

class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, files_txt, files_images, files_pdf):
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
               f"Format:"

    @staticmethod
    def get_attachment_prompt(datei_name, files):
        if files:
            return f"Die angehängte(n) {datei_name} enthalten zusätzliche Inhalte zur Turingmaschine. " \
                   f"Nutzen Sie diese Inhalte, um die Übungen entsprechend zu gestalten.\n\n"
        return ""
