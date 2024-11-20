GPT_MODEL = "gpt-4o"
MAX_TOKENS = 8000
TEMPERATURE = 0.6
VALIDATION_TEMPERATURE = 0.2

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

TASK_TYPE_INCORRECT_TASK = 'incorrect_tasks'

DIFFICULTY_EASY = 'leicht'
DIFFICULTY_MEDIUM = 'mittel'
DIFFICULTY_CHALLENGING = 'anspruchsvoll'
# DIFFICULTY_ADVANCED = 'fortgeschritten'
# DIFFICULTY_EXTREME = 'extrem schwierig'

DIFFICULTY_EXPLANATION_MAP = {
    DIFFICULTY_EASY:
        "Die Aufgaben sollen auf einem grundlegenden Niveau sein und die wesentlichen Konzepte der Turingmaschine "
        "abfragen, ohne zu komplex zu werden. DIE AUFGABEN SOLLEN EINFACH SEIN!",
    DIFFICULTY_MEDIUM:
        "Die Aufgaben sollen moderate Herausforderungen darstellen, die ein Verständnis grundlegender Konzepte sowie "
        "zusätzliche Denkschritte erfordern. DIE AUFGABEN SOLLEN EINFACH NUR MITTELMÄßIG SCHWER SEIN!",
    DIFFICULTY_CHALLENGING:
        "Die Aufgaben sollen ein hohes Maß an Verständnis und analytisches Denken erfordern und die Anwendung der "
        "Konzepte umfassend prüfen.",
    # DIFFICULTY_ADVANCED:
    #     "Fordere tiefgehendes Verständnis und Anwendungskompetenz durch komplexe Szenarien und mehrstufige "
    #     "Problemstellungen.",
    # DIFFICULTY_EXTREME:
    #     "Erzeuge Aufgaben auf höchstem Schwierigkeitsniveau, die intensive Analyse, strategische Planung und "
    #     "mehrschrittige Lösungsansätze erfordern. "
}

DIFFICULTY_WORDING_MAP = {
    DIFFICULTY_EASY:
        "leichte",
    DIFFICULTY_MEDIUM:
        "moderate",
    DIFFICULTY_CHALLENGING:
        "anspruchsvolle",
    # DIFFICULTY_ADVANCED:
    #     "",
    # DIFFICULTY_EXTREME:
    #     "mehrschrittige Lösungsansätze erfordern. "
}
