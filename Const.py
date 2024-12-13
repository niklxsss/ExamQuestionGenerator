GPT_MODEL = "gpt-4o"
MAX_TOKENS = 8000
TASK_GENERATION_TEMPERATURE = 0.7
STATE_TRANSITION_TEMPERATURE = 0.4
EXAMPLE_FLOW_TEMPERATURE = 0.3
SOLUTION_TEMPERATURE = 0.5
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
DIFFICULTY_HARD = 'hard'

DIFFICULTY_TRANSLATION_MAP = {
    DIFFICULTY_EASY: 'leicht',
    DIFFICULTY_MEDIUM: 'mittel',
    DIFFICULTY_HARD: 'schwer'
}

DIFFICULTY_EXPLANATION_MAP = {

    DIFFICULTY_EASY:
        (
            "Aufgaben auf diesem Niveau sollen sich auf die grundlegendsten Mechanismen von Turingmaschinen beschränken.\n"
            "- Es dürfen keine Schleifen, Bedingungen oder komplexe Logik enthalten sein.\n"
            "- Die Aufgaben müssen mit einer minimalen Anzahl an Zuständen lösbar sein.\n"
            "- Die Bandbewegung darf sich nur in eine Richtung vollziehen (kein Wechsel der Bewegungsrichtung).\n"
            "- Keine zusätzlichen logischen Operationen wie Überträge oder Berechnungen sind erlaubt.\n"
            "- Ziel ist es, einfache Konzepte wie Schreiben eines Zeichens oder Bewegen des Kopfes zu verdeutlichen.\n"
            "- Validieren Sie, dass die Aufgaben so einfach wie möglich gestaltet sind und der Zielgruppe von Einsteigern entsprechen.\n"
            "**Prüfen Sie sorgfältig, ob die Aufgabe den Kriterien entspricht, bevor Sie fortfahren.**\n\n"
        ),

    DIFFICULTY_MEDIUM:
        (
            "Aufgaben auf diesem Niveau sollen ein solides Verständnis der Turingmaschine vertiefen und grundlegende Herausforderungen einführen.\n"
            "- Die Aufgaben können  einfache Verzweigungen und kontrollierte Schleifen, die logisch und klar strukturiert sind.\n"
            "- Zustandsübergänge bleiben überschaubar und klar nachvollziehbar, wobei unnötige Komplexität vermieden wird.\n"
            "- Der Bandkopf kann sich in beide Richtungen bewegen, jedoch nur, wenn dies für die Erfüllung der Aufgabe notwendig ist.\n"
            "- Alle Übergänge müssen klar definiert und auf wenige, eng miteinander verknüpfte Zustände begrenzt sein.\n"
            "- Das Ziel ist es, die Fähigkeit der Teilnehmenden zu fördern, einfache Logiken und Bedingungen korrekt umzusetzen, ohne sie zu überfordern.\n"
            "**Prüfen Sie sorgfältig, ob die Aufgabe wirklich nur moderate Herausforderungen bietet und die Komplexität nicht unnötig gesteigert wird!**\n\n"
        ),

    DIFFICULTY_HARD:
        (
            "Aufgaben auf diesem Niveau sollen anspruchsvolle Szenarien darstellen, die ein tiefgehendes Verständnis der Turingmaschine und hohe Problemlösefähigkeiten erfordern.\n"
            "- Die Zustandsübergänge sind komplex und können mehrere Bedingungen, verschachtelte Schleifen sowie dynamische Richtungswechsel umfassen.\n"
            "- Die Aufgaben können längere Sequenzen mit mehreren Zwischenzielen und Zustandsgruppen umfassen, die zur Lösung erforderlich sind.\n"
            "- Der Fokus liegt auf strategischem Denken, indem die Teilnehmenden vielschichtige Abläufe analysieren und effizient umsetzen müssen.\n"
            "- Es müssen Grenzfälle und Sonderbedingungen berücksichtigt werden, um die Funktion der Maschine in allen Szenarien sicherzustellen.\n"
            "- Das Ziel ist es, Aufgaben zu erstellen, die die Herausforderungen der Turingmaschine demonstrieren und die Studierenden an die Grenzen ihres Verständnisses bringen.\n"
            "**Vergewissern Sie sich, dass die Aufgabe wirklich anspruchsvoll ist und die Komplexität angemessen erhöht wurde, ohne unlösbar zu sein.**\n\n"
        )

}

VALIDATION_MESSAGE_RESULT_PREFIX = "**HIER IST DIE ZU KORRIGIERENDE AUFGABE: **\n\n"

