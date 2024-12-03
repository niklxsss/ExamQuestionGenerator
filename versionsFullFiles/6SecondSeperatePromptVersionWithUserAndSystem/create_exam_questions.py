import time
from asyncio import wait

from Const import TEMPERATURE, VALIDATION_TEMPERATURE
from FileProcessor import FileProcessor
from InputArgumentParser import InputArgumentParser
from MessageBuilder import MessageBuilder
from OpenAIClient import OpenAIClient
from OutputSaver import OutputSaver
from PromptBuilder import PromptBuilder
from Questions import ExamQuestion, ExamQuestions, ExamQuestionWithExample, ExamQuestionWithExamples, TableContent, \
    SolutionStateTransitionTable, SolutionExampleFlowTable
from SplittedRequests import SplittedRequests
from ValidationPromptBuilder import ValidationPromptBuilder
import json



def main():
    args = InputArgumentParser.parse_arguments()
    num_questions = args.num_questions
    files_images = args.files_images
    files_txt = args.files_txt
    files_pdf = args.files_pdf
    separate = args.separate
    output_format = args.output
    difficulty = args.difficulty
    incorrect_task = args.incorrect_task

    print(f"[INFO] Number of questions to generate: {num_questions}")
    print(f"[INFO] Difficulty level: {difficulty}")
    print(f"[INFO] incorrect task: {incorrect_task}")
    print(f"[INFO] Output format: {output_format}")

    if any([files_txt, files_images, files_pdf]):
        print("[INFO] Processing attached files...")
    else:
        print("[INFO] No additional files provided.")

    resultaufgabestellung = OpenAIClient.send_request(SplittedRequests.create_aufgabenstellung_prompt(num_questions, difficulty), TEMPERATURE, ExamQuestionWithExample)
    resultZustand = OpenAIClient.send_request(SplittedRequests.create_zustandsübergangstabelle_prompt(str(resultaufgabestellung)), TEMPERATURE,TableContent)
    resultbsp = OpenAIClient.send_request(SplittedRequests.create_Beispielablauftabelle_prompt(str(resultaufgabestellung) + str(resultZustand)), TEMPERATURE, TableContent)
    result = OpenAIClient.send_request(SplittedRequests.create_restlösung_prompt(str(resultaufgabestellung) + str(resultZustand) + str(resultbsp)),TEMPERATURE,ExamQuestions)
    # result = ExamQuestions(questions=[resulta])
    print("[INFO] Question generation completed successfully.")
    #
    print(result)

    OutputSaver.save_output_to_file(result, output_format, separate)


if __name__ == "__main__":
    main()

# https://github.com/openai/openai-python
# https://platform.openai.com/docs/guides/vision
# https://platform.openai.com/docs/guides/structured-outputs/how-to-use?context=ex2

# create_exam_questions --output TXT --files_pdf gie-informatik_uebung_08.pdf --num_questions 5

# create_exam_questions --output PDF --files_images AblaufGrafik.png --files_txt Unit05.txt --files_pdf gie-informatik_uebung_08.pdf --num_questions 15

# JSON compare:
# https://jsonviewer.stack.hu/
# https://jsondiff.com/