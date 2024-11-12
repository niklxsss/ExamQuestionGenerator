GPT_MODEL = "gpt-4o"
MAX_TOKENS = 8000
TEMPERATURE = 0.7

TXT_FORMAT = "TXT"
PDF_FORMAT = "PDF"
JSON_FORMAT = "JSON"

UNDERSCORE = "_"
COLON = ": "

FILE_NAME_PREFIX = "TuringMaschine"
FILE_NAME_QUESTIONS = "Aufgaben"
FILE_NAME_SOLUTIONS = "Lösungen"
FILE_NAME_QUESTIONS_AND_SOLUTIONS = FILE_NAME_QUESTIONS + UNDERSCORE + FILE_NAME_SOLUTIONS

SECTION_QUESTIONS = "questions"
SECTION_QUESTION_CONTENT = "question_content"
SECTION_QUESTION = "question"
SECTION_QUESTION_ADDITIONAL_INFOS = "optional_question_additional_infos"
SECTION_QUESTION_TABLES = "optional_question_tables"

SECTION_SOLUTIONS = "solutions"
SECTION_SOLUTION_CONTENT = "solution_content"
SECTION_SOLUTION = "solution"
SECTION_SOLUTION_STEP_BY_STEP = "optional_solution_step_by_step"
SECTION_SOLUTION_ADDITIONAL_INFOS = "optional_solution_additional_infos"
SECTION_SOLUTION_TABLES = "optional_solution_tables"

SECTION_TABLES_TITLE = "title"
SECTION_TABLES_HEADERS = "headers"
SECTION_TABLES_ROWS = "rows"

SECTION_EXAMPLE = "optional_example"
SECTION_ID = "id"

LABEL_TASK = "Aufgabe"
LABEL_QUESTION = "Frage"
LABEL_SOLUTION = "Lösung"
LABEL_EXAMPLE = "Beispiel"
LABEL_ADDITIONAL_INFOS = "Zusatzinformationen"
LABEL_SOLUTION_STEP_BY_STEP = "Lösungsweg"
LABEL_ADDITIONAL_SOLUTION_INFOS = "Zusatzinformationen"
LABEL_TABLE = "Tabelle"
