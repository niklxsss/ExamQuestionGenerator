class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, task_type, files_txt, files_images, files_pdf):

        prompt = PromptBuilder.getBasePrompt(num_questions)

        if task_type:
            prompt += "\n\n" + PromptBuilder.get_faulty_task_prompt()

        if difficulty:
            prompt += "\n\n" + PromptBuilder.get_difficulty_prompt()

        attachment_prompt = ""
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_txt)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_pdf)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Bild-Datei", files_images)

        if attachment_prompt.strip():
            attachment_prompt_prefix = "\n\nZusätzliche Informationen zu den Aufgaben:\n\n"
            prompt += attachment_prompt_prefix + attachment_prompt

        prompt += PromptBuilder.get_general_guidelines()
        prompt += PromptBuilder.get_structure_instructions()

        return prompt

    @staticmethod
    def getBasePrompt(num_questions):
        return (
            f"Sie sind KI-Lehrassistent mit Schwerpunkt Informatik. Generieren Sie genau {num_questions} "
            f"anspruchsvolle, anwendungsbezogene Prüfungsaufgaben zu Turingmaschinen!"
        )

    @staticmethod
    def get_task_type_prompt(task_type):
        if task_type == "incorrect_tasks":
            return PromptBuilder.get_faulty_task_prompt()

        return f"Erstellen Sie Aufgaben des Typs: {task_type}. Stellen Sie sicher, dass die Aufgaben für diesen Typ geeignet sind."

    @staticmethod
    def get_difficulty_prompt(difficulty):
        return (f"Erstelle die Fragen mit der Schwierigkeitsstufe {difficulty} und stelle sicher, "
                f"dass eine merkbare Veränderung der Schwierigkeit, aufgrund der gewählten Schwierigkeitsstufe "
                f"{difficulty} stattfindet und sich in den ausgegebenen Fragen widerspiegelt.\n\n"
        )

    @staticmethod
    def get_attachment_prompt(datei_name, files):
        if files:
            return f"Die angehängte(n) {datei_name} enthalten zusätzliche Inhalte zur Turingmaschine. " \
                   f"Nutzen Sie diese Inhalte, um die Übungen entsprechend zu gestalten.\n\n"
        return ""

    @staticmethod
    def get_general_guidelines():
        return (
            "Alle Inhalte sollen auf Deutsch verfasst werden. "
            "Stellen Sie sicher, dass die Aufgaben und Lösungen korrekt und präzise sind. "
            "Vermeiden Sie Unklarheiten und stellen Sie sicher, dass die Aufgaben insich schlüssig und volltsändig sind!"
        )

    @staticmethod
    def get_structure_instructions():
        return (
            "Die Prüfungsaufgaben und Lösungen sollen im übergebenen `ExamQuestions`-Response-Format strukturiert "
            "sein, welches wie folgt aufgebaut ist:\n\n"

            "Bitte halten Sie sich streng an dieses Format und verwenden Sie optionale Felder nur dann, wenn sie für die "
            "Klarheit oder das Verständnis der spezifischen Aufgabe hilfreich sind. Tabellen sollten verwendet werden, wenn sie "
            "die Darstellung komplexer oder strukturierter Daten, wie zum Beispiel von Zustandsübergängen, erleichtern.\n\n"

            "Format der Aufgabe:\n"

            "- question_content:\n"
            "  - question (str): Die eigentliche Frage der Aufgabe. Dieser Wert ist immer erforderlich.\n"
            "  - additional_infos (optional, List[str]): Zusätzliche Informationen zur Frage, nur verwenden, wenn "
            "    für das Verständnis notwendig.\n"
            "  - tables (optional, List[TableContent]): Verwenden Sie Tabellen ausschließlich, wenn sie für die "
            "    Darstellung der Frageinhalte relevant und hilfreich sind. Die Tabellenstruktur ist wie folgt:\n"
            "    - title (str): Ein Titel für die Tabelle.\n"
            "    - headers (List[str]): Die Überschriften der Spalten.\n"
            "    - rows (List[List[str]]): Zeilen mit den Daten für jede Spalte, passend zu den Überschriften.\n\n"
            "    - Die Tabellen in der Aufgabenstellung sind primär für den Aufgabentyp 'incorrect_tasks' vorgesehen, bei anderen Aufgaben finden diese nur selten anwendung."

            "- example (optional, str): Ein Beispiel zur Frage, falls erforderlich.\n\n"

            "- solution_content:\n"
            "  - solution (str): Die Lösung zur Aufgabe. Dieser Wert ist immer erforderlich.\n"
            "  - additional_solution_infos (optional, List[str]): Weitere hilfreiche Hinweise oder Erläuterungen zur "
            "    Lösung, nur falls benötigt.\n"
            "  - step_by_step_solution (optional, List[str]): Eine Schritt-für-Schritt-Anleitung zur Lösung, falls "
            "    eine detaillierte Erläuterung erforderlich ist. Es sollte keine Nummerierung mitgegeben werden.\n"
            "  - tables (optional, List[TableContent]): Tabellen nur verwenden, wenn eine tabellarische Darstellung der "
            "    Lösung den Informationsfluss klarer macht. Dies gilt insbesondere für technische Aufgaben mit "
            "    komplexen Abläufen, wie Zustandsübergängen in Turingmaschinen. Die Struktur ist wie folgt:\n"
            "    - title (str): Ein Titel für die Tabelle.\n"
            "    - headers (List[str]): Die Überschriften der Spalten.\n"
            "    - rows (List[List[str]]): Zeilen mit den Daten für jede Spalte, die den Überschriften korrekt zugeordnet sind.\n\n"

            "Verwenden Sie die optionalen Felder nur dann, wenn sie für die Klarheit der Aufgabe oder Lösung "
            "erforderlich sind. Eine Aufgabe kann minimal auch nur die Frage und die Lösung beinhalten. Falls Tabellen verwendet "
            "werden, achten Sie bitte darauf, dass sie ausschließlich für strukturierte und komplexe Informationen genutzt werden, "
            "und dass alle Inhalte vollständig und korrekt zugeordnet sind.\n\n"

            "Bitte verwenden Sie Tabellen in der Frage nur dann, wenn dies zur vollständigen Darstellung der Aufgabe "
            "unbedingt erforderlich ist, wie z.B.eine Zustandsübergangstabelle.Andernfalls sollen Tabellen in der Lösung "
            "verwendet werden, um die Schritte oder Zustände detailliert zu beschreiben, wenn diese für die Erklärung "
            "nützlich sind.\n\n"

            "Gebe NICHT schon in der Aufgabenstellung die Lösung in form einer TAbelle oder ähnlichem an!!!.\n\n"



        )

    @staticmethod
    def get_faulty_task_prompt():
        return (
            "Zusätzlicher Auftrag:\n "
            "Generieren Sie nur Aufgaben mit fehlerhaften Turingmaschinen. Der Zweck dieser Aufgaben "
            "ist es, das Fehlersuch- und Korrekturvermögen von Studierenden gezielt zu überprüfen.\n\n"

            "Aufgabentyp:\n"
            "- Die Turingmaschine soll absichtlich einen oder mehrere Fehler enthalten, die den gewünschten Output "
            "verhindern oder zu einem falschen Output führen.\n"
            "- Diese Fehler sollen so gestaltet sein, dass Studierende durch sorgfältige Analyse der Zustände und "
            "Übergänge in der Lage sein müssen, die Ursache der Fehlfunktion zu identifizieren und zu korrigieren.\n\n"

            "Vorgaben für die Fehlerstruktur:\n"
            "- Fehler können in den Zustandsübergängen, Lese- und Schreibaktionen oder in der Bandpositionierung "
            "auftreten.\n"
            "- Die Fehler sollen so eingebaut sein, dass sie plausibel und nicht offensichtlich sind, um eine "
            "Herausforderung für Studierende zu bieten.\n\n"

            "Lernziel:\n"
            "- Die Aufgaben sollen den Studierenden helfen, ein tiefgehendes Verständnis der Funktionsweise von "
            "Turingmaschinen zu entwickeln, indem sie Fehler diagnostizieren und beheben.\n\n"

            "Beachten Sie:\n"
            "- Geben Sie klare Hinweise oder Erklärungen, wie der Studierende den Fehler identifizieren kann, falls "
            "zusätzliche Informationen erforderlich sind.\n"
            "- Optional können Tabellen verwendet werden, um die fehlerhafte Zustandstabelle zu visualisieren. "
            "Stellen Sie sicher, dass die Inhalte in den Spalten vollständig und korrekt strukturiert sind, ohne "
            "Verschiebungen zwischen den Einträgen.\n"
            "- Verwenden Sie keine nummerierte Liste für Schrittfolgen, um zusätzliche Struktur in den Anweisungen "
            "bereitzustellen.\n\n"

            "Generieren Sie die Aufgaben und Lösungen im zuvor beschriebenen Format."
        )






# Format definieren
# Nutzung des Formates
#Bei aufzählungen keine nummern angeben
