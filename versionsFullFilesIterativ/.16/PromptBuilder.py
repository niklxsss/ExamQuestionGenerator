from Const import *


class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, incorrect_task, files_txt, files_images, files_pdf):
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty)

        prompt_parts = [PromptBuilder.get_base_prompt(num_questions, difficulty, difficulty_explanation)]
        if incorrect_task:
            prompt_parts.append(PromptBuilder.get_incorrect_task_prompt())

        if any([files_txt, files_images, files_pdf]):
            prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))

        prompt_parts.append(PromptBuilder.get_general_guidelines(difficulty))
        prompt_parts.append(PromptBuilder.get_process_steps(difficulty))
        prompt_parts.append(PromptBuilder.get_structure_instructions())
        prompt_parts.append(PromptBuilder.get_final_reminder_table())
        prompt_parts.append(PromptBuilder.get_final_reminder(difficulty, difficulty_explanation))

        return prompt_parts

    @staticmethod
    def get_base_prompt(num_questions, difficulty, difficulty_explanation):
        return (
            "# Ziel der Aufgabe:\n\n"

            f"Generieren Sie genau **{num_questions}** Prüfungsaufgaben zu Turingmaschinen.\n\n"
            f"### Zielgruppe und Anforderungen:\n"
            f"Diese Aufgaben sollen speziell für Studierende der Informatik erstellt werden, um deren "
            f"Verständnis und Anwendungskompetenz zu überprüfen.\n\n"

            f"### Schwierigkeitsgrad:\n"
            f"Die Aufgaben sind auf dem Schwierigkeitsgrad '**{difficulty}**' zu halten:\n"
            f"{difficulty_explanation}\n\n"

            f"### Qualitätskriterien:\n"
            f"Die Aufgaben müssen realistisch, fehlerfrei und mit einer Standard-Turingmaschine umsetzbar sein. "
            f"Sie sind direkt für Prüfungszwecke vorgesehen und müssen höchsten Ansprüchen an Richtigkeit, "
            f"Vollständigkeit und Konsistenz genügen.\n\n"
        )

    @staticmethod
    def get_process_steps(difficulty):
        return (
            "# Ablauf der Prüfungsfrage-Generierung:\n\n"

            "## Wichtiger Hinweis:\n"
            "- **Halten Sie sich strikt an die unten angegebene Abfolge der Schritte, um sicherzustellen, dass keine Fehler oder Unvollständigkeiten auftreten.**\n"
            "- **Jeder Schritt muss vollständig abgeschlossen sein, bevor mit dem nächsten fortgefahren wird.**\n\n"

            "Der folgende Ablauf gewährleistet, dass die generierten Prüfungsaufgaben korrekt, vollständig und für Prüfungen geeignet sind:\n\n"

            "1. **Aufgabenart bestimmen:**\n"
            "   Wählen Sie die Art der Aufgabe, falls nicht vorgegeben, und stellen Sie sicher, dass die Aufgabenstellung vollständig, präzise und klar ist. "
            "Alle Aufgaben müssen auf realistisch umsetzbaren Operationen einer Turingmaschine basieren.\n\n"

            f"2. **Schwierigkeitsstufe prüfen:**\n"
            f"   Die Aufgaben müssen auf dem Schwierigkeitsgrad **{difficulty}** bleiben. Stellen Sie sicher, dass die Aufgabenstellung den Anforderungen "
            f"dieser Stufe entspricht. Vermeiden Sie plötzliche Sprünge in der Komplexität.\n\n"

            "3. **Kohärenz und Umsetzbarkeit sicherstellen:**\n"
            "   Vergewissern Sie sich, dass die Aufgaben auf der gewählten Schwierigkeitsstufe realistisch, kohärent und umsetzbar sind. "
            "Die Komplexität sollte so gehalten werden, dass die Aufgabe korrekt gelöst werden kann.\n\n"

            "4. **Beispiele hinzufügen:**\n"
            "   Generieren Sie optional ein Beispiel, falls es zur Verdeutlichung der Aufgabenstellung beiträgt. "
            "Stellen Sie sicher, dass das Beispiel korrekt ist und die Anforderungen der Aufgabenstellung erfüllt.\n\n"

            "5. **Lösung entwickeln:**\n"
            "   Formulieren Sie eine klare und vollständige Lösung, die direkt zur Aufgabenstellung passt. "
            "Erklären Sie alle Schritte nachvollziehbar, falls es der Aufgabentyp erfordert und achten Sie darauf, dass die Lösung alle Anforderungen abdeckt.\n\n"

            "6. **Zustandsübergangstabelle erstellen:**\n"
            "   Falls es die Lösung erfordert, erstellen Sie eine Zustandsübergangstabelle. Stellen Sie sicher, dass die Tabelle **vollständig ist, "
            "keine Zustände oder Übergänge auslässt** (einschließlich der Übergänge für das Bandende ⋄) und die Lösung präzise unterstützt. "
            "Tabellen dürfen keine inkonsistenten oder unvollständigen Daten enthalten.\n\n"

            "7. **Überprüfung der Zustandsübergangstabelle:**\n"
            "   Validieren Sie, dass alle Übergänge in den Zustandstabellen vollständig und klar beschrieben sind. "
            "Unvollständige Tabellen oder fehlende Zustände sind nicht zulässig und gefährden die Qualität der Aufgabe.\n\n"

            "8. **Beispielablauftabelle ergänzen:**\n"
            "   **Generieren Sie **IMMER** eine detaillierte **Beispielablauftabelle**, die jeden Schritt der Maschine darstellt, basierend auf einer Beispiel-Eingabe!!!** "
            "Die Tabelle muss den Bandzustand, die Kopfposition und den aktuellen Zustand für jeden Schritt zeigen."
            "**Die Tabelle MUSS für jede Aufgabe korrekt und nachvollziehbar sein, um die Übergänge und Ergebnisse der Maschine klar darzustellen.**\n\n"

            "9. **Validierung der Aufgaben:**\n"
            "   Prüfen Sie jede Aufgabe anhand gedanklicher Tests oder Simulationen. Stellen Sie sicher, dass die Zustandsübergänge korrekt sind "
            "und die Maschine das erwartete Ergebnis liefert. Fehlerhafte Ergebnisse oder Endlosschleifen müssen vor der Ausgabe behoben werden.\n\n"

            "10. **Grenzfälle testen:**\n"
            "   Überprüfen Sie die Maschine mit Grenzfällen wie leeren Eingaben, maximaler Eingabelänge oder ungewöhnlichen Kombinationen, um sicherzustellen, dass "
            "alle möglichen Szenarien abgedeckt sind. Verifizieren Sie, dass alle Übergänge am Bandende vollständig definiert sind und keine Fehler entstehen.\n\n"

            "11. **Simulation und abschließende Prüfung:**\n"
            "   Simulieren Sie jede Aufgabe Schritt für Schritt, bevor sie als korrekt betrachtet wird. "
            "Validieren Sie, dass alle Vorgaben der Aufgabenstellung erfüllt sind und die Lösung den Prüfungsanforderungen entspricht.\n\n"
        )

    @staticmethod
    def get_attachments_prompt(files_txt, files_images, files_pdf):
        attachments = (
            "# Zusätzliche Informationen:\n\n"
            "Als Hilfsmittel für die Erstellung von Aufgaben zu Turingmaschinen wurden folgende Inhalte dem Prompt angehängt:\n\n"
        )
        attachments += PromptBuilder.get_attachment_prompt("Textdatei", files_txt)
        attachments += PromptBuilder.get_attachment_prompt("PDF-Datei", files_pdf)
        attachments += PromptBuilder.get_attachment_prompt("Bilddatei", files_images)
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
    def get_general_guidelines(difficulty):
        return (
            "# Grundlegende Anforderungen:\n\n"

            "## Allgemeine Anforderungen:\n"
            "- **Sprache:** Alle Inhalte sollen auf Deutsch verfasst werden.\n"
            "- **Korrektheit:** Stellen Sie sicher, dass die Aufgaben und Lösungen präzise, korrekt und konsistent sind.\n"
            "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende leicht verständlich sein.\n"
            "- **Lösungsbezug:** Die Lösung muss sich direkt auf die Aufgabenstellung beziehen und die erwarteten Schritte nachvollziehbar aufzeigen.\n\n"

            "## Spezifische Anforderungen an die Aufgaben:\n"
            "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an, wenn es für die Aufgabe relevant ist (z.B. {0, 1, ⋄}).\n"
            "- **Bewegungsrichtung und Endzustand:** Beschreiben Sie klar, wie sich die Turingmaschine über das Band bewegt (z.B. von links nach rechts) und wo sie nach Abschluss stehen bleibt. Diese Informationen sollten in den Zusatzinformationen der Aufgabenstellung enthalten sein.\n"
            "- **Zustandsübergangstabellen:** Zustandsübergangstabellen müssen alle möglichen Zustände und Übergänge abdecken, einschließlich Anfangs- und Endzuständen. **Unvollständige Tabellen oder fehlende Zustände sind nicht akzeptabel.**\n"
            "- **Beispielablauftabelle:** Jede Aufgabe **MUSS** eine **Beispielablauftabelle** enthalten, die den Ablauf der Turingmaschine Schritt für Schritt anhand des Beispiels zeigt.\n\n"

            "## Einschränkungen und Komplexität:\n"
            "- **Turingmaschinen-Kompatibilität:** Aufgaben müssen realistisch mit einer Standard-Turingmaschine lösbar sein und dürfen keine zusätzlichen Speicher- oder Zählmechanismen voraussetzen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen.\n"
            f"- **Komplexitätsniveau:** Halten Sie die Komplexität der Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
            "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"

            "## Qualitätssicherung:\n"
            "- **Testfall-Validierung:** Überprüfen Sie jede Aufgabe mit einem Standard-Testfall, um Konsistenz und Korrektheit der Lösung sicherzustellen.\n"
            "- **Fehlerfreiheit:** Aufgaben mit Lücken oder Fehlern sind nicht akzeptabel. Jede Aufgabe muss vollständig, logisch konsistent und schlüssig sein. Lösungen müssen Schritt für Schritt nachvollziehbar sein.\n\n"
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
            "  2. **optional_example** (optional): Ein Beispiel zur Verdeutlichung der Aufgabenstellung.\n"
            "  3. **solution_content** (erforderlich): Die Hauptlösung und optionale Details zur Lösung.\n\n"
        )

        question_content_details = (
            "### Details zu `question_content`:\n"
            "- **question (str)**: Die Hauptfrage. Dieses Feld ist immer erforderlich.\n"
            "- **optional_question_additional_infos (List[str], optional)**: Zusätzliche Informationen, die das Verständnis erleichtern.\n"
            "- **optional_question_tables (List[TableContent], optional)**: Tabellen zur Darstellung komplexer Daten. **Diese sollten nur eingesetzt werden, wenn die "
            "Darstellung komplexer Daten in der Fragestellng sinnvoll ist.**\n"
            "  - Struktur der Tabellen:\n"
            "    - **title (str)**: Titel der Tabelle.\n"
            "    - **headers (List[str])**: Spaltenüberschriften.\n"
            "    - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
        )

        example_details = (
            "### Details zu `optional_example`:\n"
            "- Verwenden Sie dieses Feld, um ein Beispiel bereitzustellen, das das erwartete Verhalten der Lösung verdeutlicht.\n"
            "- Beispiele müssen korrekt, vollständig und direkt relevant für die Aufgabenstellung sein.\n\n"
        )

        solution_content_details = (
            "### Details zu `solution_content`:\n"
            "- **solution (str)**: Die Hauptlösung. Dieses Feld ist immer erforderlich.\n"
            "- **optional_solution_additional_infos (List[str], optional)**: Zusätzliche Hinweise, die das Verständnis der Lösung verbessern.\n"
            "- **optional_solution_step_by_step (List[str], optional)**: Schritt-für-Schritt-Anleitung der Lösung. Verwenden Sie keine Nummerierung! Die Nummerierung erfolgt automatisch.\n"
            "- **optional_solution_tables (List[TableContent], optional)**: Tabellen zur Unterstützung der Lösung (z. B. Zustandsübergänge und Beispielablauftabellen ).\n"
            "  - Struktur der Tabellen:\n"
            "    - **title (str)**: Titel der Tabelle.\n"
            "    - **headers (List[str])**: Spaltenüberschriften.\n"
            "    - **rows (List[List[str]])**: Datenzeilen, die zu den Spaltenüberschriften passen.\n\n"
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
    def get_incorrect_task_prompt():
        return (
            "# Zusätzliche Informationen zum Auftrag:\n\n"

            "Generieren Sie nur Aufgaben mit absichtlich fehlerhaften Turingmaschinen. Ziel dieser Aufgaben ist es, das "
            "Fehlersuch- und Korrekturvermögen der Studierenden gezielt zu überprüfen.\n\n"

            "## Anforderungen an die Fehlerstruktur:\n"
            "- Die Turingmaschine soll mindestens einen Fehler enthalten, der den gewünschten Output verhindert oder zu einem falschen Ergebnis führt.\n"
            "- Die Fehler müssen so eingebaut sein, dass sie logisch nachvollziehbar sind, aber eine sorgfältige Analyse erfordern, um identifiziert und behoben zu werden.\n"
            "- Fehler können auftreten in:\n"
            "   ⦁ **Zustandsübergängen** (z. B. fehlerhafte Übergangsregeln),\n"
            "   ⦁ **Lese- oder Schreibaktionen** (z. B. falsches Band-Symbol),\n"
            "   ⦁ **Bandbewegungen** (z. B. falsche Kopfbewegung).\n\n"

            "## Hinweise für die Gestaltung:\n"
            "- Fügen Sie Hinweise oder zusätzliche Informationen hinzu, um den Studierenden bei der Fehlersuche zu helfen, falls erforderlich.\n"
            "- Verwenden Sie Tabellen, um die fehlerhafte Zustandstabelle klar und präzise zu visualisieren. Achten Sie darauf, dass alle Spalten und Zeilen korrekt formatiert und vollständig sind.\n"
            "- Fehler dürfen nicht trivial oder zu leicht zu erkennen sein, um eine angemessene Herausforderung zu gewährleisten.\n\n"

            "## Ergebnisformat:\n"
            "Stellen Sie sicher, dass die Aufgaben und Lösungen im vorgeschriebenen Format generiert werden. Jede Aufgabe muss:\n"
            "- **Klar formuliert** sein, um Missverständnisse zu vermeiden.\n"
            "- **Eine vollständige Lösung** enthalten, die den Fehler aufzeigt und korrigiert (inkl.  Korrigierte Zustandsübergangstabelle und korrekter Beispielablauftabelle).\n\n"

            "Beachten Sie, dass diese Aufgaben speziell darauf abzielen, die Analyse- und Problemlösungsfähigkeiten der Studierenden zu überprüfen.\n\n"
        )

    @staticmethod
    def get_final_reminder(difficulty, difficulty_explanation):
        header = "# Wichtiger abschließender Hinweis:\n\n"

        question_count_reminder = (
            "## Anzahl der Fragen sicherstellen:\n"
            "- **Überprüfen Sie, ob genau die vorgegebene Anzahl von Fragen ({num_questions}) generiert wurde.**\n"
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
            "- Tabellen dürfen **ausschließlich in der Lösung** und nicht in der Aufgabenstellung verwendet werden, "
            "es sei denn, dies ist für das Verständnis der Aufgabe zwingend erforderlich.\n"
            "- Stellen Sie sicher, dass Tabellen korrekt formatiert sind und alle Inhalte den Spaltenüberschriften "
            "und Zeilen zugeordnet sind. Doppelte oder unvollständige Tabellen sind zu vermeiden.\n\n"
        )

        table_mapping_reminder = (
            "## Tabellen-Mapping:\n"
            "- Achten Sie besonders darauf, dass Tabellen nur an den vorgesehenen Stellen erscheinen.\n"
            "- Verhindern Sie, dass Lösungstabellen aufgrund von Mapping-Fehlern in der Aufgabenstellung auftauchen.\n"
            "- Jede Tabelle muss ausschließlich dort platziert werden, wo sie sinnvoll und inhaltlich korrekt ist.\n\n"
        )

        validation_reminder = (
            "## Aufgabenvalidierung:\n"
            "- Validieren Sie jede Aufgabe mit gedanklichen Tests oder Standard-Testfällen, bevor Sie die nächste Aufgabe generieren.\n"
            "- **Stellen Sie sicher, dass die Übergangstabellen vollständig und korrekt sind und keine Lücken enthalten**.\n"
            "- **Ergänzen Sie Beispielablauftabellen, um die Funktionalität der Zustandsübergangstabelle zu überprüfen "
            "und die Abläufe nachvollziehbar zu machen**. Diese Tabelle muss den Bandzustand, die Kopfposition und den "
            "aktuellen Zustand für jeden Schritt der Verarbeitung dokumentieren.\n"
            "- Jede Aufgabe muss logisch konsistent sein, und alle Schritte der Lösung müssen umsetzbar sein.\n"
            "- Überprüfen Sie, ob die Maschine korrekt auf Grenzfälle wie leere Eingaben oder unerwartete Zeichen reagiert.\n\n"
        )

        quality_warning = (
            "## Qualität sicherstellen:\n"
            "- **Unvollständige oder inkonsistente Aufgaben sind streng zu vermeiden.** Jede Aufgabe muss logisch und vollständig sein.\n"
            "- **Unvollständige Zustandsübergänge oder unklare Beschreibungen** gefährden die Qualität der Aufgabe und sind nicht akzeptabel.\n"
            "- Achten Sie darauf, dass die Aufgabenstellung alle Vorgaben einer Turingmaschine erfüllt und realistisch ist.\n"
            "- Alle möglichen Eingabefälle müssen abgedeckt sein, einschließlich Grenzfällen wie leere Eingaben oder Eingaben mit zusätzlichen Zeichen.\n\n"
        )

        consequences_reminder = (
            "## Konsequenzen bei Missachtung:\n"
            "- Jegliche Missachtung dieser Hinweise führt zu fehlerhaften Aufgabenstellungen, die unbrauchbar für Prüfungszwecke sind.\n"
            "- Diese Regeln sind entscheidend für die Qualität und den Nutzen der generierten Aufgaben.\n\n"
        )

        return (
                header +
                question_count_reminder +
                consistency_reminder +
                solution_separation_reminder +
                table_mapping_reminder +
                validation_reminder +
                quality_warning +
                consequences_reminder
        )

    @staticmethod
    def get_final_reminder_table():
        header = "# Dringender letzter Hinweis zu Tabellen:\n\n"

        table_addition_reminder = (
            "## Zustandsübergangstabellen und Beispielablauftabellen hinzufügen:\n"
            "- **Stellen Sie sicher, dass jede generierte Aufgabe eine vollständige und korrekte Zustandsübergangstabelle enthält.**\n"
            "- **Ergänzen Sie IMMER eine Beispielablauftabelle, die den Bandzustand, die Kopfposition und den aktuellen Zustand für jeden Schritt dokumentiert.**\n"
            "- **Fügen Sie diese Tabellen unbedingt hinzu!!!**\n"
            "- **Überprüfen Sie, dass beide Tabellen vollständig, korrekt und logisch konsistent sind.**\n"
            "- Falls diese Tabellen fehlen oder unvollständig sind, ist die Aufgabe automatisch fehlerhaft und kann NICHT für Prüfungszwecke verwendet werden!!!\n\n"
        )

        return (
                header +
                table_addition_reminder
        )

    @staticmethod
    def create_validation_prompt():
        prompt_parts = [
            PromptBuilder.get_validation_base_prompt(),
            PromptBuilder.get_requirements_validation_process_prompt(),
            PromptBuilder.get_validation_process_prompt(),
            PromptBuilder.get_final_test_prompt(),
            # PromptBuilder.get_structure_instructions()
        ]
        return prompt_parts

    @staticmethod
    def get_validation_base_prompt():
        return (
            "# Aufgabenbeschreibung und Zielsetzung:\n\n"

            "Sie sind ein hochpräziser KI-Validierungsassistent mit Schwerpunkt Informatik. Ihr Ziel ist es, die Qualität, Genauigkeit "
            "und Umsetzbarkeit von Prüfungsaufgaben zu Turingmaschinen sicherzustellen. Jede Aufgabe muss vollständig korrekt, logisch "
            "konsistent und in ihrer Gesamtheit fehlerfrei sein. **Es wird erwartet, dass jede Aufgabe nach Ihrer Validierung ohne Ausnahme den höchsten "
            "Ansprüchen an Prüfungsaufgaben entspricht.**\n\n"

            "**Falls Fehler oder fehlende Inhalte identifiziert werden:**\n"
            "- **Korrigieren Sie diese vollständig.**\n"
            "- **Stellen Sie sicher, dass die korrigierten Aufgaben anstelle der ursprünglichen Aufgaben zurückgegeben werden.**\n"
            "- **Überprüfen Sie, dass alle Teile der Aufgabe, einschließlich Beispiele und Tabellen, perfekt aufeinander abgestimmt sind.**\n\n"

            "**Verhindern Sie:**\n"
            "- Jegliche Rückgabe der ursprünglichen, unkorrigierten Aufgaben.\n"
            "- Fehlerhafte oder unvollständige Anpassungen, die neue Fehler einführen könnten.\n"
            "- Dass aufgrund von Mapping- oder Verarbeitungsfehlern die ursprünglichen, unkorrigierten Aufgaben zurückgesendet werden.\n\n"
        )

    @staticmethod
    def get_requirements_validation_process_prompt():
        return (
            "# Anforderungen an den Validierungsprozess:\n\n"

            "## Konsistenz und Vollständigkeit der gesamten Aufgabe:\n"
            "- **Stellen Sie sicher, dass alle Teile der Aufgabe logisch konsistent sind und sich gegenseitig ergänzen.**\n"
            "- Überprüfen Sie, dass die Aufgabenstellung, Lösung, Zustandsübergangstabellen, und Beispielablauftabellen inhaltlich "
            "perfekt zusammenpassen.\n"
            "- **Validieren Sie, dass das Beispiel (erwartete Ausgabe) mit dem Endzustand der Beispielablauftabelle übereinstimmt.**\n\n"

            "## Korrektheit der Aufgabenstellung:\n"
            "- Stellen Sie sicher, dass die Aufgabenstellung präzise, klar und vollständig ist.\n"
            "- Vermeiden Sie logische Widersprüche, mehrdeutige Formulierungen oder unklare Anforderungen.\n\n"

            "## Korrektheit und Vollständigkeit der Lösung:\n"
            "- Überprüfen Sie, ob die Lösung die Aufgabenstellung korrekt erfüllt.\n"
            "- Validieren Sie, dass alle Lösungsschritte detailliert, nachvollziehbar und frei von Fehlern sind.\n"
            "- Sicherstellen, dass Grenzfälle und mögliche Abweichungen abgedeckt sind.\n\n"

            "## Zustandsübergangstabellen:\n"
            "- Prüfen Sie, ob die Zustandsübergangstabellen komplett vollständig, konsistent und korrekt sind.\n"
            "- Ergänzen Sie fehlende Zustände oder Übergänge und korrigieren Sie inkonsistente Einträge.\n\n"

            "## Beispielablauftabellen und Beispielausgaben:\n"
            "- **Überprüfen Sie, ob jede Aufgabe eine Beispielablauftabelle enthält.**\n"
            "- **Falls eine Beispielablauftabelle fehlt, erstellen Sie diese vollständig neu.** Jede Tabelle muss alle Schritte der Verarbeitung dokumentieren, einschließlich:\n"
            "  - Bandzustand, Kopfposition und aktueller Zustand für jeden Schritt.\n"
            "- **Validieren Sie, dass die Beispielausgabe (Eingabe und erwartete Ausgabe) mit dem letzten Zustand und Bandinhalt der "
            "Beispielablauftabelle übereinstimmt.**\n"
            "- Falls Diskrepanzen zwischen der erwarteten Ausgabe und der Beispielablauftabelle auftreten, korrigieren Sie die Aufgabe und Tabelle vollständig.\n"
            "- Jede Tabelle muss detailliert dokumentiert sein, mit vollständigen Schritten für jeden Zustand, Kopfposition und Bandinhalt.\n\n"

            "## Simulationsprüfung:\n"
            "- Führen Sie eine gedankliche Simulation durch, um sicherzustellen, dass die Aufgabe und alle zugehörigen Tabellen "
            "und Beispiele korrekt umgesetzt wurden.\n"
            "- **Verifizieren Sie das Endergebnis durch eine vollständige Nachverfolgung aller Übergänge und Abläufe.**\n"
            "- Falls Endlosschleifen, fehlerhafte Ergebnisse oder unklare Zustandsübergänge auftreten, beheben Sie diese vollständig.\n\n"

            "## Grenzfallabdeckung:\n"
            "- **Testen Sie die Aufgabe auf Grenzfälle wie leere Eingaben, unübliche Zeichen oder andere Szenarien, die das Verhalten der Turingmaschine prüfen.**\n"
            "- Stellen Sie sicher, dass die Maschine für jeden Eingabefall ein korrekt definiertes Ergebnis liefert.\n\n"

            "## Verbesserungen bei Mängeln:\n"
            "- **Jede identifizierte Schwachstelle, jeder Fehler oder jede Lücke muss vollständig behoben werden.**\n"
            "- Ergänzen oder überarbeiten Sie Aufgabenstellung, Lösung, Zustandsübergangstabellen und Beispielabläufe, um die Anforderungen vollständig zu erfüllen.\n\n"
        )

    @staticmethod
    def get_validation_process_prompt():
        return (
            "# Vorgehen bei der Validierung und Verbesserung:\n\n"

            "## Allgemeiner Hinweis:\n"
            "- **Bearbeiten und prüfen Sie jede Aufgabe vollständig und nacheinander, bevor Sie zur nächsten übergehen.**\n"
            "- Stellen Sie sicher, dass keine Aufgabe übersprungen oder unvollständig bearbeitet wird.\n\n"

            "1. **Aufgabenstellung prüfen:**\n"
            "- Überprüfen und korrigieren Sie die Aufgabenstellung, um sicherzustellen, dass sie vollständig ist und alle Anforderungen erfüllt.\n\n"

            "2. **Lösungsprüfung:**\n"
            "- Korrigieren Sie die Lösung, wenn sie nicht vollständig, korrekt oder nachvollziehbar ist.\n\n"

            "3. **Zustandsübergangstabellen validieren und korrigieren:**\n"
            "- Überprüfen Sie jede Zustandsübergangstabelle auf Vollständigkeit, Konsistenz und Korrektheit.\n"
            "- Ergänzen Sie fehlende Zustände oder Übergänge, und korrigieren Sie fehlerhafte Einträge vollständig.\n"
            "- **Falls keine Zustandsübergangstabelle vorhanden ist, erstellen Sie eine neue, die den Anforderungen entspricht.**\n\n"

            "4. **Beispielabläufe validieren und ergänzen:**\n"
            "- **Überprüfen Sie, ob die Beispielausgabe mit dem Endzustand und Bandinhalt der Beispielablauftabelle übereinstimmt.**\n"
            "- **Falls eine Beispielablauftabelle fehlt, erstellen Sie eine vollständig neue Tabelle, die jeden Schritt dokumentiert:**\n"
            "  - Bandzustand, Kopfposition und aktueller Zustand für jeden Schritt müssen angegeben sein.\n"
            "- Überarbeiten Sie fehlerhafte oder inkonsistente Beispielabläufe, bis sie vollständig korrekt und nachvollziehbar sind.\n"
            "- **Stellen Sie sicher, dass die Beispielablauftabelle konsistent mit der Zustandsübergangstabelle ist und keine Diskrepanzen enthält.**\n\n"

            "5. **Simulationsprüfung durchführen:**\n"
            "- Führen Sie eine Simulation durch, um die Zustandsübergänge und die gesamte Funktionsweise zu überprüfen.\n"
            "- **Verifizieren Sie jeden Schritt und alle Übergänge, um Fehler oder Inkonsistenzen zu beheben.**\n\n"

            "6. **Grenzfälle validieren:**\n"
            "- Stellen Sie sicher, dass die Aufgabe alle Grenzfälle korrekt behandelt und keine undefinierten Zustände auftreten.\n\n"

            "7. **Mapping-Fehler verhindern:**\n"
            "- Verhindern Sie, dass unveränderte Aufgaben oder Teile davon aufgrund technischer Fehler zurückgegeben werden.\n"
            "- Stellen Sie sicher, dass alle zurückgegebenen Aufgaben vollständig überarbeitet und korrekt sind.\n\n"
        )

    @staticmethod
    def get_final_test_prompt():
        return (
            "# Abschlussprüfung:\n\n"

            "**Vor der Rückgabe:**\n"
            "- **Überprüfen Sie die gesamte Aufgabe, einschließlich aller Tabellen und Beispiele, auf vollständige Korrektheit und Konsistenz.**\n"
            "- Überprüfen Sie, ob die Aufgaben durch die Turingmaschine korrekt umsetzbar sind, inklusive aller Grenzfälle.\n"
            "- **Überprüfen Sie, ob jede Aufgabe eine Zustandsübergangstabellen und eine Beispielablauftabelle enthält.Falls keine vorhanden ist, ergänzen Sie diese vor der Rückgabe und testen Sie diese nochmals.**\n"
            "- **Vergleichen Sie die erwartete Beispielausgabe mit dem Endzustand der Beispielablauftabelle, um "
            "- **Ersetzen Sie die ursprünglichen Aufgaben vollständig durch die korrigierten und verbesserten Versionen.**\n"
            "- Geben Sie ausschließlich die überarbeiteten Aufgaben zurück. Eine Rückgabe unveränderter Aufgaben ist nicht zulässig.\n\n"

            "**Wichtige Hinweise:**\n"
            "- Jede Aufgabe MUSS ZWINGEND vollständig fehlerfrei, in sich schlüssig, klar formuliert und logisch konsistent sein.\n"
            "-**Eine Rückgabe, die nicht den Vorgaben entspricht, ist nicht akzeptabel**\n\n"
        )