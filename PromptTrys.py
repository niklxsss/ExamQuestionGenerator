from Const import *


class PromptBuilder:
# test versuch: Großen Prompt zu verkleinern um overfitting zu vermeiden.... viele MEthoden wie der Reminder, Struktur und die Genaue Beschreibung der Klassenstruktur waren überflüssig 30.11
    @staticmethod
    def create_prefix_prompt(num_questions, difficulty_eng, incorrect_task, files_txt, files_images, files_pdf):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        prompt_parts = [
            PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation),
            # PromptBuilder.get_general_guidelines_prompt(difficulty)
            PromptBuilder.get_general_guidelines3456(difficulty)

            # PromptBuilder.get_task_and_example_prompt(),
            # PromptBuilder.get_solution_prompt(),
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