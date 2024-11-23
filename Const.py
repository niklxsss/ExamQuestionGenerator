GPT_MODEL = "gpt-4o"
MAX_TOKENS = 8000
TEMPERATURE = 0.6
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

DIFFICULTY_EASY = 'leicht'
DIFFICULTY_MEDIUM = 'mittel'
DIFFICULTY_CHALLENGING = 'anspruchsvoll'
DIFFICULTY_ADVANCED = 'fortgeschritten'
DIFFICULTY_EXTREME = 'extrem_schwierig'

DIFFICULTY_EXPLANATION_MAP = {
    DIFFICULTY_EASY:
        "Aufgaben auf diesem Niveau vermitteln grundlegende Konzepte der Turingmaschine. "
        "Die Lösung erfordert 2-6 Zustände mit einfachen und klar nachvollziehbaren Übergängen. "
        "Es werden keine verschachtelten logischen Strukturen oder erweiterten Bandoperationen benötigt. "
        "Die Aufgaben fördern das Verständnis für die grundlegende Funktionsweise von Zustandsübergängen und Bandaktionen.",

    DIFFICULTY_MEDIUM:
        "Diese Aufgaben bieten eine moderate Herausforderung und setzen ein solides Verständnis der Turingmaschine voraus. "
        "Die Lösung erfordert 6-12 Zustände und kann Übergänge mit zusätzlichen Bedingungen oder einfachen Schleifen umfassen. "
        "Die Aufgaben bauen auf den Grundlagen auf, verlangen aber mehrere Schritte und ein besseres Verständnis von Sequenzen und Zustandsabfolgen.",

    DIFFICULTY_CHALLENGING:
        "Auf diesem Niveau wird analytisches Denken und ein tiefgreifendes Verständnis der Konzepte verlangt. "
        "Die Lösung umfasst 12-18 Zustände und erfordert die Arbeit mit verschachtelten logischen Strukturen und anspruchsvolleren Übergangsbedingungen. "
        "Die Aufgaben können komplexere Operationen wie das Verarbeiten und Überprüfen von Eingabesequenzen umfassen, bleiben jedoch mit einer Standard-Turingmaschine lösbar.",

    DIFFICULTY_ADVANCED:
        "Diese Aufgaben verlangen ein umfassendes Verständnis und die Fähigkeit, anspruchsvolle Abläufe präzise umzusetzen. "
        "Die Lösung umfasst 18-24 Zustände und erfordert den kreativen Einsatz von Bandoperationen und gut geplante Zustandsübergänge. "
        "Die Aufgaben decken Szenarien ab, die eine klare Strategie und eine strukturierte Lösung verlangen, ohne jedoch über die Fähigkeiten einer Standard-Turingmaschine hinauszugehen.",

    DIFFICULTY_EXTREME:
        "Auf diesem Schwierigkeitsniveau werden die Grenzen des Verständnisses der Turingmaschine getestet. "
        "Die Lösung erfordert mehr als 24 Zustände und beinhaltet komplexe Übergangssysteme, die sorgfältig auf mehrere Schritte und Bandbereiche abgestimmt sind. "
        "Diese Aufgaben stellen Extremsituationen dar und verlangen präzise Planung, strategisches Denken und die Berücksichtigung von Grenzfällen. "
        "Sie bleiben lösbar, fordern jedoch das Maximum an analytischem Denken und Problemlösungsfähigkeit."
}

VALIDATION_MESSAGE_RESULT_PREFIX = "**HIER SIND DIE ZU OPTIMIERENDEN AUFGABEN:**\n\n"