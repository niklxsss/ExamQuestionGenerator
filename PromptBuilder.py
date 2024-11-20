from Const import *


class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, task_type, files_txt, files_images, files_pdf):
        prompt_parts = [PromptBuilder.get_base_prompt(num_questions, DIFFICULTY_WORDING_MAP.get(difficulty),
                                                      DIFFICULTY_EXPLANATION_MAP.get(difficulty))]
        if task_type:
            prompt_parts.append(PromptBuilder.get_task_type_prompt(task_type))

        if any([files_txt, files_images, files_pdf]):
            prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))

        prompt_parts.append(PromptBuilder.get_general_guidelines())
        prompt_parts.append(PromptBuilder.get_process_steps())
        prompt_parts.append(PromptBuilder.get_structure_instructions())
        prompt_parts.append(PromptBuilder.get_final_reminder())

        return prompt_parts

    @staticmethod
    def get_base_prompt(num_questions, difficulty, difficulty_explanation):
        return (
            "# Aufgabenbeschreibung und Zielsetzung:\n\n"
            
            f"Sie sind KI-Lehrassistent mit Schwerpunkt Informatik. Generieren Sie genau **{num_questions}** "
            f"{difficulty} Prüfungsaufgaben zu Turingmaschinen. Die Aufgaben sollen speziell "
            f"für Studierende im Bereich Informatik konzipiert sein und deren Verständnis sowie die "
            f"Anwendungskompetenz der Konzepte prüfen\n. {difficulty_explanation}\n"
            f"Die generierten Aufgaben werden direkt für Prüfungszwecke verwendet und müssen daher höchsten Ansprüchen "
            f"an Richtigkeit, Vollständigkeit und Konsistenz genügen. Jede Aufgabe muss realistisch und fehlerfrei "
            f"mit einer Standard-Turingmaschine umsetzbar sein.\n\n"

        )

    @staticmethod
    def get_process_steps():
        return (
             "# Ablauf der Prüfungsfrage-Generierung:\n\n"
             
            "1. Wählen Sie die Art der Aufgabe, falls nicht vorgegeben, und stellen Sie sicher, dass die "
            "Aufgabenstellung vollständig, präzise und klar ist. Zudem müssen die Aufgaben auf realistisch umsetzbaren "
            "Operationen einer Turingmaschine basieren\n. "
            "2. Identifizieren Sie die gewählte Schwierigkeitsstufe: leicht, moderat oder anspruchsvoll. "
            "Verifizieren Sie, dass die Aufgabenstellung der Schwierigkeitsstufe entspricht.\n"
            "3. Stellen Sie sicher, dass die Aufgaben auf der gewählten Schwierigkeitsstufe realistisch und umsetzbar "
            "sind. Vermeiden Sie plötzliche Sprünge in der Komplexität innerhalb derselben Schwierigkeitsstufe.\n"
            "4. Halten Sie die Komplexität der Aufgaben immer auf einem Niveau, sodass die Richtigkeit und gegebene "
            "Funktion garantiert werden können.\n"
            "5. Generieren Sie ein Beispiel nur, wenn es die Lösung verdeutlicht, und stellen Sie sicher, dass es "
            "korrekt ist.\n"
            "6. Formulieren Sie eine klare und vollständige Lösung, die genau zur Aufgabenstellung passt und alle "
            "Schritte nachvollziehbar erklärt.\n"
            "7. Generieren Sie eine Zustandsübergangstabelle (falls erforderlich) und stellen Sie sicher, dass sie "
            "**KOMPLETT VOLLSTÄNDIG** ist und keine Zustände oder Übergänge fehlen.\n"
            "8. Überprüfen Sie am Ende, dass **alle Übergänge in den Zustandstabellen vollständig und klar "
            "beschrieben** sind. **Unvollständige Übergänge oder Zustände, die in der Beschreibung erwähnt, aber "
            "in der Tabelle fehlen, sind **streng zu vermeiden** und gefährden die Prüfungsqualität.\n"
            "9. Validieren Sie jede Aufgabe anhand mehrerer gedanklichen Tests und stellen Sie sicher, dass die Lösung "
            "vollständig mit der Aufgabenstellung übereinstimmt und umsetzbar ist. Überprüfen Sie akribisch, "
            "dass alle Zustandsübergänge vollständig sind und jede mögliche Eingabe eindeutig behandelt wird. "
            "Zustände ohne definierte Übergänge dürfen in der Zustandsübergangstabelle nicht vorkommen, da dies "
            "zu fehlerhaften Ergebnissen führt. Unvollständige Übergangstabellen sind unbrauchbar und für "
            "Prüfungsaufgaben unzulässig.\n"
            "10. Fügen Sie, falls sinnvoll, eine oder mehrere **Beispielablauftabellen** am Ende der Lösung hinzu, "
            "um die Schritte nachvollziehbar zu machen und die Lösung zu validieren.\n"
            "11. Simulieren Sie jede generierte Aufgabe nochmals, bevor sie als korrekt betrachtet wird. Prüfen Sie Schritt für "
            "Schritt, ob die Zustandsübergänge korrekt funktionieren und die Maschine das erwartete Ergebnis liefert. "
            "Fehlerhafte Ergebnisse oder Endlosschleifen müssen vor der Ausgabe behoben werden.\n\n"

        )

    @staticmethod
    def get_attachments_prompt(files_txt, files_images, files_pdf):
        attachments = ""
        attachments += PromptBuilder.get_attachment_prompt("Text", files_txt)
        attachments += PromptBuilder.get_attachment_prompt("PDF", files_pdf)
        attachments += PromptBuilder.get_attachment_prompt("Bild", files_images)
        return f"# Zusätzliche Informationen:\n\n{attachments}"


    @staticmethod
    def get_attachment_prompt(datei_name, files):
        if files:
            return f"Die angehängte {datei_name} enthält zusätzliche Inhalte zur Turingmaschine. " \
                   f"Nutzen Sie diese Inhalte, um die Aufgaben entsprechend zu gestalten.\n\n"
        return ""

    @staticmethod
    def get_general_guidelines():
        return (
            "# Grundlegende Anforderungen:\n\n"
            
            "- Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "- Stellen Sie sicher, dass die Aufgaben und Lösungen korrekt und präzise sind.\n"
            "- Vermeiden Sie Unklarheiten und stellen Sie sicher, dass die Aufgaben in sich schlüssig und vollständig "
            "sind.\n"
            "- Die Aufgabenstellung muss klar und eindeutig formuliert sein, damit Studierende wissen, was genau von "
            "ihnen erwartet wird.\n"
            "- Achten Sie darauf, dass die Lösung sich direkt mit den Anforderungen der Aufgabenstellung deckt und die "
            "erwarteten Schritte oder Ergebnisse nachvollziehbar aufzeigt.\n"
            "- **Alphabet-Angabe**: Geben Sie sobald es die Aufgabenstellung erfordert, das verwendete Alphabet in "
            "den Zusatzinformationen der Aufgabenstellung an (z.B. {0, 1, ⋄}), damit klar ist, welche Symbole die "
            "Maschine bearbeiten kann.\n"
            "- **Bewegungsrichtung und Bandbegrenzung**: Beschreiben Sie klar, wie sich die Turingmaschine über "
            "das Band bewegt (z.B. von links nach rechts) und wo die Maschine am Ende der Ausführung stehen bleiben "
            "soll, falls es für die Lösung erforderlich ist. Diese Informationen sollten ebenfalls in den "
            "zusätzlichen Informationen der Aufgabenstellung enthalten sein, um das Verständnis der Anforderungen "
            "zu erleichtern.\n"
            "- **Zustandsübergangstabellen**: Falls erforderlich, stellen Sie sicher, dass die Übergangstabellen alle "
            "möglichen Zustände und Übergänge abdecken (einschließlich Anfangs- und Endzuständen). "
            "**Unvollständige Tabellen oder fehlende Zustände gefährden die Qualität und Umsetzbarkeit der Aufgabe.**\n"
            "- Achten Sie darauf, dass die Aufgabenstellung klar formuliert ist und dass sie den Fähigkeiten und "
            "Einschränkungen einer Turingmaschine entspricht. Jede Aufgabe sollte mit einer Standard-Turingmaschine "
            "realisierbar sein und keine zusätzlichen Speicher- oder Zählmechanismen voraussetzen, die über den "
            "Rahmen einer einbandigen Turingmaschine hinausgehen.\n"
            "- Vermeiden Sie komplexe Berechnungen oder Operationen, die in einer Standard-Turingmaschine nicht "
            "durchführbar sind. Prüfen Sie, dass alle Schritte auf eine realistische Weise auf eine Turingmaschine "
            "übertragbar sind.\n"
            "Halten Sie die Komplexität der Aufgaben auf dem übergebenen SchwierigkeitsNiveau und vermeiden Sie "
            "starke Schwankungen.\n"
            "- **Testfall-Validierung**: Stellen Sie sicher, dass jede generierte Aufgabe mit einem Standard-Testfall "
            "geprüft wird, um die Konsistenz und Korrektheit der Lösung zu gewährleisten.\n"
            "- Fehlerhafte oder unvollständige Aufgaben sind für den Einsatz in Prüfungen nicht akzeptabel. Stellen "
            "Sie sicher, dass jede Aufgabe korrekt, vollständig und logisch konsistent ist. Alle Lösungen müssen "
            "Schritt für Schritt nachvollziehbar sein und dürfen keine Lücken enthalten.\n\n"
        )

    @staticmethod
    def get_structure_instructions():
        header = "# Struktur der Prüfungsaufgaben und Lösungen:\n\n"

        general_instructions = (
            "Die Prüfungsaufgaben und Lösungen sollen im `ExamQuestions`-Response-Format strukturiert sein. "
            "Verwenden Sie optionale Felder nur, wenn sie zur Klarheit und Präzision der Aufgabe beitragen.\n\n"
        )

        structure_overview = (
            "## `ExamQuestions` Format Übersicht:\n"

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
            "### Struktur von `question_content`:\n"

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
            "### `optional_example`:\n"
            "- **optional_example (str, optional)**: Generieren Sie ein Beispiel nur, wenn es zur Klarheit der "
            "Aufgabenstellung beiträgt und das erwartete Verhalten der Lösung deutlich darstellt. "
            "Falls ein Beispiel enthalten ist, muss es die Anforderungen der Aufgabenstellung exakt erfüllen "
            "und das korrekte Ergebnis zeigen.Achte darauf, dass Beispiele nicht mehrfach dargstellt werden!\n"

            "Falls ein Beispiel enthalten ist, überprüfen Sie es darauf, dass es die Aufgabenanforderungen "
            "vollständig erfüllt und die Lösung exakt abbildet. Das Beispiel sollte keine abweichenden oder "
            "unvollständigen Ergebnisse enthalten.\n\n"
        )

        solution_content_details = (
            "### Struktur von `solution_content`:\n"

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
            "### Zusätzliche Hinweise zur Formatnutzung:\n"

            "- Verwenden Sie optionale Felder ausschließlich, wenn sie die Aufgabe oder Lösung klarer und "
            "verständlicher machen. Eine minimale Aufgabe besteht aus einer `question` und einer `solution`.\n"

            "- Tabellen in der Frage sollten nur für komplexe Aufgabentypen wie bspw. 'incorrect_tasks' verwendet "
            "werden, bei diesen die Darstellung zusätzlicher Daten erforderlich ist. Ansonsten sind Tabellen in der "
            "Lösung für die Erklärung technischer Abläufe wie Zustandsübergänge in Turingmaschinen nützlich.\n"

            "-Stellen Sie sicher, dass die Lösung für jede Aufgabe vollständig und korrekt ist. Falls die Lösung eine "
            "Zustandsübergangstabelle erfordert, soll die unbedingt vollständige sein und alle Zustände, Eingaben "
            "und Übergänge beschreiben. Es dürfen keine Lücken in der Zustandslogik bestehen. Jede Tabelle sollte so "
            "gestaltet sein, dass sie die Zustandsübergänge bis zum Endzustand vollständig darstellt.\n"

            "- Achten Sie darauf, dass Tabellen nicht bereits Teile der Lösung in der Aufgabenstellung enthalten "
            "und dass die Zuordnung der Daten in den Spalten und Zeilen immer korrekt ist.\n"

            "- Geben Sie keine Lösungselemente bereits in der Aufgabenstellung an und vermeiden Sie unbedingt die "
            "Wiederholung von Informationen.\n\n"
        )

        return (
                header +
                general_instructions +
                structure_overview +
                question_content_details +
                example_details +
                solution_content_details +
                additional_guidelines
        )

    @staticmethod
    def get_task_type_prompt(task_type):
        if task_type == TASK_TYPE_INCORRECT_TASK:
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

            "Beachten Sie:\n"
            "- Geben Sie klare Hinweise oder Erklärungen, wie der Studierende den Fehler identifizieren kann, falls "
            "zusätzliche Informationen erforderlich sind.\n"
            "- Optional können Tabellen verwendet werden, um die fehlerhafte Zustandstabelle zu visualisieren. "
            "Stellen Sie sicher, dass die Inhalte in den Spalten vollständig und korrekt strukturiert sind, ohne "
            "Verschiebungen zwischen den Einträgen.\n\n"

            "Generieren Sie die Aufgaben und Lösungen im beschriebenen Format!!!\n\n"
        )

    @staticmethod
    def get_final_reminder():
        return (
            "# Wichtiger abschließender Hinweis:\n\n"

            "- Überprüfen Sie jede Aufgabe auf Konsistenz mit der angegebenen Schwierigkeitsstufe.\n"

            "- Stellen Sie sicher, dass keine Aufgabe die Komplexität der gewählten Schwierigkeitsstufe "
            "überschreitet.\n"

            "- Es ist absolut essenziell, dass **keine Elemente der Lösung bereits in der Aufgabenstellung** enthalten "
            "sind. Achten Sie besonders darauf, dass **Tabellen ausschließlich in der Lösung** und **nicht in der "
            "Aufgabenstellung** verwendet werden, es sei denn, dies macht aufgrund der Aufgabenstellung Sinn.\n"
            "Die Zuordnung der Inhalte innerhalb der Tabellen in der Lösung muss **stets korrekt** zu "
            "den Spaltenüberschriften und Zeilen erfolgen. Stellen Sie sicher, dass keine Tabellen versehentlich "
            "doppelt oder unvollständig verwendet werden.\n\n"

            "- Bei der internen Generierung der Aufgaben ist besonders darauf zu achten, dass das **Mapping von "
            "Tabellen** sorgfältig geprüft wird, damit Tabellen wirklich nur an den vorgesehenen Stellen erscheinen. "
            "Es darf **keine Lösungstabelle aufgrund eines Mapping-Fehlers** in der Aufgabenstellung auftauchen. "
            "Vergewissern Sie sich, dass jede Tabelle **ausschließlich dort platziert wird**, wo sie inhaltlich "
            "sinnvoll ist und den Anforderungen entspricht.\n\n"

            "- Validieren Sie jede Aufgabe mit mehreren gedanklichen Tests oder Standard-Testfällen, bevor Sie die nächste "
            "Aufgabe generieren. Die Validierung muss sicherstellen, dass die Übergangstabellen vollständig und korrekt sind, "
            "keine Lücken enthalten und alle Schritte der Lösung umsetzbar sind.\n"

            "- Unvollständige oder inkonsistente Aufgaben gefährden die Prüfungsqualität und sind daher **streng zu vermeiden**. "
            "Jede Aufgabe und Lösung muss logisch zusammenpassen und die vollständige Funktionsweise der Turingmaschine abbilden.\n"

            "- **Unvollständige Zustandsübergänge oder unklare Beschreibungen sind nicht akzeptabel.** Achten Sie darauf, "
            "dass die Aufgabenstellung vollständig den Vorgaben einer Turingmaschine entspricht und alle Operationen "
            "realistisch sind. Jeder mögliche Eingabefall muss abgedeckt sein.\n\n"

            "- Jegliche Missachtung dieser Anweisungen führt zu fehlerhaften und unbrauchbaren Aufgabenstellungen und muss "
            "daher vermieden werden. Diese Regeln sind entscheidend für die Qualität und den Nutzen der generierten Aufgaben.\n\n"
        )

    @staticmethod
    def create_validation_prompt():
        prompt_parts = [PromptBuilder.get_validation_base_prompt(), PromptBuilder.get_validation_prompt(),
                        PromptBuilder.get_structure_instructions()]
        return prompt_parts

    @staticmethod
    def get_validation_base_prompt():
        return (
            "# Aufgabenbeschreibung und Zielsetzung:\n\n"
            
            "Sie sind ein KI-Validierungsassistent mit Schwerpunkt Informatik. Ihr Ziel ist es, die Qualität, Genauigkeit "
            "und Umsetzbarkeit von Prüfungsaufgaben zu Turingmaschinen sicherzustellen. Überprüfen Sie die übergebenen Aufgaben "
            "und Lösungen auf Korrektheit, Vollständigkeit, logische Konsistenz und Umsetzbarkeit. Die Aufgaben sind für die "
            "Nutzung in Prüfungen vorgesehen und müssen den höchsten Ansprüchen an Qualität, Klarheit und Genauigkeit genügen. "
            "Jede Aufgabe muss mit einer Standard-Turingmaschine umsetzbar sein und darf keine logischen Widersprüche oder "
            "Fehler enthalten.\n\n"
        )

    @staticmethod
    def get_validation_prompt():
        return (
            "# Anforderungen an den Validierungsprozess:\n\n"
            
            "1. **Korrektheit der Aufgabenstellung:**\n"
            "- Stellen Sie sicher, dass die Aufgabenstellung präzise, klar und vollständig ist.\n"
            "- Vermeiden Sie logische Widersprüche, mehrdeutige Formulierungen oder unklare Anforderungen.\n\n"

            "2. **Korrektheit und Vollständigkeit der Lösung:**\n"
            "- Überprüfen Sie, ob die Lösung der Aufgabenstellung entspricht und alle geforderten Schritte klar und "
            "vollständig dokumentiert sind.\n"
            "- Stellen Sie sicher, dass die Lösung nachvollziehbar und frei von Lücken oder Fehlern ist.\n\n"

            "3. **Vollständigkeit der Zustandsübergangstabellen:**\n"
            "- Prüfen Sie, ob die Zustandsübergangstabellen alle möglichen Übergänge, Zustände und Eingaben vollständig "
            "abdecken.\n"
            "- Achten Sie darauf, dass keine Zustände oder Übergänge fehlen und dass die Tabellen korrekt formatiert "
            "und logisch konsistent sind.\n"
            "- Unvollständige oder fehlerhafte Übergangstabellen sind für Prüfungsaufgaben nicht akzeptabel.\n"
            "- Ergänzen Sie, falls sinnvoll, eine oder mehrere **Beispielablauftabellen** am Ende der Lösung, "
            "um die Schritte besser nachvollziehbar zu machen und die Lösung zu überprüfen.\n\n"

            "4. **Simulationsprüfung:**\n"
            "- Simulieren Sie jede Aufgabe Schritt für Schritt gedanklich oder systematisch, um die Zustandsübergänge "
            "und die Funktionsweise zu überprüfen.\n"
            "- Stellen Sie sicher, dass die Turingmaschine das erwartete Ergebnis liefert und dass keine Endlosschleifen "
            "oder fehlerhaften Ergebnisse auftreten.\n\n"

            "5. **Verbesserungen bei Mängeln:**\n"
            "- Falls Fehler, Lücken oder Inkonsistenzen gefunden werden:\n"
            "  - Korrigieren Sie die Aufgabenstellung, Lösung oder Zustandsübergangstabellen.\n"
            "  - Ergänzen Sie fehlende Informationen oder Übergänge, um Vollständigkeit zu gewährleisten.\n"
            "  - Erstellen Sie eine konsistente und korrekte Lösung, die den Prüfungsanforderungen entspricht.\n\n"

            "### Vorgehen bei der Validierung und Verbesserung:\n"
            "1. **Aufgabenstellung prüfen:**\n"
            "- Lesen Sie die Aufgabenstellung sorgfältig und stellen Sie sicher, dass sie alle Anforderungen erfüllt.\n\n"
            "2. **Lösungsprüfung:**\n"
            "- Vergleichen Sie die Lösung mit der Aufgabenstellung, um sicherzustellen, dass sie korrekt, vollständig "
            "und nachvollziehbar ist.\n\n"
            "3. **Zustandsübergangstabellen validieren:**\n"
            "- Überprüfen Sie jede Tabelle auf Vollständigkeit, Konsistenz und Richtigkeit.\n"
            "- Ergänzen Sie fehlende Übergänge und korrigieren Sie fehlerhafte Einträge.\n\n"
            "4. **Simulationsprüfung durchführen:**\n"
            "- Prüfen Sie, ob die Zustandsübergänge korrekt implementiert sind und ob die Maschine wie erwartet funktioniert.\n\n"

            "### Abschlussprüfung:\n"
            "Führen Sie nach der Überprüfung und Verbesserung eine abschließende Prüfung durch, um sicherzustellen, dass:\n"
            "- Jede Aufgabe logisch konsistent, korrekt und vollständig ist.\n"
            "- Alle Lösungen präzise und nachvollziehbar sind.\n"
            "- Zustandsübergangstabellen keine Lücken oder Fehler enthalten.\n"
            "- Jede Aufgabe realistisch und fehlerfrei mit einer Standard-Turingmaschine umsetzbar ist.\n\n"

            "### Hinweise für die Validierung:\n"
            "- Die generierten Aufgaben und Lösungen müssen exakt den Prüfungsanforderungen genügen.\n"
            "- Vermeiden Sie unnötige Komplexität, die die Richtigkeit der Aufgabe gefährden könnte.\n"
            "- Achten Sie darauf, dass jede Aufgabe den Anforderungen an Klarheit und Umsetzbarkeit entspricht.\n"
            "- Validieren Sie jede Aufgabe und Lösung gründlich, bevor sie als korrekt betrachtet wird.\n\n"

            "**Geben Sie die validierten und ggf. verbesserten Aufgaben im ursprünglichen Format zurück.**\n\n"
        )

