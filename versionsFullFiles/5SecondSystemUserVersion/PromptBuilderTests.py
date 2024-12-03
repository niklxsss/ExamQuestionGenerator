from PromptTrys import PromptTrys
from PromptBuilder import PromptBuilder
from Const import *
from MessageBuilder import MessageBuilder


class PromptBuilderTests:
    # Test User und System Role zu nutzen, aber anstatt alles seperat mir eigener Role zu senden werden hier einige
    # unter user fallende PromptPArts zusammengefasst, um eine konsistentere Generierung zu schaffen

    @staticmethod
    def create_prompt(num_questions, difficulty_eng):
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
                MessageBuilder.add_txt_to_content(PromptBuilderTests.get_base_prompt(num_questions, difficulty, difficulty_explanation)),
                MessageBuilder.add_txt_to_content(PromptBuilderTests.get_general_guidelines_prompt(difficulty)),
                MessageBuilder.add_txt_to_content(PromptBuilderTests.get_task_and_example_prompt() + "Erstelle die Aufgabenstellung und ein passendes Beispiel. Stelle sicher, dass diese vollständig und fehlerfrei sind."),
                MessageBuilder.add_txt_to_content("## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
                                                  "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
                                                  "- Achten Sie genau auf die Startposition des Lesekopfes und stellen Sie sicher, dass alle Bewegungen und Übergänge in den Tabellen entsprechend der Aufgabenstellung angewendet werden.\n"
                                                  "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
                                                  "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"

                                                  "## Zustandsübergangstabelle ('solution_state_transition_table'):**\n"
                                                  "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
                                                  "- **Spaltenstruktur:** Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
                                                  "- **Vollständigkeit:** Alle möglichen Zustände (inkl Start- & Endzustände) und Übergänge, einschließlich Sonderzeichen wie Leerzeichen `■`, müssen abgedeckt sein.\n"
                                                  "- **Logik und Effizienz:** Wählen Sie immer die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne dabei notwendige Zustände oder Schritte auszulassen.\n\n"
                                                  "Erstellen Sie zuerst die Zustandübergangstabelle auf Basis der Aufgabenstellung und des BEispiels und prüfen/korrigieren diese\n"
                                                  ),

                MessageBuilder.add_txt_to_content(
                                                  "## Beispielablauftabelle ('solution_example_flow_table'):**\n"
                                                  "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
                                                  "- **Spaltenstruktur:** Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
                                                  "- **Kopfposition:** Als Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE! Diese Nummerierung ist unabhängig von der Startposition des Lesekopfes auf dem Band und bezieht sich nur auf die aktuelle Position des Kopfes während des Ablaufs der Maschine.\n"
                                                  "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen (inkl. die Begrenzungsleerzeichen links und rechts von der Eingabe) an **und markieren Sie zusätzlich die aktive Kopfposition im Bandinhalt durch die Umrahmung [ ]!**\n"
                                                  # "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■11[0]10■)!\n"
                                                  "- **Anwendung der Übergangsregeln:** Stellen Sie sicher, dass die Übergangsregeln korrekt umgesetzt werden, indem der Bandinhalt nach jedem Schreibvorgang aktualisiert und die Kopfbewegung entsprechend der Zustandsübergangstabelle dokumentiert wird.\n\n"
                                                  "Erstellen Sie die Beispielablauftabelle anhand der Aufgabenstellung, Zustandübergangstabelle und des Beispiele. Prüfen Sie danach, dass die Beispielablauftabelle fehlerfrei ist, keine Lücken enthält, alle veränderungen richtig dargstellt werde\n"
                ),

                MessageBuilder.add_txt_to_content(
                                                  "## Zusätzliche Tabellen ('optional_additional_solution_tables'):**\n"
                                                  "- **Verwendungszweck:** Zusätzliche Tabellen können optional verwendet werden, um komplexe Aufgaben klarer zu erklären, bspw durch Zustandsbeschreibungstabellen etc.\n\n"
                              
                                                  "## Spezifische Anforderungen an die Lösung:\n"
                                                  "- **Lösung ('solution')**: Geben sie eine konzeptionelle Beschreibung des Lösungsansatzes an.\n"
                                                  "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
                                                  "- **Lösungsweg ('optional_solution_step_by_step')**: Beschreiben Sie optional den Lösungsweg in Textform, Schritt für Schritt, ohne Tabellen oder Aufzählungszeichen.\n\n"
                                                  "Erstellten Sie den rest der Lösung wie angegeben!\n"
                )
            ]
        )
        messages.append(base_prompt)


        assistant_validation_quality = MessageBuilder.add_message(
            "user",
            [MessageBuilder.add_txt_to_content(
                "## Überprüfung und Verbesserung der Aufgabe:\n"
                "Stellen Sie sicher, dass die gesamte Aufgabe inklusive aller Tabellen und Beschreibungen vollständig, korrekt und konsistent ist. "
                "Die Überprüfung umfasst folgende Aspekte:\n\n"

                "### Aufgabenstellung und Beispiel:\n"
                "- Überprüfen Sie, ob die Aufgabenstellung klar, präzise und vollständig ist.\n"
                "- Stellen Sie sicher, dass das Beispiel korrekt und auf die Aufgabenstellung abgestimmt ist.\n"
                "- Prüfen Sie, ob die Zusatzinformationen mit der Aufgabenstellung übereinstimmen und keine widersprüchlichen Angaben enthalten.\n\n"

                "### Zustandsübergangstabelle ('solution_state_transition_table'):\n"
                "- Überprüfen Sie, ob alle Zustände und Übergänge vollständig und korrekt abgebildet sind.\n"
                "- Stellen Sie sicher, dass die Spaltenstruktur eingehalten wurde (Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand).\n"
                "- Prüfen Sie die Konsistenz mit der Aufgabenstellung und dem Beispiel.\n"
                "- Stellen Sie sicher, dass alle möglichen Zustände (inkl. Start- und Endzustände) abgedeckt sind.\n\n"

                "### Beispielablauftabelle ('solution_example_flow_table'):\n"
                "- Stellen Sie sicher, dass der Ablauf der Turingmaschine korrekt wiedergegeben wurde.\n"
                "- Überprüfen Sie, ob die Schritte mit den Übergangsregeln der Zustandsübergangstabelle übereinstimmen.\n"
                "- Prüfen Sie die Kopfpositionen: Sind diese korrekt nummeriert und stimmen sie mit dem Ablauf überein?\n"
                "- Stellen Sie sicher, dass die Bandinhalte nach jeder Operation korrekt aktualisiert wurden, einschließlich der Markierung der aktiven Kopfposition ([ ]).\n\n"

                "### Lösung und Qualitätssicherung:\n"
                "- Überprüfen Sie, ob die konzeptionelle Beschreibung des Lösungsansatzes klar und präzise ist.\n"
                "- Stellen Sie sicher, dass alle zusätzlichen Informationen korrekt und verständlich sind.\n"
                "- Prüfen Sie, ob der schrittweise Lösungsweg alle erforderlichen Details enthält.\n"
                "- Vergewissern Sie sich, dass die Lösung den höchsten Qualitätsstandards entspricht.\n\n"

                "### Fehlerkorrektur:\n"
                "- Identifizieren und korrigieren Sie alle Fehler, die während der Überprüfung festgestellt werden.\n"
                "- Passen Sie inkonsistente oder fehlerhafte Tabellen und Beschreibungen an.\n"
                "- Generieren Sie bei Bedarf neue Tabellen, die den Anforderungen entsprechen.\n\n"

                "### Abschließende Validierung:\n"
                "- Stellen Sie sicher, dass die gesamte Aufgabe den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
                "- Überprüfen Sie, ob alle Abschnitte konsistent zueinander sind und keine logischen Widersprüche enthalten.\n\n"
                "Verbessern Sie die Aufgabe, falls Fehler oder Unstimmigkeiten gefunden werden!"
            )]
        )
        messages.append(assistant_validation_quality)
        #
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

