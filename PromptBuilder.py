from Const import *


class PromptBuilder:

    @staticmethod
    def create_prompt(num_questions, difficulty, incorrect_task, files_txt, files_images, files_pdf):

        prompt_parts = [PromptBuilder.get_base_prompt(num_questions, difficulty,
                                                      DIFFICULTY_EXPLANATION_MAP.get(difficulty))]
        if incorrect_task:
            prompt_parts.append(PromptBuilder.get_incorrect_task_prompt())

        if any([files_txt, files_images, files_pdf]):
            prompt_parts.append(PromptBuilder.get_attachments_prompt(files_txt, files_images, files_pdf))

        prompt_parts.append(PromptBuilder.get_general_guidelines(difficulty))
        prompt_parts.append(PromptBuilder.get_process_steps(difficulty))
        prompt_parts.append(PromptBuilder.get_structure_instructions())
        prompt_parts.append(PromptBuilder.get_final_reminder(difficulty))

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
            "keine Zustände oder Übergänge auslässt** und die Lösung präzise unterstützt. Tabellen dürfen keine inkonsistenten oder unvollständigen "
            "Daten enthalten.\n\n"

            "6. **Überprüfung der Zustandsübergangstabelle:**\n"
            "   Validieren Sie, dass alle Übergänge in den Zustandstabellen vollständig und klar beschrieben sind. "
            "Unvollständige Tabellen oder fehlende Zustände sind nicht zulässig und gefährden die Qualität der Aufgabe.\n\n"

            "7. **Beispielablauftabelle ergänzen:**\n"
            "   **Generieren Sie immer eine detaillierte **Beispielablauftabelle**, die jeden Schritt der Maschine darstellt, basierend auf einer Beispiel-Eingabe**. "
            "Die Tabelle muss den Bandzustand, die Kopfposition und den aktuellen Zustand für jeden Schritt zeigen."
            "Die Tabelle muss nachvollziehbar und fehlerfrei sein.\n\n"

            "8. **Validierung der Aufgaben:**\n"
            "   Prüfen Sie jede Aufgabe anhand gedanklicher Tests oder Simulationen. Stellen Sie sicher, dass die Zustandsübergänge korrekt sind "
            "und die Maschine das erwartete Ergebnis liefert. Fehlerhafte Ergebnisse oder Endlosschleifen müssen vor der Ausgabe behoben werden.\n\n"

            "9. **Grenzfälle testen:**\n"
            "   Überprüfen Sie die Maschine mit Grenzfällen wie leeren Eingaben, maximaler Eingabelänge oder ungewöhnlichen Kombinationen, um sicherzustellen, dass "
            "alle möglichen Szenarien abgedeckt sind.\n\n"

            "10. **Simulation und abschließende Prüfung:**\n"
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
                f"  Nutzen Sie die Inhalte aus der {datei_typ.lower()}, um die Aufgaben entsprechend zu gestalten.\n\n"
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
            "- **Zustandsübergangstabellen:** Falls erforderlich, müssen Zustandsübergangstabellen alle möglichen Zustände und Übergänge abdecken, einschließlich Anfangs- und Endzuständen. **Unvollständige Tabellen oder fehlende Zustände sind nicht akzeptabel.**\n"
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
            "# Zusätzlicher Informationen zum Auftrag:\n "
            "Generieren Sie nur Aufgaben mit fehlerhaften Turingmaschinen. Der Zweck dieser Aufgaben "
            "ist es, das Fehlersuch- und Korrekturvermögen von Studierenden gezielt zu überprüfen.\n\n"

            "### Aufgabentyp:\n"
            "- Die Turingmaschine soll absichtlich einen oder mehrere Fehler enthalten, die den gewünschten Output "
            "verhindern oder zu einem falschen Output führen.\n"
            "- Diese Fehler sollen so gestaltet sein, dass Studierende durch sorgfältige Analyse der Zustände und "
            "Übergänge in der Lage sein müssen, die Ursache der Fehlfunktion zu identifizieren und zu korrigieren.\n\n"

            "### Vorgaben für die Fehlerstruktur:\n"
            "- Fehler können in den Zustandsübergängen, Lese- und Schreibaktionen oder in der Bandpositionierung "
            "auftreten.\n"
            "- Die Fehler sollen so eingebaut sein, dass sie plausibel und nicht offensichtlich sind, um eine "
            "Herausforderung für Studierende zu bieten.\n\n"

            "### Beachten Sie:\n"
            "- Geben Sie klare Hinweise oder Erklärungen, wie der Studierende den Fehler identifizieren kann, falls "
            "zusätzliche Informationen erforderlich sind.\n"
            "- Optional können Tabellen verwendet werden, um die fehlerhafte Zustandstabelle zu visualisieren. "
            "Stellen Sie sicher, dass die Inhalte in den Spalten vollständig und korrekt strukturiert sind, ohne "
            "Verschiebungen zwischen den Einträgen.\n\n"

            "Generieren Sie die Aufgaben und Lösungen im beschriebenen Format!!!\n\n"
        )

    @staticmethod
    def get_final_reminder(difficulty):
        header = "# Wichtiger abschließender Hinweis:\n\n"

        consistency_reminder = (
            "## Konsistenz prüfen:\n"
            "- Überprüfen Sie jede Aufgabe auf Konsistenz mit der angegebenen Schwierigkeitsstufe.\n"
            f"- Stellen Sie sicher, dass keine Aufgabe die Komplexität der gewählten Schwierigkeitsstufe '**{difficulty}**' überschreitet.\n\n"
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
            "- **Ergänzen Sie Beispielablauftabellen, um die Funktionalität der Zustandsübergangstabelle zu überprüfen und die Abläufe nachvollziehbar zu machen**.\n"
            "- Jede Aufgabe muss logisch konsistent sein, und alle Schritte der Lösung müssen umsetzbar sein.\n\n"
        )

        quality_warning = (
            "## Qualität sicherstellen:\n"
            "- **Unvollständige oder inkonsistente Aufgaben sind streng zu vermeiden.** Jede Aufgabe muss logisch und vollständig sein.\n"
            "- **Unvollständige Zustandsübergänge oder unklare Beschreibungen** gefährden die Qualität der Aufgabe und sind nicht akzeptabel.\n"
            "- Achten Sie darauf, dass die Aufgabenstellung alle Vorgaben einer Turingmaschine erfüllt und realistisch ist.\n"
            "- Alle möglichen Eingabefälle müssen abgedeckt sein.\n\n"
        )

        consequences_reminder = (
            "## Konsequenzen bei Missachtung:\n"
            "- Jegliche Missachtung dieser Hinweise führt zu fehlerhaften Aufgabenstellungen, die unbrauchbar für Prüfungszwecke sind.\n"
            "- Diese Regeln sind entscheidend für die Qualität und den Nutzen der generierten Aufgaben.\n\n"
        )

        return (
                header +
                consistency_reminder +
                solution_separation_reminder +
                table_mapping_reminder +
                validation_reminder +
                quality_warning +
                consequences_reminder
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
            "- Überprüfen Sie, ob die Lösung der Aufgabenstellung entspricht und alle geforderten Schritte klar und vollständig dokumentiert sind.\n"
            "- Stellen Sie sicher, dass die Lösung nachvollziehbar und frei von Lücken oder Fehlern ist.\n\n"

            "3. **Zustandsübergangstabellen:**\n"
            "- Prüfen Sie, ob die Zustandsübergangstabellen vorhanden ist und alle möglichen Übergänge, Zustände und Eingaben vollständig abdecken.\n"
            "- Achten Sie darauf, dass keine Zustände oder Übergänge fehlen und dass die Tabellen korrekt formatiert und logisch konsistent sind.\n"
            "- Unvollständige oder fehlerhafte Übergangstabellen sind für Prüfungsaufgaben nicht akzeptabel.\n"

            "4. **Beispielablauftabellen:**\n"
            "- Ergänzen Sie, falls sinnvoll, eine oder mehrere **Beispielablauftabellen** am Ende der Lösung, um die Schritte besser nachvollziehbar zu machen und die Lösung zu überprüfen.\n"
            "- Die Tabelle muss den Bandzustand, die Kopfposition und den aktuellen Zustand in jedem Schritt dokumentieren.\n"
            "- Falls Beispielablauftabellen fehlen, erstellen Sie diese basierend auf der Zustandsübergangstabelle und der Beispiel-Eingabe.\n\n"

            "5. **Simulationsprüfung:**\n"
            "- Simulieren Sie jede Aufgabe Schritt für Schritt gedanklich oder systematisch, um die Zustandsübergänge und die Funktionsweise zu überprüfen.\n"
            "- Stellen Sie sicher, dass die Turingmaschine das erwartete Ergebnis liefert und dass keine Endlosschleifen oder fehlerhaften Ergebnisse auftreten.\n\n"

            "6. **Grenzfallabdeckung:**\n"
            "- Überprüfen Sie, ob alle denkbaren Eingaben (inklusive Grenzfällen) zu einem definierten Ergebnis führen.\n"
            "- Stellen Sie sicher, dass die Turingmaschine bei maximal zulässigen Eingaben nicht in Endlosschleifen gerät oder fehlerhafte Ergebnisse liefert.\n\n"

            "7. **Verbesserungen bei Mängeln:**\n"
            "- Falls Fehler, Lücken oder Inkonsistenzen gefunden werden:\n"
            "- Korrigieren Sie die Aufgabenstellung, Lösung oder Zustandsübergangstabellen.\n"
            "- Ergänzen Sie fehlende Informationen oder Übergänge, um Vollständigkeit zu gewährleisten.\n"
            "- Erstellen Sie eine konsistente und korrekte Lösung, die den Prüfungsanforderungen entspricht.\n\n"

            "### Vorgehen bei der Validierung und Verbesserung:\n"

            "1. **Aufgabenstellung prüfen:**\n"
            "- Lesen Sie die Aufgabenstellung sorgfältig und stellen Sie sicher, dass sie alle Anforderungen erfüllt.\n\n"

            "2. **Lösungsprüfung:**\n"
            "- Vergleichen Sie die Lösung mit der Aufgabenstellung, um sicherzustellen, dass sie korrekt, vollständig und nachvollziehbar ist.\n\n"

            "3. **Zustandsübergangstabellen validieren:**\n"
            "- Überprüfen Sie jede Tabelle auf Vollständigkeit, Konsistenz und Richtigkeit.\n"
            "- Ergänzen Sie fehlende Übergänge und korrigieren Sie fehlerhafte Einträge.\n\n"

            "4. **Simulationsprüfung durchführen:**\n"
            "- Prüfen Sie, ob die Zustandsübergänge korrekt implementiert sind und ob die Maschine wie erwartet funktioniert.\n\n"

            "5. **Beispielabläufe validieren und ergänzen:**\n"
            "- Überprüfen Sie, ob für jede Aufgabe eine oder mehrere Beispielablauftabellen vorhanden sind, die den Bandzustand, die Kopfposition und den aktuellen Zustand für jeden Schritt der Verarbeitung darstellen.\n"
            "- **Falls Beispielabläufe fehlen, ergänzen Sie diese, um die Schritte der Maschine nachvollziehbar zu machen**.\n"
            "  Jede Beispielablauftabelle muss die korrekte Funktion der Zustandsübergänge mit einer Beispiel-Eingabe vollständig dokumentieren.\n"
            "- Stellen Sie sicher, dass die Beispielabläufe mit den Zustandsübergangstabellen übereinstimmen und keine Inkonsistenzen enthalten.\n\n"

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
