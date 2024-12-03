GPT_MODEL = "gpt-4o"
MAX_TOKENS = 8000
TASK_GENERATION_TEMPERATURE = 0.7
ADDITIONAL_TASK_GENERATION_TEMPERATURE = 0.3
VALIDATION_TEMPERATURE = 0.3

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
SECTION_ADDITIONAL_SOLUTION_TABLES = "optional_additional_solution_tables"
SECTION_SOLUTION_STATE_TRANSITION_TABLE = "solution_state_transition_table"
SECTION_SOLUTION_EXAMPLE_FLOW_TABLE = "solution_example_flow_table"

SECTION_TABLES_TITLE = "title"
SECTION_TABLES_HEADERS = "headers"
SECTION_TABLES_ROWS = "rows"

SECTION_EXAMPLE = "example"
SECTION_ID = "id"

LABEL_TASK = "Aufgabe"
LABEL_QUESTION = "Frage"
LABEL_SOLUTION = "Lösung"
LABEL_EXAMPLE = "Beispiel"
LABEL_ADDITIONAL_INFOS = "Zusatzinformationen"
LABEL_SOLUTION_STEP_BY_STEP = "Lösungsweg"
LABEL_ADDITIONAL_SOLUTION_INFOS = "Zusatzinformationen"
LABEL_TABLE = "Tabelle"

DIFFICULTY_EASY = 'easy'
DIFFICULTY_MEDIUM = 'medium'
DIFFICULTY_CHALLENGING = 'challenging'
DIFFICULTY_ADVANCED = 'advanced'
DIFFICULTY_EXTREME = 'extreme'

DIFFICULTY_TRANSLATION_MAP = {
    DIFFICULTY_EASY: 'leicht',
    DIFFICULTY_MEDIUM: 'mittel',
    DIFFICULTY_CHALLENGING: 'anspruchsvoll',
    DIFFICULTY_ADVANCED: 'fortgeschritten',
    DIFFICULTY_EXTREME: 'extrem schwierig'
}

DIFFICULTY_EXPLANATION_MAP = {
    DIFFICULTY_EASY:
        "Aufgaben auf diesem Niveau vermitteln grundlegende Konzepte der Turingmaschine. "
        "Die Lösung umfasst einfache Übergänge und klare logische Strukturen ohne Schleifen oder Bedingungen. "
        "Die Aufgaben konzentrieren sich auf elementare Operationen wie das Schreiben und Verschieben des Bandkopfes, "
        "um das Verständnis grundlegender Zustandsübergänge zu fördern.",

    DIFFICULTY_MEDIUM:
        "Diese Aufgaben setzen ein solides Verständnis der Turingmaschine voraus. "
        "Die Lösung erfordert die Integration mehrerer Schritte mit Bedingungen und einfachen Schleifen. "
        "Die Aufgaben fordern ein besseres Verständnis der Sequenzen und Zustandsabfolgen, "
        "können aber immer noch in kleineren, klar strukturierten Blöcken umgesetzt werden.",

    DIFFICULTY_CHALLENGING:
        "Dieses Niveau verlangt analytisches Denken und ein tiefes Verständnis der Konzepte. "
        "Die Lösung beinhaltet komplexe logische Strukturen, verschachtelte Übergänge und erfordert "
        "das Verarbeiten und Überprüfen von längeren Eingabesequenzen. "
        "Die Aufgaben verlangen eine durchdachte Planung der Zustandsübergänge und das Verständnis anspruchsvollerer Bandoperationen.",

    DIFFICULTY_ADVANCED:
        "Diese Aufgaben verlangen ein umfassendes Verständnis und die Fähigkeit, komplexe Abläufe präzise umzusetzen. "
        "Sie umfassen dynamische Bedingungen, erweiterte Logiken und erfordern kreative Strategien, "
        "um Szenarien mit mehreren möglichen Endzuständen oder komplexen Prüfungen zu lösen. "
        "Die Aufgaben fördern das strategische Denken und die klare Strukturierung komplexer Zustandsübergänge.",

    DIFFICULTY_EXTREME:
        "Aufgaben auf diesem Schwierigkeitsniveau testen die Grenzen des Verständnisses der Turingmaschine. "
        "Die Lösung erfordert fortgeschrittenes strategisches Denken, das Navigieren durch mehrere verschachtelte Logiksysteme "
        "und die Berücksichtigung von Grenzfällen. "
        "Diese Aufgaben fordern maximale Präzision und Problemlösungsfähigkeit und beinhalten Szenarien, "
        "bei denen fehlerfreie Planung und Simulation unverzichtbar sind."
}


VALIDATION_MESSAGE_RESULT_PREFIX = "**HIER IST DIE ZU KORRIGIERENDE AUFGABE: **\n\n"