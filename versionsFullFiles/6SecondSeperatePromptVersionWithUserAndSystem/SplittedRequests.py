from Const import DIFFICULTY_TRANSLATION_MAP, DIFFICULTY_EXPLANATION_MAP
from MessageBuilder import MessageBuilder
from PromptTrys import PromptTrys


class SplittedRequests:

    # für create MEthode:
    # resultaufgabestellung = OpenAIClient.send_request(
    #     SplittedRequests.create_aufgabenstellung_prompt(num_questions, difficulty), TEMPERATURE,
    #     ExamQuestionWithExample)
    # resultZustand = OpenAIClient.send_request(
    #     SplittedRequests.create_zustandsübergangstabelle_prompt(str(resultaufgabestellung)), TEMPERATURE, TableContent)
    # resultbsp = OpenAIClient.send_request(
    #     SplittedRequests.create_Beispielablauftabelle_prompt(str(resultaufgabestellung) + str(resultZustand)),
    #     TEMPERATURE, TableContent)
    # resulta = OpenAIClient.send_request(
    #     SplittedRequests.create_restlösung_prompt(str(resultaufgabestellung) + str(resultZustand) + str(resultbsp)),
    #     TEMPERATURE, ExamQuestion)
    # result = [resulta]


    @staticmethod
    def create_aufgabenstellung_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)
        messages = []

        # System-Prompt hinzufügen, um den Kontext klarzustellen
        system_prompt = MessageBuilder.add_message(
            "system",
            [
                MessageBuilder.add_txt_to_content(
                    "Du bist ein spezialisiertes KI-Modell, das Aufgaben zu Turingmaschinen erstellt. Dein Ziel ist es, "
                    "fehlerfreie, konsistente und qualitativ hochwertige Augaben zu erstellen!\n\n"
                    "Halte dich unbedingt an die Anforderungen des Users!!!\n\n")
            ]
        )
        messages.append(system_prompt)

        # Schritt 1: Basisanforderungen an die Aufgabe
        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    PromptTrys.get_base_prompt(num_questions, difficulty, difficulty_explanation)),
                MessageBuilder.add_txt_to_content(PromptTrys.get_general_guidelines_prompt(difficulty)),
                MessageBuilder.add_txt_to_content(
                    PromptTrys.get_task_and_example_prompt() + "Erstelle die Aufgabenstellung und ein passendes Beispiel. Stelle sicher, dass diese vollständig und fehlerfrei sind."),
            ]
        )
        messages.append(base_prompt)


        assistant_validation_quality = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Überprüfung und Verbesserung der Aufgabe:\n"
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
            )]
        )
        messages.append(assistant_validation_quality)
        #
        return messages

    @staticmethod
    def create_zustandsübergangstabelle_prompt(aufgabenstellung):

        messages = []

        # System-Prompt hinzufügen, um den Kontext klarzustellen
        system_prompt = MessageBuilder.add_message(
            "system",
            [
                MessageBuilder.add_txt_to_content(
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
            ]
        )
        messages.append(system_prompt)


        # Schritt 1: Basisanforderungen an die Aufgabe
        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(f"Aufgabenstellung: {aufgabenstellung}\n\n"
                                                  "Erstellen Sie die Zustandübergangstabelle auf Basis der Aufgabenstellung und des BEispiels!\n"
                                                  ),
            ]
        )
        messages.append(base_prompt)

        assistant_validation_quality = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Überprüfung und Verbesserung der Zustandsübergangstabelle:\n"
                "Stellen Sie sicher, dass die gesamte Zustandsübergangstabelle vollständig, korrekt und konsistent ist. "

                "### Abschließende Validierung:\n"
                "- Stellen Sie sicher, dass die gesamte Zustandsübergangstabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
                "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
                "Verbessern Sie die Zustandsübergangstabelle, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
            )]
        )
        messages.append(assistant_validation_quality)
        #
        return messages

    @staticmethod
    def create_Beispielablauftabelle_prompt(aufgabenstellung):
        messages = []

        # System-Prompt hinzufügen, um den Kontext klarzustellen
        system_prompt = MessageBuilder.add_message(
            "system",
            [
                MessageBuilder.add_txt_to_content(
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
            ]
        )
        messages.append(system_prompt)

        # Schritt 1: Basisanforderungen an die Aufgabe
        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    f"Aufgabenstellung und Zustandstabelle: {aufgabenstellung} \n\n"
                    "Erstellen Sie die Beispielablauftabelle anhand der Aufgabenstellung, Zustandübergangstabelle und des Beispiele. Prüfen Sie danach, dass die Beispielablauftabelle fehlerfrei ist, keine Lücken enthält, alle veränderungen richtig dargstellt werde\n"
                    ),
            ]
        )
        messages.append(base_prompt)

        assistant_validation_quality = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Überprüfung und Verbesserung der Beispielablauftabelle:\n"
                "Stellen Sie sicher, dass die gesamte Beispielablauftabelle vollständig, korrekt und konsistent ist. "

                "### Abschließende Validierung:\n"
                "- Stellen Sie sicher, dass die gesamte Beispielablauftabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
                "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
                "Verbessern Sie die Beispielablauftabelle, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
            )]
        )
        messages.append(assistant_validation_quality)
        #
        return messages

    @staticmethod
    def create_restlösung_prompt(aufgabenstellung):
        messages = []

        # System-Prompt hinzufügen, um den Kontext klarzustellen
        system_prompt = MessageBuilder.add_message(
            "system",
            [
                MessageBuilder.add_txt_to_content(
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
            ]
        )
        messages.append(system_prompt)

        # Schritt 1: Basisanforderungen an die Aufgabe
        base_prompt = MessageBuilder.add_message(
            "user",
            [
                MessageBuilder.add_txt_to_content(
                    f"Aufgabenstellung und Tabelle: {aufgabenstellung}\n\n"
                                                                            "Erstellten Sie den rest der Lösung wie angegeben und baue die Aufgabe im format ExamQuestions zusammen!\n"
                ),
            ]
        )
        messages.append(base_prompt)

        assistant_validation_quality = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Überprüfung und Verbesserung der Aufgabe:\n"
                "Stellen Sie sicher, dass die gesamte Aufgabe vollständig, korrekt und konsistent ist. "

                "### Abschließende Validierung:\n"
                "- Stellen Sie sicher, dass die gesamte Aufgabe den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
                "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
                "Verbessern Sie die Aufgabe, falls Fehler oder Unstimmigkeiten gefunden werden!\n\n"
            )]
        )
        messages.append(assistant_validation_quality)
        #
        return messages