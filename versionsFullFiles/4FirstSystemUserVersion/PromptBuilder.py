from Const import *
from MessageBuilder import MessageBuilder


class PromptBuilder:

    # ----------Verusch mit system u user u assistant zu arbeiten um mehr strukur zu schaffen------------

    @staticmethod
    def create_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)
        # Liste für die Nachrichtenstruktur
        messages = []

        # System-Prompt hinzufügen
        system_prompt = MessageBuilder.add_message(
            "system",
            [MessageBuilder.add_txt_to_content(
                "Du bist ein KI-Modell, das Prüfungsaufgaben zu Turingmaschinen generiert. Jede Aufgabe muss präzise, fehlerfrei und den spezifischen Anforderungen entsprechen."
            )]
        )
        messages.append(system_prompt)

        # Schritt 1: Aufgabenbeschreibung (Base Prompt)
        base_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation)
            )]
        )
        messages.append(base_prompt)

        # Schritt 2: Allgemeine Anforderungen und Einschränkungen
        general_guidelines = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                PromptBuilder.get_general_guidelines_prompt(difficulty)
            )]
        )
        messages.append(general_guidelines)

        # Schritt 3: Anforderungen an die Aufgabenstellung und Zusatzinformationen
        task_and_example_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                PromptBuilder.get_task_and_example_prompt() + "Erstellen Sie Die Aufgabenstellung + Beispiel nach den "
                                                              "Vorgaben! Überprüfe danach, ob die Aufgabenstellung, die Zusatzinfos und das BEispiel konsistent sind!"
            )]
        )
        messages.append(task_and_example_prompt)
        #
        # Assistant: Überprüfung der Aufgabenstellung
        assistant_validation = MessageBuilder.add_message(
            # "assistant",
            "user",
            [MessageBuilder.add_txt_to_content(
                "Stelle sicher, dass die Aufgabenstellung, Zusatzinformationen und das Beispiel klar und konsistent sind. Prüfe insbesondere auf Widersprüche.\n\n"
            )]
        )
        messages.append(assistant_validation)


        # Schritt 7: Anforderungen an die Lösung
        solution_prompt = MessageBuilder.add_message(
            # "user",
            "system",
            [MessageBuilder.add_txt_to_content(
                # "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
                # "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
                # "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
                # "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
                # "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"

                "Du bist ein KI-Modell, das detaillierte Zustandsübergangstabellen und Beispielablauftabellen für Turingmaschinen erstellt. Beachte immer: "
                "Die Zustandsübergangstabelle und die Beispielablauftabelle müssen vollständig und konsistent sein. "
                "Jede Regel und jeder Schritt müssen mit der Aufgabenstellung und dem Beispiel übereinstimmen."

                "Jede Tabelle muss:**\n"
                "1. Präzise und fehlerfrei sein.\n"
                "2. Vollständig alle Übergänge und Zustände abdecken.\n"
                "3. Konsistent mit der Aufgabenstellung und dem Beispiel sein.\n"
                "4. Die Kopfbewegung und Bandänderungen korrekt darstellen.\n\n"

                "**Qualitätsanforderungen**:\n"
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


            )]
        )
        messages.append(solution_prompt)

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
        solution_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                # "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
                # "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
                # "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
                # "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
                # "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
                # "Erstelle die Zustandsübergangstabelle basierend auf der Aufgabenstellung und dem Beispiel. Jede Regel muss korrekt und konsistent sein. Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, korrigiere diese!!\n\n"
                #
                # "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
                # "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
                # "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
                # "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
                # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
                # # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
                # "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
                # "Erstelle die Beispielablauftabelle auf Basis der Aufgabenstellung des Beispiels und der Zustandsübergangstabelle. Überprüfe danach selbst ob sie mit der Zustandstabelle übereinstimmt und falls Fehler auftreten, korrigiere diese!\n"
                # # "Erstellen Sie die Beispielablauftabelle auf Basis der Aufgabenstellung, des BEispiels und der Zustandsübergangstabelle FEHLERFREI!\n\n"
                "Erstelle die Zustandsübergangstabelle und Beispielablauftabelle basierend auf der Aufgabenstellung, dem Beispiel und den definierten Qualitätsanforderungen . Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, KORRIGIERE diese!!\n\n"

            )]
        )
        messages.append(solution_prompt)

        # Assistant: Überprüfung der Lösung
        assistant_validation = MessageBuilder.add_message(
            "assistant",
            # "user",
            [MessageBuilder.add_txt_to_content(
                # "Prüfe die Zustandsübergangstabelle auf:\n"
                # "- Vollständigkeit (alle Zustände und Übergänge abgedeckt)\n"
                # "- Konsistenz mit der Aufgabenstellung und dem Beispiel\n"
                # "- Wenn der Übertrag abgeschlossen ist, bewegt sich der Kopf korrekt zur Ruheposition.\n"
                # "- Effizienz der Übergänge. Korrigiere logische Fehler und füge fehlende Zustände hinzu.\n\n"
                #
                # "Prüfe die erstellte Beispielablauftabelle auf folgende Punkte:\n"
                # "- Stimmen die Schritte und Kopfpositionen mit den Übergangsregeln der Zustandsübergangstabelle überein?\n"
                # "- Sind alle Bandinhalte korrekt nach jeder Operation aktualisiert worden?\n"
                # "- Gibt es Abweichungen zwischen den Zustandswechseln und der Tabelle? Wenn ja, korrigiere diese.\n\n"

                "Überprüfe die Zustandsübergangstabelle und die Beispielablauftabelle auf Konsistenz. "
                "Stimmen alle Übergänge mit der Aufgabenstellung und dem Beispiel überein? "
                "Falls nein, korrigiere die Fehler und generiere die Tabellen neu."
            )]
        )
        messages.append(assistant_validation)


        # ------------------End----------------------------------------------------------------------------------------------e


        solution_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Spezifische Anforderungen an die Lösung:\n"
                "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
                "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
                "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
                "Erstelle die vollständige Lösung mit einer konzeptionellen Beschreibung, zusätzlichen Informationen und einem schrittweisen Lösungsweg.!!\n\n"
            )]
        )
        messages.append(solution_prompt)

        # Assistant: Überprüfung der Lösung
        assistant_validation = MessageBuilder.add_message(
            "assistant",
            # "user",
            [MessageBuilder.add_txt_to_content(
                "Prüfe die gesamte Lösung auf:\n"
                "- Konsistenz zwischen Beispiel, Zustandsübergangstabelle und Beispielablauftabelle.\n"
                "- Fehlerfreiheit in den Tabellen.\n"
                "- Eindeutigkeit und Klarheit der konzeptionellen Beschreibung.\n"
                "Verbessere inkonsistente oder fehlerhafte Abschnitte.\n\n"
            )]
        )
        messages.append(assistant_validation)

        # Schritt 8: Qualitätssicherung
        quality_prompt = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                PromptBuilder.get_quality_prompt()
            )]
        )
        messages.append(quality_prompt)

        # Assistant: Überprüfung der Qualitätssicherung
        assistant_validation = MessageBuilder.add_message(
            "assistant",
            # "user",
            [MessageBuilder.add_txt_to_content(
                "Stelle sicher, dass die Qualitätssicherungsanforderungen vollständig erfüllt sind."
            )]
        )
        messages.append(assistant_validation)

        return messages





    @staticmethod
    def get_base_prompt(num_questions, difficulty, difficulty_explanation):
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
    def get_general_guidelines_prompt(difficulty):
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
    def get_task_and_example_prompt():
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



    # ------------------------------------------------------Andere Version

    # ---------------------Versuch die Prompt Parts in immer neuen user und system roles an die KI zu geben-----------------------

    # @staticmethod
    #     def create_prompt(num_questions, difficulty_eng):
    #         difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
    #         difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)
    #         # Liste für die Nachrichtenstruktur
    #         messages = []
    #
    #         # System-Prompt hinzufügen
    #         system_prompt = MessageBuilder.add_message(
    #             "system",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Du bist ein KI-Modell, das Prüfungsaufgaben zu Turingmaschinen generiert. Jede Aufgabe muss präzise, fehlerfrei und den spezifischen Anforderungen entsprechen."
    #             )]
    #         )
    #         messages.append(system_prompt)
    #
    #         # Schritt 1: Aufgabenbeschreibung (Base Prompt)
    #         base_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation)
    #             )]
    #         )
    #         messages.append(base_prompt)
    #
    #         # Schritt 2: Allgemeine Anforderungen und Einschränkungen
    #         general_guidelines = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 PromptBuilder.get_general_guidelines_prompt(difficulty)
    #             )]
    #         )
    #         messages.append(general_guidelines)
    #
    #         # Schritt 3: Anforderungen an die Aufgabenstellung und Zusatzinformationen
    #         task_and_example_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 PromptBuilder.get_task_and_example_prompt() + "Erstellen Sie Die Aufgabenstellung + Beispiel nach den "
    #                                                               "Vorgaben! Überprüfe danach, ob die Aufgabenstellung, die Zusatzinfos und das BEispiel konsistent sind!"
    #             )]
    #         )
    #         messages.append(task_and_example_prompt)
    #         #
    #         # Assistant: Überprüfung der Aufgabenstellung
    #         assistant_validation = MessageBuilder.add_message(
    #             # "assistant",
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Stelle sicher, dass die Aufgabenstellung, Zusatzinformationen und das Beispiel klar und konsistent sind. Prüfe insbesondere auf Widersprüche.\n\n"
    #             )]
    #         )
    #         messages.append(assistant_validation)
    #
    #
    #         # Schritt 7: Anforderungen an die Lösung
    #         solution_prompt = MessageBuilder.add_message(
    #             # "user",
    #             "system",
    #             [MessageBuilder.add_txt_to_content(
    #                 "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
    #                 "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
    #                 "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
    #                 "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
    #                 "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
    #             )]
    #         )
    #         messages.append(solution_prompt)
    #
    #         solution_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
    #                 "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
    #                 "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
    #                 "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
    #                 "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
    #                 "Erstelle die Zustandsübergangstabelle basierend auf der Aufgabenstellung und dem Beispiel. Jede Regel muss korrekt und konsistent sein. Überprüfe danach selbst ob sie mit dert Aufgabenstellung und dem Beispiel übereinstimmt und falls Fehler auftreten, korrigiere diese!!\n\n"
    #             )]
    #         )
    #         messages.append(solution_prompt)
    #
    #         # Assistant: Überprüfung der Lösung
    #         assistant_validation = MessageBuilder.add_message(
    #             # "assistant",
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Prüfe die Zustandsübergangstabelle auf:\n"
    #                 "- Vollständigkeit (alle Zustände und Übergänge abgedeckt)\n"
    #                 "- Konsistenz mit der Aufgabenstellung und dem Beispiel\n"
    #                 "- Effizienz der Übergänge. Korrigiere logische Fehler und füge fehlende Zustände hinzu.\n\n"
    #             )]
    #         )
    #         messages.append(assistant_validation)
    #
    #         solution_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
    #                 "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
    #                 "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
    #                 "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
    #                 "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!\n"
    #                 # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
    #                 "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
    #                 "Erstelle die Beispielablauftabelle. Überprüfe danach selbst ob sie mit der Zustandstabelle übereinstimmt und falls Fehler auftreten, korrigiere diese!\n"
    #                 # "Erstellen Sie die Beispielablauftabelle auf Basis der Aufgabenstellung, des BEispiels und der Zustandsübergangstabelle FEHLERFREI!\n\n"
    #             )]
    #         )
    #         messages.append(solution_prompt)
    #
    #         # Assistant: Überprüfung der Lösung
    #         assistant_validation = MessageBuilder.add_message(
    #             # "assistant",
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Prüfe die erstellte Beispielablauftabelle auf folgende Punkte:\n"
    #                 "- Stimmen die Schritte und Kopfpositionen mit den Übergangsregeln der Zustandsübergangstabelle überein?\n"
    #                 "- Sind alle Bandinhalte korrekt nach jeder Operation aktualisiert worden?\n"
    #                 "- Gibt es Abweichungen zwischen den Zustandswechseln und der Tabelle? Wenn ja, korrigiere diese.\n\n"
    #             )]
    #         )
    #         messages.append(assistant_validation)
    #
    #         solution_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "## Spezifische Anforderungen an die Lösung:\n"
    #                 "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
    #                 "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
    #                 "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
    #                 "Erstelle die vollständige Lösung mit einer konzeptionellen Beschreibung, zusätzlichen Informationen und einem schrittweisen Lösungsweg.!!\n\n"
    #             )]
    #         )
    #         messages.append(solution_prompt)
    #
    #         # Assistant: Überprüfung der Lösung
    #         assistant_validation = MessageBuilder.add_message(
    #             # "assistant",
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Prüfe die gesamte Lösung auf:\n"
    #                 "- Konsistenz zwischen Beispiel, Zustandsübergangstabelle und Beispielablauftabelle.\n"
    #                 "- Fehlerfreiheit in den Tabellen.\n"
    #                 "- Eindeutigkeit und Klarheit der konzeptionellen Beschreibung.\n"
    #                 "Verbessere inkonsistente oder fehlerhafte Abschnitte.\n\n"
    #             )]
    #         )
    #         messages.append(assistant_validation)
    #
    #         # Schritt 8: Qualitätssicherung
    #         quality_prompt = MessageBuilder.add_message(
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 PromptBuilder.get_quality_prompt()
    #             )]
    #         )
    #         messages.append(quality_prompt)
    #
    #         # Assistant: Überprüfung der Qualitätssicherung
    #         assistant_validation = MessageBuilder.add_message(
    #             # "assistant",
    #             "user",
    #             [MessageBuilder.add_txt_to_content(
    #                 "Stelle sicher, dass die Qualitätssicherungsanforderungen vollständig erfüllt sind."
    #             )]
    #         )
    #         messages.append(assistant_validation)
    #
    #         return messages