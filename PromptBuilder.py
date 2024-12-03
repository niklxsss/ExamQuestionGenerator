from Const import *


class PromptBuilder:

    # task_message -----------------------------------------------------------------------------------------------------

    @staticmethod
    def get_task_system_prompt():
        return(
            "Du bist ein spezialisiertes KI-Modell, das Aufgaben zu Turingmaschinen erstellt. Dein Ziel ist es, "
            "fehlerfreie, konsistente und qualitativ hochwertige Augaben zu erstellen!\n\n"
            "Halte dich unbedingt an die Anforderungen des Users!!!\n\n"
        )

    @staticmethod
    def get_task_base_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        return (
            "# Ziel der Aufgabe:\n\n"

            f"Generieren Sie genau **{num_questions}** Prüfungsaufgaben zu Turingmaschinen.\n\n"
            f"### Zielgruppe und Anforderungen:\n"
            f"Diese Aufgaben sollen speziell für Studierende der Informatik erstellt werden, um deren "
            f"Verständnis und Anwendungskompetenz zu überprüfen.\n\n"

            f"### Schwierigkeitsgrad:\n"
            f"Die Aufgaben müssen dem Schwierigkeitsgrad '**{difficulty}**' entsprechen:\n"
            f"{difficulty_explanation}\n\n"

            f"### Qualitätskriterien:\n"
            f"Die Aufgaben müssen realistisch, fehlerfrei und mit einer Standard-Turingmaschine umsetzbar sein. "
            f"Sie sind direkt für Prüfungszwecke vorgesehen und müssen höchsten Ansprüchen an Richtigkeit, Vollständigkeit und Konsistenz genügen.\n\n"
        )

    @staticmethod
    def get_task_general_guidelines_prompt(difficulty):
        return (
            "## Allgemeine Anforderungen:\n"
            "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
            "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
            "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
            "- **Lösungsbezug:** Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n"
            "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"

            "## Einschränkungen und Komplexität:\n"
            "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
            f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
            "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"
        )

    @staticmethod
    def get_task_and_example_requirements_prompt():
        return (
            "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
            "- **Strikte Trennung:** Die 'question' muss **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
            "- **Verbot für technische Details:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
            "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"

            "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
            "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
            "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
            # "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Position sollte sinnvoll sein und logisch zur Aufgabenstellung passen (Wähle immer je nach Aufgabe die günstigste Position!!).\n"
            "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann. Dies hängt von der Natur der Aufgabe ab und kann bedeuten, dass der Kopf rechts oder links beginnt.\n"
            "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n\n"

            "## Spezifische Anforderungen an das Beispiel ('example'):\n"
            "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
            "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
            "- **Formatierung des Beispiels:** Das Beispiel muss immer im folgenden Format angegeben werden: `Eingabe: <Wert> | Ausgabe: <Wert>`.\n"
            "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"
        )

    @staticmethod
    def get_task_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Aufgaben:\n"
            "Stellen Sie sicher, dass die gesamte Aufgabe vollständig, korrekt und konsistent ist. "
            "Die Überprüfung umfasst folgende Aspekte:\n\n"

            "### Aufgabenstellung und Beispiel:\n"
            "- Überprüfen Sie, ob die Aufgabenstellung klar, präzise und vollständig ist.\n"
            "- Stellen Sie sicher, dass das Beispiel korrekt und auf die Aufgabenstellung abgestimmt ist.\n"
            "- Prüfen Sie, ob die Start und Endposition präzise definiert ist.\n"
            "- Prüfen Sie, dass die Fragestellung frei von Inhalten sind, die iegentlich in die Zusatzinformationen gehören.\n"
            "- Prüfen Sie, ob die Zusatzinformationen mit der Aufgabenstellung übereinstimmen und keine widersprüchlichen Angaben enthalten.\n\n"

            "### Abschließende Validierung:\n"
            "- Stellen Sie sicher, dass die gesamte Aufgabe den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
            "Verbessern Sie die Aufgabe, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
        )

    @staticmethod
    def get_task_request_prompt():
        return (
            "Erstelle die Aufgabenstellungen und jeweils ein passendes Beispiel. Stelle sicher, dass diese vollständig und fehlerfrei sind.\n\n"
        )

    @staticmethod
    def get_info_text_prompt():
        return ()

    @staticmethod
    def get_bas64_prompt():
        return ()

    @staticmethod
    def get_pdf_texts_prompt():
        return ()

    # state_transition_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_state_transition_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Zustandsübergangstabelle zu Turingmaschinen auf Basis von Aufgabenstellung und Beipiel erstellt. Dein Ziel ist es, "
            "fehlerfreie, konsistente und qualitativ hochwertige Zustandsübergangstabelle zu erstellen!\n\n"
            "Halte dich unbedingt an die folgenden Qualitätsstandards:\n\n"

            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Zustandsübergangstabelle MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in der Tabelle entsprechend der Aufgabenstellung angewendet werden.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
            "- Überprüfen Sie, dass alle Informationen korrekt in die Lösung integriert wurden.\n\n"

            "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
            "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
            "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
            "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
        )

    @staticmethod
    def get_state_transition_table_request_prompt(task_parts):
        return (
            f"Aufgaben:\n\n {task_parts}\n\n"
            "Erstellen Sie die Zustandübergangstabelle auf Basis der Aufgabenstellung und des Beispiels!\n"
        )

    @staticmethod
    def get_state_transition_table_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Zustandsübergangstabelle:\n"
            "Stellen Sie sicher, dass die gesamte Zustandsübergangstabelle vollständig, korrekt und konsistent ist. "

            "### Abschließende Validierung:\n"
            "- Stellen Sie sicher, dass die gesamte Zustandsübergangstabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
            "Verbessern Sie die Zustandsübergangstabelle, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
        )

    # example_flow_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_example_flow_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Beispielablauftabelle zu Turingmaschinen auf Basis von Aufgabenstellung, Beipiel und der schon Vorhanden Zustandsübergangstabelle erstellt. Dein Ziel ist es, "
            "fehlerfreie, konsistente und qualitativ hochwertige Beispielablauftabelle zu erstellen!\n\n"
            "Halte dich unbedingt an die folgenden Qualitätsstandards:\n\n"

            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Beispielablauftabelle MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in der Tabelle entsprechend der Aufgabenstellung angewendet werden.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n\n"

            "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
            "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an **und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!**\n"
            # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
            "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
        )

    @staticmethod
    def get_example_flow_table_request_prompt(task_parts):
        return (
            f"Aufgabenstellung und Zustandstabelle: {task_parts} \n\n"
            "Erstellen Sie die Beispielablauftabelle anhand der Aufgabenstellung, Zustandübergangstabelle und des Beispiele. Prüfen Sie danach, dass die Beispielablauftabelle fehlerfrei ist, keine Lücken enthält, alle veränderungen richtig dargstellt werde\n"
        )

    @staticmethod
    def get_example_flow_table_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Beispielablauftabelle:\n"
            "Stellen Sie sicher, dass die gesamte Beispielablauftabelle vollständig, korrekt und konsistent ist.\n"

            "### Abschließende Validierung:\n"
            "- Stellen Sie sicher, dass die gesamte Beispielablauftabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
            "Verbessern Sie die Beispielablauftabelle, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
        )

    # solution_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_solution_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Lösungsmaterial zu Turingmaschinen auf Basis von übergebenen schon erstellten Elementen erstellt. Dein Ziel ist es, "
            "fehlerfreie, konsistente und qualitativ hochwertige Lösungsmaterial zu erstellen!\n\n"
            "Halte dich unbedingt an die folgenden Qualitätsstandards:\n\n"

            # "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            # "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            # "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in der Tabelle entsprechend der Aufgabenstellung angewendet werden.\n"
            # "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n\n"

            "## Spezifische Anforderungen an die Lösung:\n"
            "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
            "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
            "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
        )

    @staticmethod
    def get_solution_request_prompt(task_parts):
        return (
            f"Aufgabenstellung und Tabelle:\n\n {task_parts}\n\n"
            "Erstellten Sie den rest der Lösung wie angegeben und baue die Aufgabe im format ExamQuestion zusammen!\n"
        )

    @staticmethod
    def get_solution_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Aufgabe:\n"
            "Stellen Sie sicher, dass die gesamte Aufgabe vollständig, korrekt und konsistent ist. "

            "### Abschließende Validierung:\n"
            "- Stellen Sie sicher, dass die gesamte Aufgabe den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
            "Verbessern Sie die Aufgabe, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
        )


    # @staticmethod
    # def get_question_prompt(num_questions, difficulty, difficulty_explanation):
    #     return (
    #
    #         "# Ziel der Aufgabe:\n\n"
    #
    #         f"Generieren Sie genau **{num_questions}** Prüfungsaufgaben zu Turingmaschinen.\n\n"
    #         f"### Zielgruppe und Anforderungen:\n"
    #         f"Diese Aufgaben sollen speziell für Studierende der Informatik erstellt werden, um deren "
    #         f"Verständnis und Anwendungskompetenz zu überprüfen.\n\n"
    #
    #         f"### Schwierigkeitsgrad:\n"
    #         f"Die Aufgaben müssen dem Schwierigkeitsgrad '**{difficulty}**' entsprechen:\n"
    #         f"{difficulty_explanation}\n\n"
    #
    #         f"### Qualitätskriterien:\n"
    #         f"Die Aufgaben müssen realistisch, fehlerfrei und mit einer Standard-Turingmaschine umsetzbar sein. "
    #         f"Sie sind direkt für Prüfungszwecke vorgesehen und müssen höchsten Ansprüchen an Richtigkeit, Vollständigkeit und Konsistenz genügen.\n\n"
    #
    #         "## Allgemeine Anforderungen:\n"
    #         "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
    #         "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben präzise, korrekt und konsistent sind.\n"
    #         "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
    #         "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
    #         "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"
    #
    #         "## Einschränkungen und Komplexität:\n"
    #         "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
    #         f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
    #         "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"
    #
    #         "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
    #         "- **Strikte Trennung:** Die 'question' muss **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
    #         "- **Verbot für technische Details:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
    #         "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"
    #
    #         "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
    #         "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
    #         "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
    #         "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann. Dies hängt von der Natur der Aufgabe ab und kann bedeuten, dass der Kopf rechts oder links beginnt.\n"
    #         "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n\n"
    #
    #         "## Spezifische Anforderungen an die Zusatztabellen ('optional_question_tables'):\n"
    #         "- NUR BENUTZEN WENN EXPLIZIT GEFORDERT, ANSONSTEN KEINE TABELLE ANGEBEN.\n\n"
    #
    #         "## Spezifische Anforderungen an das Beispiel ('example'):\n"
    #         "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
    #         "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
    #         "- **Formatierung des Beispiels:** Das Beispiel muss immer im folgenden Format angegeben werden: `Eingabe: <Wert> | Ausgabe: <Wert>`.\n"
    #         "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"
    #     )
    #
    # @staticmethod
    # def get_zustand_prompt():
    #     return (
    #         "Erstellen Sie die **Zustandsübergangstabelle** basierend auf der folgenden Aufgabenstellung und dem Beispiel.\n"
    #         "Stellen Sie sicher, dass die Tabelle den Ablauf der Turingmaschine vollständig, logisch konsistent und exakt abbildet.\n\n"
    #
    #         "## Konsistenz zwischen Aufgabenstellung, Beispiel und Zustandsübergangstabelle:\n"
    #         "- Die Zustandsübergangstabelle MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
    #         "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
    #         "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
    #         "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
    #
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
    #         "GEben Sie bitte nur den Table im übergebenen Format zurück!!!"
    #
    #         "class TableContent(BaseModel):\n"
    #         "title: str\n"
    #         "headers: List[str]\n"
    #         "rows: List[List[str]]\n"
    #     )
    #
    # @staticmethod
    # def get_bsp_prompt():
    #     return (
    #         "Erstellen Sie die **Beispielablauftabelle** basierend auf der folgenden Aufgabenstellung, Beispiel und. Zustandsübergangstabelle"
    #         "Stellen Sie sicher, dass die Tabelle den Bespielablauf der Turingmaschine konsistent und exakt anhand des Beispiels abbildet.\n\n"
    #
    #         "## Konsistenz zwischen Aufgabenstellung, Beispiel, Zustandsübergangstabelle und Beispielablauftabelle:\n"
    #         "- Die Beispielablauftabelle MUSS den den korrekten Ablauf des BEispeils entsprechen.\n"
    #         "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
    #         "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n\n"
    #
    #         "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #         "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
    #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #         "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
    #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
    #         # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
    #         "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
    #         "GEben Sie bitte nur den Table im übergebenen Format zurück!!!"
    #
    #         "class TableContent(BaseModel):"
    #         "title: str"
    #         "headers: List[str]"
    #         "rows: List[List[str]]"
    #    )
    #
    # @staticmethod
    # def get_sol_prompt():
    #     return (
    #         "korrigieren Sie folgende PRüfungsaufgabe der Turingmaschine: Bessern Sie alle Fehler in den TAbellen aus und erstellen sie den rest der Lösung:"
    #
    #         "## Spezifische Anforderungen an die Lösung:\n"
    #         "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
    #         "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
    #         "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #     )

    # --------Versuch Ende--------------------

    # ----------Verusch mit system u user u assistant zu arbeiten um mehr strukur zu schaffen------------

    # @staticmethod
    # def create_system_prompt(difficulty_eng):
    #     difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
    #     return (
    #         "Du bist ein KI-Modell, das Prüfungsaufgaben zu Turingmaschinen generiert. "
    #         "Antworten müssen präzise, fehlerfrei und den folgenden Anforderungen entsprechen:\n\n"
    #         + PromptBuilder.get_general_guidelines_prompt(difficulty)  # Allgemeine Anforderungen
    #         + "\n\n"
    #         + PromptBuilder.get_quality_prompt()
    #     )

    # @staticmethod
    # def create_prompt(num_questions, difficulty_eng):
    #     difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
    #     difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)
    #     # Liste für die Nachrichtenstruktur
    #     messages = []
    #
    #     # System-Prompt hinzufügen
    #     system_prompt = MessageBuilder.add_message(
    #         "system",
    #         [MessageBuilder.add_txt_to_content(
    #             "Du bist ein KI-Modell, das Prüfungsaufgaben zu Turingmaschinen generiert. Jede Aufgabe muss präzise, fehlerfrei und den spezifischen Anforderungen entsprechen."
    #         )]
    #     )
    #     messages.append(system_prompt)
    #
    #     # Schritt 1: Aufgabenbeschreibung (Base Prompt)
    #     base_prompt = MessageBuilder.add_message(
    #         "user",
    #         [MessageBuilder.add_txt_to_content(
    #             PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation)
    #         )]
    #     )
    #     messages.append(base_prompt)
    #
    #     # Schritt 2: Allgemeine Anforderungen und Einschränkungen
    #     general_guidelines = MessageBuilder.add_message(
    #         "user",
    #         [MessageBuilder.add_txt_to_content(
    #             PromptBuilder.get_general_guidelines_prompt(difficulty)
    #         )]
    #     )
    #     messages.append(general_guidelines)
    #
    #     # Schritt 3: Anforderungen an die Aufgabenstellung und Zusatzinformationen
    #     task_and_example_prompt = MessageBuilder.add_message(
    #         "user",
    #         [MessageBuilder.add_txt_to_content(
    #             PromptBuilder.get_task_and_example_prompt() + "Erstellen Sie Die Aufgabenstellung + Beispiel nach den "
    #                                                           "Vorgaben! Überprüfe danach, ob die Aufgabenstellung, die Zusatzinfos und das BEispiel konsistent sind!"
    #         )]
    #     )
    #     messages.append(task_and_example_prompt)
    #     #
    #     # Assistant: Überprüfung der Aufgabenstellung
    #     assistant_validation = MessageBuilder.add_message(
    #         # "assistant",
    #         "user",
    #         [MessageBuilder.add_txt_to_content(
    #             "Stelle sicher, dass die Aufgabenstellung, Zusatzinformationen und das Beispiel klar und konsistent sind. Prüfe insbesondere auf Widersprüche.\n\n"
    #         )]
    #     )
    #     messages.append(assistant_validation)
    #
    #
    #     # Schritt 7: Anforderungen an die Lösung
    #     solution_prompt = MessageBuilder.add_message(
    #         # "user",
    #         "system",
    #         [MessageBuilder.add_txt_to_content(
    #             # "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
    #             # "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
    #             # "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
    #             # "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
    #             # "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
    #
    #             "Du bist ein KI-Modell, das detaillierte Zustandsübergangstabellen und Beispielablauftabellen für Turingmaschinen erstellt. Beachte immer: "
    #             "Die Zustandsübergangstabelle und die Beispielablauftabelle müssen vollständig und konsistent sein. "
    #             "Jede Regel und jeder Schritt müssen mit der Aufgabenstellung und dem Beispiel übereinstimmen."
    #
    #             "Jede Tabelle muss:**\n"
    #             "1. Präzise und fehlerfrei sein.\n"
    #             "2. Vollständig alle Übergänge und Zustände abdecken.\n"
    #             "3. Konsistent mit der Aufgabenstellung und dem Beispiel sein.\n"
    #             "4. Die Kopfbewegung und Bandänderungen korrekt darstellen.\n\n"
    #
    #             "**Qualitätsanforderungen**:\n"
    #             "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #             "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
    #             "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #             "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #             "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
    #
    #             "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #             "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
    #             "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #             "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
    #             "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
    #             # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
    #             "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
    #
    #
    #         )]
    #     )
    #     messages.append(solution_prompt)

        # solution_prompt = MessageBuilder.add_message(
        #     "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
        #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
        #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
        #         "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
        #         "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
        #         "Erstelle die Zustandsübergangstabelle basierend auf der Aufgabenstellung und dem Beispiel. Jede Regel muss korrekt und konsistent sein. Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, korrigiere diese!!\n\n"
        #     )]
        # )
        # messages.append(solution_prompt)
        #
        # # Assistant: Überprüfung der Lösung
        # assistant_validation = MessageBuilder.add_message(
        #     "assistant",
        #     # "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "Prüfe die Zustandsübergangstabelle auf:\n"
        #         "- Vollständigkeit (alle Zustände und Übergänge abgedeckt)\n"
        #         "- Konsistenz mit der Aufgabenstellung und dem Beispiel\n"
        #         "- Wenn der Übertrag abgeschlossen ist, bewegt sich der Kopf korrekt zur Ruheposition.\n"
        #         "- Effizienz der Übergänge. Korrigiere logische Fehler und füge fehlende Zustände hinzu.\n\n"
        #     )]
        # )
        # messages.append(assistant_validation)
        #
        # solution_prompt = MessageBuilder.add_message(
        #     "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
        #         "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
        #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
        #         "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
        #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
        #         # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
        #         "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
        #         "Erstelle die Beispielablauftabelle. Überprüfe danach selbst ob sie mit der Zustandstabelle übereinstimmt und falls Fehler auftreten, korrigiere diese!\n"
        #         # "Erstellen Sie die Beispielablauftabelle auf Basis der Aufgabenstellung, des BEispiels und der Zustandsübergangstabelle FEHLERFREI!\n\n"
        #     )]
        # )
        # messages.append(solution_prompt)
        #
        # # Assistant: Überprüfung der Lösung
        # assistant_validation = MessageBuilder.add_message(
        #     "assistant",
        #     # "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "Prüfe die erstellte Beispielablauftabelle auf folgende Punkte:\n"
        #         "- Stimmen die Schritte und Kopfpositionen mit den Übergangsregeln der Zustandsübergangstabelle überein?\n"
        #         "- Sind alle Bandinhalte korrekt nach jeder Operation aktualisiert worden?\n"
        #         "- Gibt es Abweichungen zwischen den Zustandswechseln und der Tabelle? Wenn ja, korrigiere diese.\n\n"
        #     )]
        # )

        # ------tabellen zusammen generieren-----------
        # solution_prompt = MessageBuilder.add_message(
        #     "user",
        #     [MessageBuilder.add_txt_to_content(
        #         # "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
        #         # "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
        #         # "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
        #         # "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
        #         # "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
        #         # "Erstelle die Zustandsübergangstabelle basierend auf der Aufgabenstellung und dem Beispiel. Jede Regel muss korrekt und konsistent sein. Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, korrigiere diese!!\n\n"
        #         #
        #         # "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
        #         # "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
        #         # "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
        #         # "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
        #         # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
        #         # # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
        #         # "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
        #         # "Erstelle die Beispielablauftabelle auf Basis der Aufgabenstellung des Beispiels und der Zustandsübergangstabelle. Überprüfe danach selbst ob sie mit der Zustandstabelle übereinstimmt und falls Fehler auftreten, korrigiere diese!\n"
        #         # # "Erstellen Sie die Beispielablauftabelle auf Basis der Aufgabenstellung, des BEispiels und der Zustandsübergangstabelle FEHLERFREI!\n\n"
        #         "Erstelle die Zustandsübergangstabelle und Beispielablauftabelle basierend auf der Aufgabenstellung, dem Beispiel und den definierten Qualitätsanforderungen . Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, KORRIGIERE diese!!\n\n"
        #
        #     )]
        # )
        # messages.append(solution_prompt)
        #
        # # Assistant: Überprüfung der Lösung
        # assistant_validation = MessageBuilder.add_message(
        #     "assistant",
        #     # "user",
        #     [MessageBuilder.add_txt_to_content(
        #         # "Prüfe die Zustandsübergangstabelle auf:\n"
        #         # "- Vollständigkeit (alle Zustände und Übergänge abgedeckt)\n"
        #         # "- Konsistenz mit der Aufgabenstellung und dem Beispiel\n"
        #         # "- Wenn der Übertrag abgeschlossen ist, bewegt sich der Kopf korrekt zur Ruheposition.\n"
        #         # "- Effizienz der Übergänge. Korrigiere logische Fehler und füge fehlende Zustände hinzu.\n\n"
        #         #
        #         # "Prüfe die erstellte Beispielablauftabelle auf folgende Punkte:\n"
        #         # "- Stimmen die Schritte und Kopfpositionen mit den Übergangsregeln der Zustandsübergangstabelle überein?\n"
        #         # "- Sind alle Bandinhalte korrekt nach jeder Operation aktualisiert worden?\n"
        #         # "- Gibt es Abweichungen zwischen den Zustandswechseln und der Tabelle? Wenn ja, korrigiere diese.\n\n"
        #
        #         "Überprüfe die Zustandsübergangstabelle und die Beispielablauftabelle auf Konsistenz. "
        #         "Stimmen alle Übergänge mit der Aufgabenstellung und dem Beispiel überein? "
        #         "Falls nein, korrigiere die Fehler und generiere die Tabellen neu."
        #     )]
        # )
        # messages.append(assistant_validation)
        #
        #
        # # ------------------End----------------------------------------------------------------------------------------------e
        #
        #
        # solution_prompt = MessageBuilder.add_message(
        #     "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "## Spezifische Anforderungen an die Lösung:\n"
        #         "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
        #         "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
        #         "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
        #         "Erstelle die vollständige Lösung mit einer konzeptionellen Beschreibung, zusätzlichen Informationen und einem schrittweisen Lösungsweg.!!\n\n"
        #     )]
        # )
        # messages.append(solution_prompt)
        #
        # # Assistant: Überprüfung der Lösung
        # assistant_validation = MessageBuilder.add_message(
        #     "assistant",
        #     # "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "Prüfe die gesamte Lösung auf:\n"
        #         "- Konsistenz zwischen Beispiel, Zustandsübergangstabelle und Beispielablauftabelle.\n"
        #         "- Fehlerfreiheit in den Tabellen.\n"
        #         "- Eindeutigkeit und Klarheit der konzeptionellen Beschreibung.\n"
        #         "Verbessere inkonsistente oder fehlerhafte Abschnitte.\n\n"
        #     )]
        # )
        # messages.append(assistant_validation)
        #
        # # Schritt 8: Qualitätssicherung
        # quality_prompt = MessageBuilder.add_message(
        #     "user",
        #     [MessageBuilder.add_txt_to_content(
        #         PromptBuilder.get_quality_prompt()
        #     )]
        # )
        # messages.append(quality_prompt)
        #
        # # Assistant: Überprüfung der Qualitätssicherung
        # assistant_validation = MessageBuilder.add_message(
        #     "assistant",
        #     # "user",
        #     [MessageBuilder.add_txt_to_content(
        #         "Stelle sicher, dass die Qualitätssicherungsanforderungen vollständig erfüllt sind."
        #     )]
        # )
        # messages.append(assistant_validation)
        #
        # return messages

    @staticmethod
    def get_solution_prompt():
        return (
            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
            "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"

            "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
            "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
            "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
            "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"

            "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
            "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
            # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
            "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"

            "## Zusätzliche Tabellen ('optional_additional_solution_tables'):**\n"
            "- **Verwendungszweck:** Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"

            "## Spezifische Anforderungen an die Lösung:\n"
            "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
            "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
            "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
        )

    @staticmethod
    def create_prefix_prompt(num_questions, difficulty_eng, incorrect_task, files_txt, files_images, files_pdf):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        prompt_parts = [
            PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation),
            # PromptBuilder.get_general_guidelines_prompt(difficulty)
            # PromptBuilder.get_general_guidelines3456(difficulty)

            PromptBuilder.get_task_and_example_prompt(),
            PromptBuilder.get_solution_prompt(),
            # PromptBuilder.get_quality_prompt()
        ]

        if incorrect_task:
            prompt_parts.append(PromptBuilder.get_incorrect_task_prompt())

        if any([files_txt, files_images, files_pdf]):
            prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))

        # prompt_parts.append(PromptBuilder.get_task_and_example_prompt())
        # prompt_parts.append(PromptBuilder.get_solution_prompt())
        # prompt_parts.append(PromptBuilder.get_quality_prompt())

        return prompt_parts

    # -------------Verusch Ende --------------------------------------------------------------
    # @staticmethod
    # def create_prefix_prompt(num_questions, difficulty_eng, incorrect_task, files_txt, files_images, files_pdf):
    #     difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
    #     difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)
    #
    #     prompt_parts = [
    #         PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation),
    #         # PromptBuilder.get_general_guidelines_prompt(difficulty)
    #         PromptBuilder.get_general_guidelines3456(difficulty)
    #
    #         # PromptBuilder.get_task_and_example_prompt(),
    #         # PromptBuilder.get_solution_prompt(),
    #         # PromptBuilder.get_quality_prompt()
    #     ]
    #
    #     if incorrect_task:
    #         prompt_parts.append(PromptBuilder.get_incorrect_task_prompt())
    #
    #     if any([files_txt, files_images, files_pdf]):
    #         prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))
    #
    #     # prompt_parts.append(PromptBuilder.get_task_and_example_prompt())
    #     # prompt_parts.append(PromptBuilder.get_solution_prompt())
    #     # prompt_parts.append(PromptBuilder.get_quality_prompt())
    #
    #     return prompt_parts

    @staticmethod
    def create_suffix_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        return [
            # PromptBuilder.get_process_steps(difficulty),
            # PromptBuilder.get_structure_instructions(),
            # PromptBuilder.get_final_reminder(difficulty, difficulty_explanation, num_questions)
        ]



    @staticmethod
    def get_solution_prompt():
        return (
            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
            "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"

            "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
            "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
            "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
            "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"

            "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
            "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
            # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
            "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"

            "## Zusätzliche Tabellen ('optional_additional_solution_tables'):**\n"
            "- **Verwendungszweck:** Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"

            "## Spezifische Anforderungen an die Lösung:\n"
            "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
            "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
            "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
        )

    @staticmethod
    def get_quality_prompt():
        return (
            "## Qualitätssicherung:\n"
            "- **Kopfbewegung validieren:** Stellen Sie sicher, dass die Bewegungsrichtung des Kopfes die effizienteste und logischste Wahl ist, um das Ziel der Aufgabe zu erreichen.\n"
            "- **Testfälle:** Überprüfen Sie jede Aufgabe mit mehreren Testfällen, um Konsistenz und Korrektheit der Lösung sicherzustellen. Falls Fehler autreten, korrigieren Sie diese!\n"
            "- **Fehlerfreiheit:** Aufgaben mit Lücken oder Fehlern sind nicht akzeptabel. **Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein. Lösungen müssen Schritt für Schritt nachvollziehbar sein**.\n\n"
        )

    @staticmethod
    def get_incorrect_task_prompt():
        return (
            "# Zusätzliche Informationen zum Auftrag:\n\n"

            "Generieren Sie nur Aufgaben mit absichtlich fehlerhaften Turingmaschinen. Ziel dieser Aufgaben ist es, das "
            "Fehlersuch- und Korrekturvermögen der Studierenden gezielt zu überprüfen.\n\n"

            "## Anforderungen an die Fehlerstruktur:\n"
            "- Die Turingmaschine soll mindestens einen oder mehrere Fehler enthalten, der den gewünschten Output verhindert oder zu einem falschen Ergebnis führt.\n"
            "- Die Fehler müssen so eingebaut sein, dass sie logisch nachvollziehbar sind, aber eine sorgfältige Analyse erfordern, um identifiziert und behoben zu werden.\n"
            "- Fehler können auftreten in:\n"
            "   ⦁ **Zustandsübergängen** (z. B. fehlerhafte Übergangsregeln),\n"
            "   ⦁ **Lese- oder Schreibaktionen** (z. B. falsches Band-Symbol),\n"
            "   ⦁ **Bandbewegungen** (z. B. falsche Kopfbewegung).\n\n"

            "## Hinweise für die Gestaltung:\n"
            "- Fügen Sie Hinweise oder zusätzliche Informationen hinzu, falls erforderlich.\n"
            "- Verwenden Sie Tabellen, um die fehlerhafte Zustandstabelle klar und präzise zu visualisieren. Achten Sie darauf, dass alle Spalten und Zeilen korrekt formatiert und vollständig sind.\n"
            "- Fehler dürfen nicht trivial oder zu leicht zu erkennen sein, um eine angemessene Herausforderung zu gewährleisten.\n\n"

            "## Ergebnisformat:\n"
            "Stellen Sie sicher, dass die Aufgaben und Lösungen im vorgeschriebenen Format generiert werden. Jede Aufgabe muss:\n"
            "- **Klar formuliert** sein, um Missverständnisse zu vermeiden.\n"
            "- **Eine vollständige Lösung** enthalten, die den Fehler aufzeigt und korrigiert (inkl.  Korrigierte Zustandsübergangstabelle und korrekter Beispielablauftabelle).\n\n"

            "Beachten Sie, dass diese Aufgaben speziell darauf abzielen, die Analyse- und Problemlösungsfähigkeiten der Studierenden zu überprüfen.\n\n"
        )

    @staticmethod
    def get_attachments_prompt(files_txt, files_images, files_pdf):
        attachments = (
            "# Zusätzliche Informationen:\n\n"
            "Als Hilfsmittel für die Erstellung von Aufgaben zu Turingmaschinen wurden folgende Inhalte dem Prompt angehängt:\n\n"
        )
        attachments += PromptBuilder.get_attachment_prompt("Text-Datei", files_txt)
        attachments += PromptBuilder.get_attachment_prompt("PDF-Datei", files_pdf)
        attachments += PromptBuilder.get_attachment_prompt("Bild-Datei", files_images)
        return attachments

    @staticmethod
    def get_attachment_prompt(datei_typ, files):
        if files:
            return (
                f"- **{datei_typ}:**\n"
                f"  Es wurden {len(files)} {datei_typ.lower()}(en) beigefügt.\n"
                f"  Nutzen Sie die Inhalte aus der beigefügten {datei_typ.lower()}, um die Aufgaben entsprechend zu gestalten.\n\n"
            )
        return ""

    @staticmethod
    def get_general_guidelines3456(difficulty):
        return (
            "## Allgemeine Anforderungen:\n"
            "- *Sprache:* Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "- *Korrektheit:* Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
            "- *Klarheit:* Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
            "- *Keine Spoiler:* Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
            "- *Lösungsbezug:* Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n"
            "- *Formatierung von Aufzählungen:* Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"

            "## Einschränkungen und Komplexität:\n"
            "- *Kompatibilität mit Standard-Turingmaschinen:* Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
            f"- *Schwierigkeitsniveau:* Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '{difficulty}' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
            "- *Realisierbarkeit:* Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"

            "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
            "- *Strikte Trennung:* Die 'question' muss *ausschließlich* das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
            "- *Verbot für technische Details:* Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
            "- *Eindeutigkeit:* Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"

            "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
            "- *Alphabet:* Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol ■ (Klartext, nicht in anderen Formaten).\n"
            "- *Bandinhalt:* Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen ■ begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
            # "- *Start- und Endposition:* Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Position sollte sinnvoll sein und logisch zur Aufgabenstellung passen (Wähle immer je nach Aufgabe die günstigste Position!!).\n"
            "- *Start- und Endposition:* Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann. Dies hängt von der Natur der Aufgabe ab und kann bedeuten, dass der Kopf rechts oder links beginnt.\n"
            "- *Konzepte und Prinzipien:* Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n\n"

            "## Spezifische Anforderungen an das Beispiel ('example'):\n"
            "- *Sinnvolles Beispiel:* Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
            "- *Korrekte Darstellung:* Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole ■ am Anfang und Ende (z. B. ■11010■).\n"
            "- *Eindeutigkeit:* Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"

            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
            "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"

            "## Zustandsübergangstabelle ('solution_state_transition_table'):\n"
            "- *Konsistenz:* Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
            "- *Spaltenstruktur:* Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- *Vollständigkeit:* Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen ■, müssen abgedeckt sein.\n"
            "- *Logik und Effizienz:* Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"

            "## Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- *Konsistenz:* Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
            "- *Spaltenstruktur:* Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- *Kopfposition:* Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG *1* UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
            "- *Bandinhalt:* Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
            # "- *Bandinhalt:* Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
            "- *Anwendung der Übergangsregeln:* Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"

            "## Zusätzliche Tabellen ('optional_additional_solution_tables'):\n"
            "- *Verwendungszweck:* Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"

            "## Spezifische Anforderungen an die Lösung:\n"
            "- *Lösung ('solution')*: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
            "- *Zusätzliche Informationen ('optional_solution_additional_infos')*: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
            "- *Lösungsweg ('optional_solution_step_by_step')*: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"

            "## Qualitätssicherung:\n"
            "- *Kopfbewegung validieren:* Stellen Sie sicher, dass die Bewegungsrichtung des Kopfes die effizienteste und logischste Wahl ist, um das Ziel der Aufgabe zu erreichen.\n"
            "- *Testfälle:* Überprüfen Sie jede Aufgabe mit mehreren Testfällen, um Konsistenz und Korrektheit der Lösung sicherzustellen. Falls Fehler autreten, korrigieren Sie diese!\n"
            "- *Fehlerfreiheit:* Aufgaben mit Lücken oder Fehlern sind nicht akzeptabel. *Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein. Lösungen müssen Schritt für Schritt nachvollziehbar sein*.\n\n"
        )

    # --------------------------------------------------------------------------------------------------------------------

    # @staticmethod
    # def get_general_guidelines3456(difficulty):
    #     return (
    #         "## Allgemeine Anforderungen:\n"
    #         "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
    #         "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
    #         "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
    #         "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
    #         "- **Lösungsbezug:** Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n"
    #         "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"
    #
    #         "## Einschränkungen und Komplexität:\n"
    #         "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
    #         f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
    #         "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"
    #
    #         "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
    #         "- **Strikte Trennung:** Die 'question' muss **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
    #         "- **Verbot für technische Details:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
    #         "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"
    #
    #         "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
    #         "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
    #         "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
    #         # "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Position sollte sinnvoll sein und logisch zur Aufgabenstellung passen (Wähle immer je nach Aufgabe die günstigste Position!!).\n"
    #         "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann. Dies hängt von der Natur der Aufgabe ab und kann bedeuten, dass der Kopf rechts oder links beginnt.\n"
    #         "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n\n"
    #
    #         "## Spezifische Anforderungen an das Beispiel ('example'):\n"
    #         "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
    #         "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
    #         "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"
    #
    #         "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
    #         "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
    #         "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
    #         "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
    #         "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
    #
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
    #
    #         "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #         "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
    #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #         "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
    #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
    #         # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
    #         "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
    #
    #         "## Zusätzliche Tabellen ('optional_additional_solution_tables'):**\n"
    #         "- **Verwendungszweck:** Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"
    #
    #         "## Spezifische Anforderungen an die Lösung:\n"
    #         "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
    #         "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
    #         "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #
    #         "## Qualitätssicherung:\n"
    #         "- **Kopfbewegung validieren:** Stellen Sie sicher, dass die Bewegungsrichtung des Kopfes die effizienteste und logischste Wahl ist, um das Ziel der Aufgabe zu erreichen.\n"
    #         "- **Testfälle:** Überprüfen Sie jede Aufgabe mit mehreren Testfällen, um Konsistenz und Korrektheit der Lösung sicherzustellen. Falls Fehler autreten, korrigieren Sie diese!\n"
    #         "- **Fehlerfreiheit:** Aufgaben mit Lücken oder Fehlern sind nicht akzeptabel. **Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein. Lösungen müssen Schritt für Schritt nachvollziehbar sein**.\n\n"
    #     )
    #
    #
    #
    # @staticmethod
    # def get_general_guidelines5():
    #     return (
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #         # "- Erstellen Sie eine vollständige und KORREKTE Zustandsübergangstabelle, die alle möglichen Zustände, Übergänge und alle Zwischenschritte abdeckt und exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n"
    #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
    #         # "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n\n"
    #         # "- Stellen Sie sicher, dass Übergänge am Bandende (Leerzeichen `■`) korrekt behandelt werden.\n"
    #         # "- Vermeiden Sie Zustands- oder Übergangslücken, insbesondere bei komplexen Aufgaben.\n"
    #         # "- Vermeiden Sie unnötige Zustände oder Übergänge.\n"
    #         # "- Stellen Sie sicher, dass alle Zustände und Übergänge fehlerfrei und konsistent mit der Aufgabenstellung sind.\n\n"
    #     )
    #
    # @staticmethod
    # def get_general_guidelines6():
    #     return (
    #          "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #          "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
    #         # "- Erstellen Sie eine Beispielablauftabelle, die jeden erforderlichen Schritt der Turingmaschine dokumentiert (in der Reihenfolge: Schritt, aktueller Zustand, Bandzustand, Kopfposition).\n"
    #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #         "- **Kopfposition:** NKopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE!\n"
    #         # "- In der Spalte Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE.! Dies ist unabhängig davon, ob die Position initial auf einem Leerzeichen, einem Eingabezeichen oder einem Bandende-Symbol liegt.\n"
    #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■[1]000■)!\n\n"
    #         # "- In der Spalte Bandinhalt muss der gesamte Bandinhalt einschließlich aller Leerzeichen vor und nach der Eingabe angegeben werden. Zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] zu kennzeichnen (Beispiel: ■[1]000■).\n\n"
    #         # "- Diese Tabelle MUSS exakt die Übergänge und Ergebnisse der Maschine darstellen und konsistent mit der Zustandsübergangstabelle sowie der Aufgabenstellung und dem Beispiel sein.\n"
    #         # "- Simulieren Sie die Schritte und korrigieren Sie Diskrepanzen, bis alle Anforderungen erfüllt und alle Zwischenschritte vollständig sind.\n\n"
    #         # "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n\n"
    #     )
    #
    # @staticmethod
    # def get_general_guidelines7():
    #     return (
    #         "## Zusätzliche Tabellen ('optional_additional_solution_tables'):**\n"
    #         "- **Verwendungszweck:** Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"
    #
    #     )
    #
    # @staticmethod
    # def get_general_guidelines8():
    #     return (
    #         "## Spezifische Anforderungen an die Lösung:\n"
    #         "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
    #         "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
    #         "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #     )
    #
    #
    #
    # @staticmethod
    # def get_general_guidelines_og(difficulty):
    #     return (
    #         "# Anforderungen:\n\n"
    #
    #         "## Allgemeine Anforderungen:\n"
    #         "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
    #         "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
    #         "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
    #         "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
    #         "- **Lösungsbezug:** Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n"
    #         "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"
    #
    #         "## Einschränkungen und Komplexität:\n"
    #         "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
    #         f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
    #         "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"
    #
    #         # "## Einfachheit und Effizienz:\n"
    #         # "- Die Aufgabe soll so starten und enden, dass der Ablauf der Turingmaschine, je nach Aufgabenstellung, am logischsten ist!"
    #         # "- Die Lösung der Aufgabe (einschließlich Zustandsübergangstabelle und Beispielablauftabelle) MUSS die Anforderungen auf die einfachste und effizienteste Weise erfüllen.\n"
    #         # "- Vermeiden Sie unnötige Zustände, Übergänge oder komplexe Abläufe, die nicht erforderlich sind, um eine tendenziell einfache Aufgabe korrekt zu lösen.\n"
    #         # "- Jede Aufgabe und Lösung soll den klarsten Weg zur Erfüllung der Anforderungen beschreiben.\n\n"
    #
    #         "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
    #         "- **Strikte Trennung:** Die 'question' muss **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
    #         "- **Verbot für technische Details:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
    #         "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"
    #
    #         "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
    #         "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
    #         "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
    #         # "- **Startposition und Endzustand:** Geben Sie eindeutig an, an welcher Position der Lese-/Schreibkopf der Turingmaschine startet und wo er nach Abschluss stehen bleibt. Geben Sie dabei immer die Seite der Eingabe (links oder rechts) an. Achte dabei auch darauf, welche Start und Endposition sich durch die Aufgabenstellung anbietet!\n"
    #         "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Position sollte sinnvoll sein und logisch zur Aufgabenstellung passen.\n"
    #         "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n"
    #         # "Diese Details sind nur in den Zusatzinformationen erlaubt.\n\n"
    #
    #         "## Spezifische Anforderungen an das Beispiel ('example'):\n"
    #         "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
    #         "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
    #         # "- **Korrekte Darstellung:** Die Eingabe und der daraus resultierende Output müssen **inklusive der Leerzeichen-Symbole `■` am Anfang und Ende** dargestellt werden, um die Konsistenz mit der Bandrepräsentation zu gewährleisten. Bsp: `■11010■`\n"
    #         "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"
    #
    #         "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
    #         "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
    #         "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
    #         "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
    #
    #         # "## Einfachheit und Effizienz:\n"
    #         # "- Die Aufgabe soll so starten und enden, dass der Ablauf der Turingmaschine am logischsten ist!"
    #         # "- Die Lösung der Aufgabe (einschließlich Zustandsübergangstabelle und Beispielablauftabelle) MUSS die Anforderungen auf die einfachste und effizienteste Weise erfüllen.\n"
    #         # "- Vermeiden Sie unnötige Zustände, Übergänge oder komplexe Abläufe, die nicht erforderlich sind, um eine tendenziell einfache Aufgabe korrekt zu lösen.\n"
    #         # "- Jede Aufgabe und Lösung soll den klarsten Weg zur Erfüllung der Anforderungen beschreiben.\n\n"
    #
    #         "## Spezifische Anforderungen an die Lösung:\n"
    #         "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
    #         "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
    #         "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #         # "- Erstellen Sie eine vollständige und KORREKTE Zustandsübergangstabelle, die alle möglichen Zustände, Übergänge und alle Zwischenschritte abdeckt und exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen. "
    #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n\n"
    #         # "- Stellen Sie sicher, dass Übergänge am Bandende (Leerzeichen `■`) korrekt behandelt werden.\n"
    #         # "- Vermeiden Sie Zustands- oder Übergangslücken, insbesondere bei komplexen Aufgaben.\n"
    #         # "- Vermeiden Sie unnötige Zustände oder Übergänge.\n"
    #         # "- Stellen Sie sicher, dass alle Zustände und Übergänge fehlerfrei und konsistent mit der Aufgabenstellung sind.\n\n"
    #
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Effizienz:** Vermeiden Sie unnötige Zustände oder Übergänge.\n"
    #         "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen."
    #
    #         "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #         # "- Erstellen Sie eine Beispielablauftabelle, die jeden erforderlichen Schritt der Turingmaschine dokumentiert (in der Reihenfolge: Schritt, aktueller Zustand, Bandzustand, Kopfposition).\n"
    #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #         "- **Kopfposition:** NKopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE!\n"
    #         # "- In der Spalte Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE.! Dies ist unabhängig davon, ob die Position initial auf einem Leerzeichen, einem Eingabezeichen oder einem Bandende-Symbol liegt.\n"
    #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■[1]000■)!\n"
    #         # "- In der Spalte Bandinhalt muss der gesamte Bandinhalt einschließlich aller Leerzeichen vor und nach der Eingabe angegeben werden. Zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] zu kennzeichnen (Beispiel: ■[1]000■).\n\n"
    #         # "- Diese Tabelle MUSS exakt die Übergänge und Ergebnisse der Maschine darstellen und konsistent mit der Zustandsübergangstabelle sowie der Aufgabenstellung und dem Beispiel sein.\n"
    #         # "- Simulieren Sie die Schritte und korrigieren Sie Diskrepanzen, bis alle Anforderungen erfüllt und alle Zwischenschritte vollständig sind.\n\n"
    #         "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n\n"
    #
    #
    #         # "## Einschränkungen und Komplexität:\n"
    #         # "- **Turingmaschinen-Kompatibilität:** Aufgaben müssen realistisch mit einer Standard-Turingmaschine lösbar sein und dürfen keine zusätzlichen Speicher- oder Zählmechanismen voraussetzen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen.\n"
    #         # f"- **Komplexitätsniveau:** Halten Sie die Komplexität der Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
    #         # "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"
    #
    #         "## Qualitätssicherung:\n"
    #         "- **Testfälle:** Überprüfen Sie jede Aufgabe mit mehreren Testfällen, um Konsistenz und Korrektheit der Lösung sicherzustellen.\n"
    #         "- **Fehlerfreiheit:** Aufgaben mit Lücken oder Fehlern sind nicht akzeptabel. **Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein. Lösungen müssen Schritt für Schritt nachvollziehbar sein**.\n\n"
    #     )

    # @staticmethod
    # def get_general_guidelines1(difficulty):
    #     return (
    #         "# Anforderungen für die Erstellung von Turingmaschinen-Aufgaben:\n\n"
    #
    #         "## Allgemeine Anforderungen:\n"
    #         "- **Sprache:** Alle Inhalte müssen auf Deutsch verfasst werden.\n"
    #         "- **Korrektheit:** Aufgaben und Lösungen müssen präzise, korrekt und logisch konsistent sein.\n"
    #         "- **Klarheit:** Formulieren Sie die Aufgabenstellung so, dass sie vollständig, eindeutig und leicht verständlich ist.\n"
    #         "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inklusive Zusatzinformationen und Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
    #         "- **Formatierung von Aufzählungen:** Verzichten Sie auf Nummerierungen, Striche oder andere Aufzählungszeichen in Listen, da diese automatisch hinzugefügt werden.\n"
    #         "- **Effizienz:** Die Lösung der Aufgabe muss den effizientesten und klarsten Weg zur Erfüllung der Anforderungen darstellen.\n\n"
    #
    #         "## Einschränkungen und Komplexität:\n"
    #         "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
    #         f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
    #         "- **Realisierbarkeit:** Vermeiden Sie komplexe oder nicht umsetzbare Operationen, die eine Standard-Turingmaschine nicht ausführen kann.\n\n"
    #
    #         "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
    #         "- **Strikte Trennung:** Die 'question' muss ausschließlich das zu lösende Problem beschreiben und darf keine technischen Details, Hinweise oder Beispiele enthalten.\n"
    #         "- **Verbot für technische Details:** Hinweise zu Leerzeichen, Begrenzungen, Start-/Endpositionen oder anderen Spezifikationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
    #         "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"
    #
    #         "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
    #         "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
    #         "- **Bandinhalt:** Beschreiben Sie, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist (Band selbst ist unendlich).\n"
    #         "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Position sollte logisch zur Aufgabenstellung passen.\n"
    #         "- **Konzepte:** Erläutern Sie methodische Ansätze oder Prinzipien, die für die Lösung der Aufgabe wichtig sind.\n\n"
    #
    #         "## Anforderungen an das Beispiel ('example'):\n"
    #         "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Aufgabenstellung verdeutlicht und zur Lösung passt.\n"
    #         "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
    #         "- **Eindeutigkeit:** Das Beispiel muss den Ablauf der Turingmaschine widerspiegeln und darf nicht von der Aufgabenstellung oder der Lösung abweichen.\n\n"
    #
    #         "## Anforderungen an die Lösung:\n"
    #         "- **Konzeptionelle Beschreibung ('solution'):** Geben Sie eine klare Beschreibung des Lösungsansatzes, der zeigt, wie die Aufgabe gelöst wird.\n"
    #         "- **Zusätzliche Informationen ('optional_solution_additional_infos'):** Fügen Sie optional hilfreiche Details hinzu, um die Lösung verständlicher zu machen.\n"
    #         "- **Schritt-für-Schritt-Anleitung ('optional_solution_step_by_step'):** Beschreiben Sie optional die Lösung in Textform, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #
    #         "## Zustandsübergangstabelle ('solution_state_transition_table'):\n"
    #         "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #         "- **Vollständigkeit:** Alle möglichen Zustände und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #         "- **Effizienz:** Vermeiden Sie unnötige Zustände oder Übergänge.\n"
    #
    #         "## Beispielablauftabelle ('solution_example_flow_table'):\n"
    #         "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #         "- **Kopfposition:** Numerischer Wert der aktuellen Position des Lese-/Schreibkopfes, beginnend bei 1. Die Position ist unabhängig von Leerzeichen oder Symbolen auf dem Band.\n"
    #         "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen, und markieren Sie die Kopfposition mit `[ ]` (z. B. `■[1]000■`).\n"
    #         "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle übereinstimmen.\n\n"
    #
    #         "## Qualitätssicherung:\n"
    #         "- **Testfälle:** Überprüfen Sie jede Aufgabe und Lösung mit mehreren Testfällen, um Konsistenz und Korrektheit sicherzustellen.\n"
    #         "- **Fehlerfreiheit:** Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein.\n\n"
    #     )
    #

    #
    # @staticmethod
    # def get_process_steps(difficulty):
    #     return (
    #         "# Ablauf der Prüfungsfrage-Generierung:\n\n"
    #
    #         "## Wichtiger Hinweis:\n"
    #         "- **Halten Sie sich strikt an die unten angegebene Abfolge der Schritte, um sicherzustellen, dass keine Fehler oder Unvollständigkeiten auftreten.**\n"
    #         "- **Jeder Schritt muss vollständig abgeschlossen sein, bevor mit dem nächsten fortgefahren wird.**\n\n"
    #
    #         "##Der folgende Ablauf gewährleistet, dass die generierten Prüfungsaufgaben korrekt, vollständig und für Prüfungen geeignet sind:\n\n"
    #
    #         "1. **Aufgabenart bestimmen:**\n"
    #         "   Wählen Sie die Art der Aufgabe, falls nicht vorgegeben, und stellen Sie sicher, dass die Aufgabenstellung vollständig, präzise und klar ist. "
    #         "Alle Aufgaben müssen auf realistisch umsetzbaren Operationen einer Turingmaschine basieren.\n\n"
    #
    #         f"2. **Schwierigkeitsstufe prüfen:**\n"
    #         f"   Die Aufgaben müssen auf dem Schwierigkeitsgrad **{difficulty}** bleiben. Stellen Sie sicher, dass die Aufgabenstellung den Anforderungen "
    #         f"dieser Stufe entspricht. Vermeiden Sie plötzliche Sprünge in der Komplexität.\n\n"
    #
    #         "3. **Kohärenz und Umsetzbarkeit sicherstellen:**\n"
    #         "   Vergewissern Sie sich, dass die Aufgaben auf der gewählten Schwierigkeitsstufe realistisch, kohärent und umsetzbar sind. "
    #         "Die Komplexität sollte so gehalten werden, dass die Aufgabe korrekt gelöst werden kann.\n\n"
    #
    #         "4. **Aufgabenstellung und Zusatzinformationen erstellen:**\n"
    #         "- **Formulieren Sie die Frage ('question'), die nur das Problem beschreibt.**\n"
    #         "- **Überprüfen Sie, ob die Frage keine technischen Details enthält.**\n"
    #         "- **Fügen Sie die technischen Details ausschließlich in die Zusatzinformationen ('optional_question_additional_infos') ein.**\n"
    #         "- **Finalisieren Sie die Frage, indem Sie sicherstellen, dass keine Redundanzen oder Widersprüche zwischen Frage und Zusatzinformationen bestehen.**\n\n"
    #
    #         "5. **Beispiele hinzufügen:**\n"
    #         "   Generieren Sie ein Beispiel, welches zur Verdeutlichung der Aufgabenstellung dient. "
    #         "**Stellen Sie sicher, dass das Beispiel korrekt ist** und die Anforderungen der Aufgabenstellung erfüllt!.\n\n"
    #
    #         "6. **Lösung entwickeln:**\n"
    #         "   Formulieren Sie eine klare und vollständige Lösung, die direkt zur Aufgabenstellung passt. "
    #         "Erklären Sie alle Schritte nachvollziehbar, falls es der Aufgabentyp erfordert und achten Sie darauf, dass die Lösung alle Anforderungen abdeckt.\n\n"
    #
    #         "7. **Zustandsübergangstabelle erstellen:**\n"
    #         "   **Erstellen Sie eine vollständige und KORREKTE Zustandsübergangstabelle, die alle möglichen Zustände, Übergänge und alle Zwischenschritte abdeckt und exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n"
    #         "- Stellen Sie sicher, dass Übergänge am Bandende (Leerzeichen `■`) korrekt behandelt werden.\n"
    #         "- Vermeiden Sie Zustands- oder Übergangslücken, insbesondere bei komplexen Aufgaben.\n"
    #         "- Vermeiden Sie unnötige Zustände oder Übergänge.\n"
    #         "- Stellen Sie sicher, dass alle Zustände und Übergänge fehlerfrei und konsistent mit der Aufgabenstellung sind.\n"
    #         "- Validieren Sie die Tabelle, indem Sie die Simulation Schritt für Schritt prüfen und sicherstellen, dass keine Zustände übersprungen werden.\n\n"
    #
    #         "8. **Überprüfung der Zustandsübergangstabelle:**\n"
    #         "   Testen Sie die Zustandsübergangstabelle umfassend!.\n"
    #         "Stellen Sie sicher, dass alle Übergänge vollständig und korrekt beschrieben sind und die Tabelle alle notwendigen Schritte abbildet! (keine Zustände oder Schritte dürfen fehlen).\n"
    #         "Die Tabelle muss konsistent mit der Aufgabenstellung und dem Beispiel sein.\n\n"
    #
    #         "9. **Beispielablauftabelle ergänzen:**\n"
    #         "   - Erstellen Sie eine Beispielablauftabelle, die jeden erforderlichen Schritt der Turingmaschine dokumentiert (in der Reihenfolge: Schritt, aktueller Zustand, Bandzustand, Kopfposition).\n"
    #         "- In der Spalte Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE.! Dies ist unabhängig davon, ob die Position initial auf einem Leerzeichen, einem Eingabezeichen oder einem Bandende-Symbol liegt.\n"
    #         "- In der Spalte Bandinhalt muss der gesamte Bandinhalt einschließlich der Leerzeichen vor und nach der Eingabe angegeben werden. Zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] zu kennzeichnen (Beispiel: ■[1]000■).\n"
    #         "- Diese Tabelle MUSS exakt die Übergänge und Ergebnisse der Maschine darstellen und konsistent mit der Zustandsübergangstabelle sowie der Aufgabenstellung und dem Beispiel sein.\n"
    #         "- Simulieren Sie die Schritte und korrigieren Sie Diskrepanzen, bis alle Anforderungen erfüllt und alle Zwischenschritte vollständig sind.\n\n"
    #
    #         "10. **Kombinierte Überprüfung der Tabellen:**\n"
    #         "   **Sobald die Zustandsübergangstabelle und die Beispielablauftabelle erstellt wurden, müssen diese umfassend getestet werden.**\n"
    #         "- **Prüfen Sie, ob beide Tabellen vollständig und fehlerfrei sind und ob sie konsistent miteinander sowie mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n\n"
    #
    #         "11. **Weitere Tabellen ergänzen wenn nötig:**\n"
    #         "   Falls zu den bestehenden Tabellen zusätzliche Tabellen für die Lösung erforderlich sind, ergänzen Sie diese unter `optional_additional_solution_tables`.\n"
    #         "Stellen Sie sicher, dass alle zusätzlichen Tabellen korrekt, vollständig und konsistent mit den Haupttabellen sind.\n\n"
    #
    #         "12. **Abschließende Prüfung:**\n"
    #         "   Validieren Sie jede Aufgabe umfassend, indem Sie folgende Schritte iterativ durchführen:\n"
    #         "- **Übergangsvalidierung:** Stellen Sie sicher, dass die Zustandsübergangstabelle vollständig und korrekt ist. Alle Zustände und Übergänge müssen vorhanden sein, einschließlich Bandende- und Sonderzeichen-Übergängen (■).\n"
    #         "- **Simulation:** Simulieren Sie jeden Schritt der Aufgabe. Die Simulation muss zeigen, dass die Turingmaschine alle Übergänge korrekt umsetzt und das erwartete Ergebnis liefert.\n"
    #         "- **Grenzfalltests:** Testen Sie die Aufgabe mit leeren Eingaben, ungültigen Zeichen oder ungewöhnlichen Kombinationen. Validieren Sie, dass die Maschine korrekt darauf reagiert.\n"
    #         "- **Ergebnisabgleich:** Überprüfen Sie, ob das Ergebnis der Simulation exakt den Anforderungen der Aufgabenstellung entspricht.\n"
    #         "Eine Aufgabe darf erst zurückgegeben werden, wenn alle Tests erfolgreich abgeschlossen sind. **Fehlerhafte oder unvollständige Aufgaben sind unzulässig!**\n\n"
    #     )
    #
    # @staticmethod
    # def get_structure_instructions():
    #     header = "# Struktur der Prüfungsaufgaben:\n\n"
    #
    #     general_instructions = (
    #         "## Allgemeine Richtlinien:\n"
    #         "- Die Prüfungsaufgaben und Lösungen sollen im `ExamQuestions`-Response-Format strukturiert sein.\n"
    #         "- Verwenden Sie optionale Felder nur, wenn sie die Aufgabe oder Lösung klarer und verständlicher machen.\n"
    #         "- Stellen Sie sicher, dass die Struktur klar und konsistent ist, um die Lesbarkeit zu gewährleisten.\n\n"
    #     )
    #
    #     structure_overview = (
    #         "## Übersicht über das `ExamQuestions`-Format:\n"
    #         "- `ExamQuestions` ist eine Liste von Prüfungsfragen (`questions`).\n"
    #         "- Jede Prüfungsfrage ist vom Typ `ExamQuestion` und enthält die folgenden Felder:\n"
    #         "  1. **question_content** (erforderlich): Die Hauptfrage und optionale Informationen.\n"
    #         "  2. **example** (erforderlich): Ein Beispiel zur Verdeutlichung der Aufgabenstellung.\n"
    #         "  3. **solution_content** (erforderlich): Die Hauptlösung und optionale Details zur Lösung.\n\n"
    #     )
    #
    #     question_content_details = (
    #         "### Details zu `question_content`:\n"
    #         "- **question (str)**: Die Hauptfrage. Dieses Feld ist immer erforderlich.\n"
    #         "- **optional_question_additional_infos (List[str], optional)**: Zusätzliche Informationen.\n"
    #         "- **optional_question_tables (List[TableContent], optional)**: Tabellen zur Darstellung komplexer Daten. **Diese sollten nur eingesetzt werden, wenn die Darstellung komplexer Daten in der Fragestellng sinnvoll ist.**\n"
    #         + PromptBuilder.get_table_structure_details()
    #     )
    #
    #     example_details = (
    #         "### Details zu `example`:\n"
    #         "- Verwenden Sie dieses Feld, um ein Beispiel bereitzustellen, das das erwartete Verhalten der Turingmaschine verdeutlicht.\n"
    #         "- **Beispiele müssen korrekt, vollständig und direkt relevant für die Aufgabenstellung sein!**\n\n"
    #     )
    #
    #     solution_content_details = (
    #         "### Details zu `solution_content`:\n"
    #         "- **solution (str)**: Die Hauptlösung. Dieses Feld ist immer erforderlich.\n"
    #         "- **optional_solution_additional_infos (List[str], optional)**: Zusätzliche Hinweise, die das Verständnis der Lösung verbessern.\n"
    #         "- **optional_solution_step_by_step (List[str], optional)**: Schritt-für-Schritt-Anleitung der Lösung. VERWENDEN SIE KEINE NUMMERIERUNG!!! **Die Nummerierung erfolgt automatisch!!!**\n"
    #         "- **solution_state_transition_table (TableContent)**: Die Zustandsübergangstabelle, die alle möglichen Zustände und Übergänge der Lösung vollständig beschreibt. Dieses Feld ist verpflichtend.\n"
    #         "- **solution_example_flow_table (TableContent)**: Die Beispielablauftabelle, die den Ablauf der Turingmaschine für das Beispiel dokumentiert. Dieses Feld ist verpflichtend.\n"
    #         "- **optional_additional_solution_tables (List[TableContent], optional)**: Weitere optionale Tabellen zur Unterstützung der Lösung (nur falls erforderlich).\n"
    #         + PromptBuilder.get_table_structure_details()
    #     )
    #
    #     additional_guidelines = (
    #         "## Zusätzliche Hinweise:\n"
    #         "- Verwenden Sie optionale Felder nur, wenn sie die Aufgabe oder Lösung klarer und verständlicher machen.\n"
    #         "- Tabellen sollten nur in der Lösung genutzt werden, um technische Abläufe wie Zustandsübergänge oder Beispielabläufe darzustellen (Außer es wird explizit gefordert).\n"
    #         "- Stellen Sie sicher, dass Tabellen vollständig sind und keine Lücken in der Zustandslogik aufweisen.\n"
    #         "- Unterlassen Sie es, Lösungselemente bereits in der Aufgabenstellung zu nennen.\n"
    #         "- Jede Aufgabe muss klar, konsistent und logisch nachvollziehbar sein.\n\n"
    #     )
    #
    #     return (
    #             header +
    #             general_instructions +
    #             structure_overview +
    #             question_content_details +
    #             example_details +
    #             solution_content_details +
    #             additional_guidelines
    #     )
    #
    # @staticmethod
    # def get_table_structure_details():
    #     return (
    #         "  - Struktur der Tabellen:\n"
    #         "    - **title (str)**: Titel der Tabelle.\n"
    #         "    - **headers (List[str])**: Spaltenüberschriften.\n"
    #         "    - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
    #     )
    #
    # @staticmethod
    # def get_final_reminder(difficulty, difficulty_explanation, num_questions):
    #     header = "# Wichtige abschließende Hinweise!!!:\n\n"
    #
    #     question_count_reminder = (
    #         "## Anzahl der Fragen sicherstellen:\n"
    #         f"- **Überprüfen Sie, ob genau die vorgegebene Anzahl von Fragen {num_questions} generiert wurde.**\n"
    #         "- Stellen Sie sicher, dass keine Fragen fehlen!\n\n"
    #     )
    #
    #     consistency_reminder = (
    #         "## Konsistenz prüfen:\n"
    #         "- Überprüfen Sie jede Aufgabe auf Konsistenz mit der angegebenen Schwierigkeitsstufe.\n"
    #         f"- Stellen Sie sicher, dass keine Aufgabe die Komplexität der gewählten Schwierigkeitsstufe '**{difficulty}**' überschreitet.\n"
    #         f"- Schwierigkeitsgrad '**{difficulty}**' Erklärung: {difficulty_explanation}\n\n"
    #     )
    #
    #     solution_separation_reminder = (
    #         "## Lösungselemente und Tabellenplatzierung:\n"
    #         "- **Keine Elemente der Lösung dürfen in der Aufgabenstellung enthalten sein.**\n"
    #         "- Tabellen dürfen **ausschließlich in der Lösung** und nicht in der Aufgabenstellung verwendet werden, es sei denn, dies ist für das Verständnis der Aufgabe zwingend erforderlich.\n"
    #         "- Stellen Sie sicher, dass Tabellen korrekt formatiert sind und alle Inhalte den Spaltenüberschriften und Zeilen zugeordnet sind. Doppelte oder unvollständige Tabellen sind zu vermeiden.\n\n"
    #     )
    #
    #     table_mapping_reminder = (
    #         "## Tabellen-Mapping:\n"
    #         "- Achten Sie besonders darauf, dass Tabellen nur an den vorgesehenen Stellen erscheinen.\n"
    #         "- Verhindern Sie, dass Lösungstabellen aufgrund von Mapping-Fehlern in der Aufgabenstellung auftauchen.\n"
    #         "- Jede Tabelle muss ausschließlich dort platziert werden, wo sie sinnvoll und inhaltlich korrekt ist.\n\n"
    #     )
    #
    #     quality_reminder = (
    #         "## Aufgabenvalidierung und Qualitätssicherung:\n"
    #         "- **Prüfen Sie jede Aufgabe gründlich**, bevor Sie sie als abgeschlossen betrachten. Nutzen Sie gedankliche Tests, Simulationen und Grenzfallanalysen.\n\n"
    #
    #         "- **Zustandsübergangstabellen:**\n"
    #         "  ⦁ Müssen vollständig, korrekt und ohne Lücken sein.\n"
    #         "  ⦁ Alle möglichen Zustände und Übergänge müssen abgedeckt sein, einschließlich Übergänge an Bandenden (Leerzeichen `■`).\n"
    #         "  ⦁ Iterative Prozesse, falls vorhanden müssen präzise dargestellt und validiert sein.\n\n"
    #
    #         "- **Beispielablauftabellen:**\n"
    #         "  ⦁ Dokumentieren Sie jeden Schritt der Turingmaschine, einschließlich aller Bandinhalte, Kopfpositionen und Zustände.\n"
    #         "  ⦁ Bandinhalte müssen vollständig und korrekt sein, einschließlich Leerzeichen `■` vor und nach der Eingabe.\n"
    #         "  ⦁ Überprüfen Sie, dass keine Zwischenschritte fehlen, und simulieren Sie den Ablauf Schritt für Schritt, um Diskrepanzen zu vermeiden.\n\n"
    #
    #         "- **Beispiel und Ergebnisabgleich:**\n"
    #         "  ⦁ Stellen Sie sicher, dass ein Beispiel vorhanden ist, welches das korrekte Verhalten der Turingmaschine verdeutlicht.\n"
    #         "  ⦁ Überprüfen Sie, ob das Beispiel mit der Zustandsübergangstabelle und der Aufgabenstellung übereinstimmt.\n\n"
    #
    #         "- **Konsistenz und Qualität:**\n"
    #         "  ⦁ Jede Aufgabe muss logisch konsistent, vollständig und realistisch sein. Achten Sie darauf, dass alle Vorgaben der Turingmaschine korrekt umgesetzt werden.\n"
    #         "  ⦁ Unvollständige Zustandsübergänge oder unklare Beschreibungen sind nicht akzeptabel.\n\n"
    #
    #         "- **Grenzfälle prüfen:**\n"
    #         "  ⦁ Testen Sie die Aufgaben mit leeren Eingaben, ungewöhnlichen Kombinationen und anderen Grenzfällen. Verifizieren Sie, dass alle möglichen Szenarien korrekt behandelt werden.\n\n"
    #     )
    #
    #     consequences_reminder = (
    #         "## Bedeutung der Einhaltung der Vorgaben:\n"
    #         "- **Unvollständige oder fehlerhafte Aufgaben mindern den Wert der generierten Ergebnisse und können NICHT für Prüfungszwecke verwendet werden.**\n"
    #         "- **Aufgaben, die nicht den Anforderungen entsprechen, müssen verworfen werden.**\n"
    #         "- **Eine sorgfältige Validierung und Korrektur ist essenziell, um die Qualität und Konsistenz der generierten Aufgaben sicherzustellen.**\n"
    #         "- Ihr Ziel ist es, präzise, vollständige und fehlerfreie Aufgaben zu erstellen, die höchsten Ansprüchen genügen. Daher wird von Ihnen erwartet, alle vorgegebenen Anforderungen konsequent umzusetzen.\n\n"
    #         "**Bitte beachten Sie, dass nur vollständig und korrekt validierte Aufgaben akzeptiert werden können.**"
    #     )
    #
    #     return (
    #             header +
    #             question_count_reminder +
    #             consistency_reminder +
    #             solution_separation_reminder +
    #             table_mapping_reminder +
    #             quality_reminder +
    #             consequences_reminder
    #     )
