from Const import *


class PromptBuilder:

    @staticmethod
    def create_prefix_prompt(num_questions, difficulty_eng, incorrect_task, files_txt, files_images, files_pdf):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        prompt_parts = [
            PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation),
            PromptBuilder.get_general_guidelines(difficulty),
        ]

        if incorrect_task:
            prompt_parts.append(PromptBuilder.get_incorrect_task_prompt())

        if any([files_txt, files_images, files_pdf]):
            prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))

        return prompt_parts

    @staticmethod
    def create_suffix_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        return [
            PromptBuilder.get_process_steps(difficulty),
            PromptBuilder.get_structure_instructions(),
            PromptBuilder.get_final_reminder(difficulty, difficulty_explanation, num_questions)
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
    def get_general_guidelines(difficulty):
        return (
            "# Grundlegende Anforderungen:\n\n"

            "## Allgemeine Anforderungen:\n"
            "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
            "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
            "- **Keine Spoiler:** Vermeiden Sie in der Aufgabenstellung (inkl Zusatzinformationen & Beispiel) jegliche Hinweise, die auf die Lösung oder den Lösungsweg schließen lassen. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
            "- **Lösungsbezug:** Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n\n"

            "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
            "- **Strikte Trennung:** Die 'question' darf **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
            "- **Verbot für technische Details in der Frage:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
            "- **Vermeiden Sie unklare oder mehrdeutige Formulierungen, die zu unterschiedlichen Interpretationen führen können.**\n\n"
            
            "## Spezifische Anforderungen an die Zusatzinformationen (optional_question_additional_infos):\n"
            "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` als Klartext, NICHT im LaTeX-Format (z. B. cdot oder u25a0). \n"
            "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
            "- **Startposition und Endzustand:** Geben Sie eindeutig an, an welcher Position der Lese-/Schreibkopf der Turingmaschine startet und wo er nach Abschluss stehen bleibt. Geben Sie dabei immer die Seite der Eingabe (links oder rechts) an. Achte dabei auch darauf, welche Start und Endposition sich durch die Aufgabenstellung anbietet!\n"
            "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten, Prinzipien oder methodischen Ansätzen basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n"
            "Diese Details sind nur in den Zusatzinformationen erlaubt.\n\n"
            
            "## Anforderungen an das Beispiel:\n"
            "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, dass im Kontext der Aufgabe am meisten Sinn macht.\n"
            "- **Korrekte Darstellung:** Die Eingabe und der daraus resultierende Output müssen **inklusive der Leerzeichen-Symbole `■` am Anfang und Ende** dargestellt werden, um die Konsistenz mit der Bandrepräsentation zu gewährleisten. Bsp: `■11010■`\n"
            "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n\n"
            
            "## Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Lösung MUSS den Anforderungen und der Zielsetzung der Aufgabenstellung genau entsprechen.\n"
            "- Vermeiden Sie jegliche Abweichungen oder Annahmen, die nicht in der Aufgabenstellung beschrieben sind.\n"
            "- Überprüfen Sie, dass alle Zusatzinformationen korrekt in die Lösung integriert wurden.\n\n"
            
            "## Einfachheit und Effizienz:\n"
            "- Die Aufgabe soll so starten und enden, dass der Ablauf der Turingmaschine am kürzesten ist!"
            "- Die Lösung der Aufgabe (einschließlich Zustandsübergangstabelle und Beispielablauftabelle) MUSS die Anforderungen auf die einfachste und effizienteste Weise erfüllen.\n"
            "- Vermeiden Sie unnötige Zustände, Übergänge oder komplexe Abläufe, die nicht erforderlich sind, um eine tendenziell einfache Aufgabe korrekt zu lösen.\n"
            "- Jede Aufgabe und Lösung soll den kürzesten und klarsten Weg zur Erfüllung der Anforderungen beschreiben.\n\n"
            
            "## Spezifische Anforderungen an die Lösung:\n"
            "- **Zustandsübergangstabellen:** Zustandsübergangstabellen müssen alle möglichen Zustände und Übergänge abdecken, **EINSCHLIEßLICH Anfangs- und Endzuständen **. **Unvollständige Tabellen oder fehlende Zustände sind nicht akzeptabel.**\n"
            "- **Beispielablauftabelle:** Beispielablauftabelle müssen den Ablauf der Turingmaschine komplett Schritt für Schritt anhand des Beispiels aufzeigen.\n"
            "- **Alle Tabellen und Abläufe müssen logisch und fehlerfrei sein!**\n"

            "## Einschränkungen und Komplexität:\n"
            "- **Turingmaschinen-Kompatibilität:** Aufgaben müssen realistisch mit einer Standard-Turingmaschine lösbar sein und dürfen keine zusätzlichen Speicher- oder Zählmechanismen voraussetzen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen.\n"
            f"- **Komplexitätsniveau:** Halten Sie die Komplexität der Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
            "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"

            "## Qualitätssicherung:\n"
            "- **Testfälle:** Überprüfen Sie jede Aufgabe mit mehreren Testfällen, um Konsistenz und Korrektheit der Lösung sicherzustellen.\n"
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
    def get_process_steps(difficulty):
        return (
            "# Ablauf der Prüfungsfrage-Generierung:\n\n"

            "## Wichtiger Hinweis:\n"
            "- **Halten Sie sich strikt an die unten angegebene Abfolge der Schritte, um sicherzustellen, dass keine Fehler oder Unvollständigkeiten auftreten.**\n"
            "- **Jeder Schritt muss vollständig abgeschlossen sein, bevor mit dem nächsten fortgefahren wird.**\n\n"

            "##Der folgende Ablauf gewährleistet, dass die generierten Prüfungsaufgaben korrekt, vollständig und für Prüfungen geeignet sind:\n\n"

            "1. **Aufgabenart bestimmen:**\n"
            "   Wählen Sie die Art der Aufgabe, falls nicht vorgegeben, und stellen Sie sicher, dass die Aufgabenstellung vollständig, präzise und klar ist. "
            "Alle Aufgaben müssen auf realistisch umsetzbaren Operationen einer Turingmaschine basieren.\n\n"

            f"2. **Schwierigkeitsstufe prüfen:**\n"
            f"   Die Aufgaben müssen auf dem Schwierigkeitsgrad **{difficulty}** bleiben. Stellen Sie sicher, dass die Aufgabenstellung den Anforderungen "
            f"dieser Stufe entspricht. Vermeiden Sie plötzliche Sprünge in der Komplexität.\n\n"

            "3. **Kohärenz und Umsetzbarkeit sicherstellen:**\n"
            "   Vergewissern Sie sich, dass die Aufgaben auf der gewählten Schwierigkeitsstufe realistisch, kohärent und umsetzbar sind. "
            "Die Komplexität sollte so gehalten werden, dass die Aufgabe korrekt gelöst werden kann.\n\n"
            
            "4. **Aufgabenstellung und Zusatzinformationen erstellen:**\n"
            "- **Formulieren Sie die Frage ('question'), die nur das Problem beschreibt.**\n"
            "- **Überprüfen Sie, ob die Frage keine technischen Details enthält.**\n"
            "- **Fügen Sie die technischen Details ausschließlich in die Zusatzinformationen ('optional_question_additional_infos') ein.**\n"
            "- **Finalisieren Sie die Frage, indem Sie sicherstellen, dass keine Redundanzen oder Widersprüche zwischen Frage und Zusatzinformationen bestehen.**\n\n"

            "5. **Beispiele hinzufügen:**\n"
            "   Generieren Sie ein Beispiel, welches zur Verdeutlichung der Aufgabenstellung dient. "
            "**Stellen Sie sicher, dass das Beispiel korrekt ist** und die Anforderungen der Aufgabenstellung erfüllt!.\n\n"

            "6. **Lösung entwickeln:**\n"
            "   Formulieren Sie eine klare und vollständige Lösung, die direkt zur Aufgabenstellung passt. "
            "Erklären Sie alle Schritte nachvollziehbar, falls es der Aufgabentyp erfordert und achten Sie darauf, dass die Lösung alle Anforderungen abdeckt.\n\n"
            
            "7. **Zustandsübergangstabelle erstellen:**\n"
            "   **Erstellen Sie eine vollständige und KORREKTE Zustandsübergangstabelle, die alle möglichen Zustände, Übergänge und alle Zwischenschritte abdeckt und exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n"
            "- Stellen Sie sicher, dass Übergänge am Bandende (Leerzeichen `■`) korrekt behandelt werden.\n"
            "- Vermeiden Sie Zustands- oder Übergangslücken, insbesondere bei komplexen Aufgaben.\n"
            "- Vermeiden Sie unnötige Zustände oder Übergänge.\n"
            "- Stellen Sie sicher, dass alle Zustände und Übergänge fehlerfrei und konsistent mit der Aufgabenstellung sind.\n"
            "- Validieren Sie die Tabelle, indem Sie die Simulation Schritt für Schritt prüfen und sicherstellen, dass keine Zustände übersprungen werden.\n\n"

            "8. **Überprüfung der Zustandsübergangstabelle:**\n"
            "   Testen Sie die Zustandsübergangstabelle umfassend!.\n"
            "Stellen Sie sicher, dass alle Übergänge vollständig und korrekt beschrieben sind und die Tabelle alle notwendigen Schritte abbildet! (keine Zustände oder Schritte dürfen fehlen).\n"
            "Die Tabelle muss konsistent mit der Aufgabenstellung und dem Beispiel sein.\n\n"

            "9. **Beispielablauftabelle ergänzen:**\n"
            "   - Erstellen Sie eine Beispielablauftabelle, die jeden erforderlichen Schritt der Turingmaschine dokumentiert (in der Reihenfolge: Schritt, aktueller Zustand, Bandzustand, Kopfposition).\n"
            "- In der Spalte Kopfposition ist ausschließlich der numerische Wert der aktuellen Position des Lesekopfes anzugeben. DIE KOPFPOSITION BEGINNT IMMER MIT DER NUMMERIERUNG **1** UND FOLGT SEQUENTIELL JEDEM SCHRITT DER TURINGMASCHINE.! Dies ist unabhängig davon, ob die Position initial auf einem Leerzeichen, einem Eingabezeichen oder einem Bandende-Symbol liegt.\n"
            "- In der Spalte Bandinhalt muss der gesamte Bandinhalt einschließlich der Leerzeichen vor und nach der Eingabe angegeben werden. Zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] zu kennzeichnen (Beispiel: ■[1]000■).\n"
            "- Diese Tabelle MUSS exakt die Übergänge und Ergebnisse der Maschine darstellen und konsistent mit der Zustandsübergangstabelle sowie der Aufgabenstellung und dem Beispiel sein.\n"
            # "-  Überflüssige oder redundante Schritte müssen entfernt werden.\n"
            # "- Validieren Sie, dass die Tabelle vollständig ist und keine Zwischenschritte oder Bandinhalte fehlen, einschließlich Leerzeichen `■` vor und nach der Eingabe.\n"
            # "- Achten Sie darauf, falls die Aufgabe auf iterative Prozesse angewiesen ist, dass diese korrekt und vollständig durchlaufen werden und dokumentiert sind.\n"
            "- Simulieren Sie die Schritte und korrigieren Sie Diskrepanzen, bis alle Anforderungen erfüllt und alle Zwischenschritte vollständig sind.\n\n"

            "10. **Kombinierte Überprüfung der Tabellen:**\n"
            "   **Sobald die Zustandsübergangstabelle und die Beispielablauftabelle erstellt wurden, müssen diese umfassend getestet werden.**\n"
            "- **Prüfen Sie, ob beide Tabellen vollständig und fehlerfrei sind und ob sie konsistent miteinander sowie mit der Aufgabenstellung und dem Beispiel übereinstimmen.**\n\n"

            "11. **Weitere Tabellen ergänzen wenn nötig:**\n"
            "   Falls zu den bestehenden Tabellen zusätzliche Tabellen für die Lösung erforderlich sind, ergänzen Sie diese unter `optional_additional_solution_tables`.\n"
            "Stellen Sie sicher, dass alle zusätzlichen Tabellen korrekt, vollständig und konsistent mit den Haupttabellen sind.\n\n"

            "12. **Abschließende Prüfung:**\n"
            "   Validieren Sie jede Aufgabe umfassend, indem Sie folgende Schritte iterativ durchführen:\n"
            "- **Übergangsvalidierung:** Stellen Sie sicher, dass die Zustandsübergangstabelle vollständig und korrekt ist. Alle Zustände und Übergänge müssen vorhanden sein, einschließlich Bandende- und Sonderzeichen-Übergängen (■).\n"
            "- **Simulation:** Simulieren Sie jeden Schritt der Aufgabe. Die Simulation muss zeigen, dass die Turingmaschine alle Übergänge korrekt umsetzt und das erwartete Ergebnis liefert.\n"
            "- **Grenzfalltests:** Testen Sie die Aufgabe mit leeren Eingaben, ungültigen Zeichen oder ungewöhnlichen Kombinationen. Validieren Sie, dass die Maschine korrekt darauf reagiert.\n"
            "- **Ergebnisabgleich:** Überprüfen Sie, ob das Ergebnis der Simulation exakt den Anforderungen der Aufgabenstellung entspricht.\n"
            "Eine Aufgabe darf erst zurückgegeben werden, wenn alle Tests erfolgreich abgeschlossen sind. **Fehlerhafte oder unvollständige Aufgaben sind unzulässig!**\n\n"
        )

    @staticmethod
    def get_structure_instructions():
        header = "# Struktur der Prüfungsaufgaben:\n\n"

        general_instructions = (
            "## Allgemeine Richtlinien:\n"
            "- Die Prüfungsaufgaben und Lösungen sollen im `ExamQuestions`-Response-Format strukturiert sein.\n"
            "- Verwenden Sie optionale Felder nur, wenn sie die Aufgabe oder Lösung klarer und verständlicher machen.\n"
            "- Stellen Sie sicher, dass die Struktur klar und konsistent ist, um die Lesbarkeit zu gewährleisten.\n\n"
        )

        structure_overview = (
            "## Übersicht über das `ExamQuestions`-Format:\n"
            "- `ExamQuestions` ist eine Liste von Prüfungsfragen (`questions`).\n"
            "- Jede Prüfungsfrage ist vom Typ `ExamQuestion` und enthält die folgenden Felder:\n"
            "  1. **question_content** (erforderlich): Die Hauptfrage und optionale Informationen.\n"
            "  2. **example** (erforderlich): Ein Beispiel zur Verdeutlichung der Aufgabenstellung.\n"
            "  3. **solution_content** (erforderlich): Die Hauptlösung und optionale Details zur Lösung.\n\n"
        )

        question_content_details = (
            "### Details zu `question_content`:\n"
            "- **question (str)**: Die Hauptfrage. Dieses Feld ist immer erforderlich.\n"
            "- **optional_question_additional_infos (List[str], optional)**: Zusätzliche Informationen.\n"
            "- **optional_question_tables (List[TableContent], optional)**: Tabellen zur Darstellung komplexer Daten. **Diese sollten nur eingesetzt werden, wenn die Darstellung komplexer Daten in der Fragestellng sinnvoll ist.**\n"
            + PromptBuilder.get_table_structure_details()
        )

        example_details = (
            "### Details zu `example`:\n"
            "- Verwenden Sie dieses Feld, um ein Beispiel bereitzustellen, das das erwartete Verhalten der Turingmaschine verdeutlicht.\n"
            "- **Beispiele müssen korrekt, vollständig und direkt relevant für die Aufgabenstellung sein!**\n\n"
        )

        solution_content_details = (
            "### Details zu `solution_content`:\n"
            "- **solution (str)**: Die Hauptlösung. Dieses Feld ist immer erforderlich.\n"
            "- **optional_solution_additional_infos (List[str], optional)**: Zusätzliche Hinweise, die das Verständnis der Lösung verbessern.\n"
            "- **optional_solution_step_by_step (List[str], optional)**: Schritt-für-Schritt-Anleitung der Lösung. VERWENDEN SIE KEINE NUMMERIERUNG!!! **Die Nummerierung erfolgt automatisch!!!**\n"
            "- **solution_state_transition_table (TableContent)**: Die Zustandsübergangstabelle, die alle möglichen Zustände und Übergänge der Lösung vollständig beschreibt. Dieses Feld ist verpflichtend.\n"
            "- **solution_example_flow_table (TableContent)**: Die Beispielablauftabelle, die den Ablauf der Turingmaschine für das Beispiel dokumentiert. Dieses Feld ist verpflichtend.\n"
            "- **optional_additional_solution_tables (List[TableContent], optional)**: Weitere optionale Tabellen zur Unterstützung der Lösung (nur falls erforderlich).\n"
            + PromptBuilder.get_table_structure_details()
        )

        additional_guidelines = (
            "## Zusätzliche Hinweise:\n"
            "- Verwenden Sie optionale Felder nur, wenn sie die Aufgabe oder Lösung klarer und verständlicher machen.\n"
            "- Tabellen sollten nur in der Lösung genutzt werden, um technische Abläufe wie Zustandsübergänge oder Beispielabläufe darzustellen (Außer es wird explizit gefordert).\n"
            "- Stellen Sie sicher, dass Tabellen vollständig sind und keine Lücken in der Zustandslogik aufweisen.\n"
            "- Unterlassen Sie es, Lösungselemente bereits in der Aufgabenstellung zu nennen.\n"
            "- Jede Aufgabe muss klar, konsistent und logisch nachvollziehbar sein.\n\n"
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
    def get_table_structure_details():
        return (
            "  - Struktur der Tabellen:\n"
            "    - **title (str)**: Titel der Tabelle.\n"
            "    - **headers (List[str])**: Spaltenüberschriften.\n"
            "    - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
        )

    @staticmethod
    def get_final_reminder(difficulty, difficulty_explanation, num_questions):
        header = "# Wichtige abschließende Hinweise!!!:\n\n"

        question_count_reminder = (
            "## Anzahl der Fragen sicherstellen:\n"
            f"- **Überprüfen Sie, ob genau die vorgegebene Anzahl von Fragen {num_questions} generiert wurde.**\n"
            "- Stellen Sie sicher, dass keine Fragen fehlen!\n\n"
        )

        consistency_reminder = (
            "## Konsistenz prüfen:\n"
            "- Überprüfen Sie jede Aufgabe auf Konsistenz mit der angegebenen Schwierigkeitsstufe.\n"
            f"- Stellen Sie sicher, dass keine Aufgabe die Komplexität der gewählten Schwierigkeitsstufe '**{difficulty}**' überschreitet.\n"
            f"- Schwierigkeitsgrad '**{difficulty}**' Erklärung: {difficulty_explanation}\n\n"
        )

        solution_separation_reminder = (
            "## Lösungselemente und Tabellenplatzierung:\n"
            "- **Keine Elemente der Lösung dürfen in der Aufgabenstellung enthalten sein.**\n"
            "- Tabellen dürfen **ausschließlich in der Lösung** und nicht in der Aufgabenstellung verwendet werden, es sei denn, dies ist für das Verständnis der Aufgabe zwingend erforderlich.\n"
            "- Stellen Sie sicher, dass Tabellen korrekt formatiert sind und alle Inhalte den Spaltenüberschriften und Zeilen zugeordnet sind. Doppelte oder unvollständige Tabellen sind zu vermeiden.\n\n"
        )

        table_mapping_reminder = (
            "## Tabellen-Mapping:\n"
            "- Achten Sie besonders darauf, dass Tabellen nur an den vorgesehenen Stellen erscheinen.\n"
            "- Verhindern Sie, dass Lösungstabellen aufgrund von Mapping-Fehlern in der Aufgabenstellung auftauchen.\n"
            "- Jede Tabelle muss ausschließlich dort platziert werden, wo sie sinnvoll und inhaltlich korrekt ist.\n\n"
        )

        quality_reminder = (
            "## Aufgabenvalidierung und Qualitätssicherung:\n"
            "- **Prüfen Sie jede Aufgabe gründlich**, bevor Sie sie als abgeschlossen betrachten. Nutzen Sie gedankliche Tests, Simulationen und Grenzfallanalysen.\n\n"

            "- **Zustandsübergangstabellen:**\n"
            "  ⦁ Müssen vollständig, korrekt und ohne Lücken sein.\n"
            "  ⦁ Alle möglichen Zustände und Übergänge müssen abgedeckt sein, einschließlich Übergänge an Bandenden (Leerzeichen `■`).\n"
            "  ⦁ Iterative Prozesse, falls vorhanden müssen präzise dargestellt und validiert sein.\n\n"

            "- **Beispielablauftabellen:**\n"
            "  ⦁ Dokumentieren Sie jeden Schritt der Turingmaschine, einschließlich aller Bandinhalte, Kopfpositionen und Zustände.\n"
            "  ⦁ Bandinhalte müssen vollständig und korrekt sein, einschließlich Leerzeichen `■` vor und nach der Eingabe.\n"
            "  ⦁ Überprüfen Sie, dass keine Zwischenschritte fehlen, und simulieren Sie den Ablauf Schritt für Schritt, um Diskrepanzen zu vermeiden.\n\n"

            "- **Beispiel und Ergebnisabgleich:**\n"
            "  ⦁ Stellen Sie sicher, dass ein Beispiel vorhanden ist, welches das korrekte Verhalten der Turingmaschine verdeutlicht.\n"
            "  ⦁ Überprüfen Sie, ob das Beispiel mit der Zustandsübergangstabelle und der Aufgabenstellung übereinstimmt.\n\n"

            "- **Konsistenz und Qualität:**\n"
            "  ⦁ Jede Aufgabe muss logisch konsistent, vollständig und realistisch sein. Achten Sie darauf, dass alle Vorgaben der Turingmaschine korrekt umgesetzt werden.\n"
            "  ⦁ Unvollständige Zustandsübergänge oder unklare Beschreibungen sind nicht akzeptabel.\n\n"

            "- **Grenzfälle prüfen:**\n"
            "  ⦁ Testen Sie die Aufgaben mit leeren Eingaben, ungewöhnlichen Kombinationen und anderen Grenzfällen. Verifizieren Sie, dass alle möglichen Szenarien korrekt behandelt werden.\n\n"
        )

        consequences_reminder = (
            "## Bedeutung der Einhaltung der Vorgaben:\n"
            "- **Unvollständige oder fehlerhafte Aufgaben mindern den Wert der generierten Ergebnisse und können NICHT für Prüfungszwecke verwendet werden.**\n"
            "- **Aufgaben, die nicht den Anforderungen entsprechen, müssen verworfen werden.**\n"
            "- **Eine sorgfältige Validierung und Korrektur ist essenziell, um die Qualität und Konsistenz der generierten Aufgaben sicherzustellen.**\n"
            "- Ihr Ziel ist es, präzise, vollständige und fehlerfreie Aufgaben zu erstellen, die höchsten Ansprüchen genügen. Daher wird von Ihnen erwartet, alle vorgegebenen Anforderungen konsequent umzusetzen.\n\n"
            "**Bitte beachten Sie, dass nur vollständig und korrekt validierte Aufgaben akzeptiert werden können.**"
        )

        return (
                header +
                question_count_reminder +
                consistency_reminder +
                solution_separation_reminder +
                table_mapping_reminder +
                quality_reminder +
                consequences_reminder
        )
