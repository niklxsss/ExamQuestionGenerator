class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, task_type, files_txt, files_images, files_pdf):
        prompt = PromptBuilder.get_base_prompt(num_questions)

        if task_type:
            prompt += PromptBuilder.get_task_type_prompt(task_type)

        if difficulty:
            prompt += PromptBuilder.get_difficulty_prompt(difficulty)

        if any([files_txt, files_images, files_pdf]):
            prompt += PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf)

        prompt += PromptBuilder.get_structure_instructions()
        prompt += PromptBuilder.get_general_guidelines()
        prompt += PromptBuilder.get_final_reminder()

        return prompt


    @staticmethod
    def get_base_prompt(num_questions):
        return (
            f"Sie sind KI-Lehrassistent mit Schwerpunkt Informatik. Generieren Sie genau **{num_questions}** "
            f"anspruchvoll Prüfungsaufgaben zu Turingmaschinen. Die Aufgaben sollen speziell "
            f"für Studierende im Bereich Informatik konzipiert sein und deren Verständnis sowie die "
            f"Anwendungskompetenz der Konzepte prüfen.\n\n"
        )

    @staticmethod
    def get_difficulty_prompt(difficulty):
        return (
            f"Erstelle die Aufgaben mit der Schwierigkeitsstufe **{difficulty.upper()}** und stelle sicher, "
            f"dass eine merkbare Veränderung der Schwierigkeit, aufgrund der gewählten Schwierigkeitsstufe "
            f"**{difficulty.upper()}** stattfindet und sich in den ausgegebenen Fragen widerspiegelt!"
            f"Die Schwierigkeitsstufen umfassen 'leicht', 'mittel' und 'schwer'.\n\n"
        )

    @staticmethod
    def get_attachments_prompt(files_txt, files_images, files_pdf):
        attachment_prompt = ""
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_txt)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Info-Text", files_pdf)
        attachment_prompt += PromptBuilder.get_attachment_prompt("Bild-Datei", files_images)
        attachment_prompt_prefix = "Zusätzliche Informationen zu den Aufgaben:\n\n"
        return attachment_prompt_prefix + attachment_prompt

    @staticmethod
    def get_attachment_prompt(datei_name, files):
        if files:
            return f"Die angehängte(n) {datei_name} enthalten zusätzliche Inhalte zur Turingmaschine. " \
                   f"Nutzen Sie diese Inhalte, um die Aufgaben entsprechend zu gestalten.\n\n"
        return ""

    @staticmethod
    def get_general_guidelines():
        return (
            "### Grundlegende Anforderungen:\n\n"
            "-Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "-Stellen Sie sicher, dass die Aufgaben und Lösungen korrekt und präzise sind.\n"
            "-Vermeiden Sie Unklarheiten und stellen Sie sicher, dass die Aufgaben insich schlüssig und volltsändig "
            "sind!\n"
            "- Die Aufgabenstellung muss klar und eindeutig formuliert sein, damit Studierende wissen, was genau von "
            "ihnen erwartet wird.\n"
            "- Achten Sie darauf, dass die Lösung sich direkt mit den Anforderungen der Aufgabenstellung deckt und die "
            "erwarteten Schritte oder Ergebnisse nachvollziehbar aufzeigt.\n\n"
        )

    @staticmethod
    def get_structure_instructions():

        general_instructions = (
            "Die Prüfungsaufgaben und Lösungen sollen im übergebenen `ExamQuestions`-Response-Format strukturiert "
            "sein. Dieses Format enthält alle relevanten Felder und muss exakt eingehalten werden. Verwenden Sie "
            "optionale Felder nur, wenn sie zur Klarheit und Präzision der Aufgabe beitragen.\n\n"
        )

        structure_overview = (
            "### `ExamQuestions` Format Übersicht:\n"

            "`ExamQuestions` besteht aus einer Liste von Prüfungsfragen (`questions`). "
            "Jede Prüfungsfrage ist vom Typ `ExamQuestion` und umfasst:\n\n"

            "1. **question_content** (erforderlich): "
            "Enthält die eigentliche Frage sowie zusätzliche optionale Informationen.\n"

            "2. **optional_example** (optional): "
            "Ein Beispiel zur Frage, falls relevant.\n"

            "3. **solution_content** (erforderlich): "
            "Enthält die Lösung sowie zusätzliche optionale Details zur Lösung.\n\n"
        )

        question_content_details = (
            "#### Struktur von `question_content`:\n"

            "- **question (str)**: "
            "Die Hauptfrage, die immer erforderlich ist.\n"

            "- **optional_question_additional_infos (List[str], optional)**: "
            "Zusätzliche Informationen zur Frage. Verwenden Sie dieses Feld nur, wenn es das Verständnis der Aufgabe "
            "erleichtert.\n"

            "- **optional_question_tables (List[TableContent], optional)**: "
            "Tabellen zur Darstellung relevanter Informationen. Diese sollten nur eingesetzt werden, wenn die "
            "Darstellung komplexer Daten in der Fragestellng sinnvoll ist. "
            "Die Tabellenstruktur ist wie folgt:\n "

            "  - **title (str)**: Titel der Tabelle.\n"
            "  - **headers (List[str])**: Spaltenüberschriften der Tabelle.\n"
            "  - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
        )

        example_details = (
            "#### `optional_example`:\n"
            "- **optional_example (str, optional)**: Ein Beispiel zur Frage, nur verwenden, wenn es für das "
            "Verständnis hilfreich ist. Achte darauf, dass Beispiele nicht mehrfach dargstellt werden!\n\n"
        )

        solution_content_details = (
            "#### Struktur von `solution_content`:\n"

            "- **solution (str)**: Die Hauptlösung, die immer erforderlich ist.\n"

            "- **optional_solution_additional_infos (List[str], optional)**: Zusätzliche Hinweise zur Lösung. "
            "Nur verwenden, wenn diese für das Verständnis der Lösung nötig sind.\n"

            "- **optional_solution_step_by_step (List[str], optional)**: Schritt-für-Schritt-Erklärung der Lösung. "
            "Verwenden Sie keine Nummerierung, da diese automatisch hinzugefügt wird.\n"

            "- **optional_solution_tables (List[TableContent], optional)**: Tabellen zur Unterstützung der Lösung, "
            "z.B. für komplexe Abläufe oder Zustandsübergänge. Die Struktur entspricht der folgenden:\n"

            "  - **title (str)**: Titel der Tabelle.\n"
            "  - **headers (List[str])**: Spaltenüberschriften der Tabelle.\n"
            "  - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
        )

        additional_guidelines = (
            "#### Zusätzliche Hinweise zur Formatnutzung:\n"

            "- Verwenden Sie optionale Felder ausschließlich, wenn sie die Aufgabe oder Lösung klarer und "
            "verständlicher machen. Eine minimale Aufgabe besteht aus einer `question` und einer `solution`.\n"

            "- Tabellen in der Frage sollten nur für komplexe Aufgabentypen wie bspw. 'incorrect_tasks' verwendet "
            "werden, bei diesen die Darstellung zusätzlicher Daten erforderlich ist. Ansonsten sind Tabellen in der "
            "Lösung für die Erklärung technischer Abläufe wie Zustandsübergänge in Turingmaschinen nützlich.\n"

            "- Achten Sie darauf, dass Tabellen nicht bereits Teile der Lösung in der Aufgabenstellung enthalten "
            "und dass die Zuordnung der Daten in den Spalten und Zeilen immer korrekt ist.\n"

            "- Geben Sie keine Lösungselemente bereits in der Aufgabenstellung an und vermeiden Sie unbedingt die "
            "Wiederholung von Informationen.\n\n"
        )

        return (
                general_instructions +
                structure_overview +
                question_content_details +
                example_details +
                solution_content_details +
                additional_guidelines
        )

    @staticmethod
    def get_task_type_prompt(task_type):
        if task_type == "incorrect_tasks":
            return PromptBuilder.get_faulty_task_prompt()

        return (
            f"Erstellen Sie Aufgaben des Typs: **{task_type.upper()}**. "
            f"Stellen Sie sicher, dass die generierten Aufgaben diesem Typ entsprechen.\n\n"
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
            "Verschiebungen zwischen den Einträgen.\n\n"

            "Generieren Sie die Aufgaben und Lösungen im zuvor beschriebenen Format!!!\n\n"
        )

    @staticmethod
    def get_final_reminder():
        return (
            "\n\n**Wichtiger abschließender Hinweis:**\n\n"

            "Es ist absolut essenziell, dass **keine Elemente der Lösung bereits in der Aufgabenstellung** enthalten "
            "sind. Achten Sie besonders darauf, dass **Tabellen ausschließlich in der Lösung** und **nicht in der "
            "Aufgabenstellung** verwendet werden, es sei denn, dies macht aufgrund der Aufgabenstellung Sinn und "
            "ist essenziell. Die Zuordnung der Inhalte innerhalb der Tabellen in der Lösung muss **stets korrekt** zu "
            "den Spaltenüberschriften und Zeilen erfolgen. Stellen Sie sicher, dass keine Tabellen versehentlich "
            "doppelt oder unvollständig verwendet werden.\n\n"

            "Bei der internen Generierung der Aufgaben ist besonders darauf zu achten, dass das **Mapping von "
            "Tabellen** sorgfältig geprüft wird, damit Tabellen wirklich nur an den vorgesehenen Stellen erscheinen. "
            "Es darf **keine Lösungstabelle aufgrund eines Mapping-Fehlers** in der Aufgabenstellung auftauchen. "
            "Vergewissern Sie sich, dass jede Tabelle **ausschließlich dort platziert wird**, wo sie inhaltlich "
            "sinnvoll ist und den Anforderungen entspricht.\n\n"

            "Jegliche Missachtung dieser Anweisung führt zu falschen und verwirrenden Aufgabenstellungen und soll "
            "daher strikt vermieden werden!!! Diese Regeln sind für die Klarheit der Aufgabenstruktur entscheidend "
            "und müssen beachtet werden!!!"
        )