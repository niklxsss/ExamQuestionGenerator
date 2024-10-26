# PROMPT = """
# You are an AI teaching assistant specializing in computer science. Create a set of challenging, application-based exam exercises on the topic of Turing Machines. These exercises should not focus on theory or definitions, but instead require practical applications where students must demonstrate their understanding of Turing Machine operations. Design each question to test students' ability to apply Turing Machine principles to solve computational problems.
#
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


# def create_prompt(base_prompt, files_txt, files_pdf, files_images):
#     full_prompt = base_prompt
#
#     if files_images:
#         full_prompt += "\n\nAdditionally, incorporate the content from the attached images. Analyze each image to determine how it can support or illustrate a practical application of Turing Machine principles."
#
#     if files_pdf:
#         full_prompt += "\n\nReview the information provided in the attached PDF(s). Use any computational scenarios or examples in the PDF(s) to create hands-on exercises involving Turing Machine operations."
#
#     if files_txt:
#         full_prompt += "\n\nThe text files included contain additional reference material or context. Integrate this information into the exercises to add depth to the scenarios."
#
#     return full_prompt
