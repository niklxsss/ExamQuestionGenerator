class ValidationPromptBuilder:

    @staticmethod
    def get_validation_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen validiert. Dein Ziel ist es, "
            "jede Aufgabe vollständig, korrekt und konsistent zu machen. Achte darauf, dass alle Bestandteile der Aufgabe "
            "(Aufgabenstellung, Zusatzinformationen, Beispiel, Zustandsübergangstabelle und Beispielablauftabelle) logisch "
            "miteinander übereinstimmen und fehlerfrei sind.\n\n"
            "Während der Validierung ist es besonders wichtig sicherzustellen, dass:\n"
            "- Die Aufgabe klar und präzise formuliert ist und keine inhaltlichen oder logischen Fehler enthält.\n"
            "- Die Tabellen (Zustandsübergangstabelle und Beispielablauftabelle) exakt und konsistent mit der Aufgabenstellung und dem Beispiel sind.\n"
            "- Das Beispiel korrekt und repräsentativ für die Aufgabe ist.\n"
            "- Alle Fehler oder Unstimmigkeiten identifiziert und behoben werden."
        )

    @staticmethod
    def get_validation_request_prompt(task):
        return (
            f"## Zu überprüfende Aufgabe:\n\n"
            f"{task}\n\n\n\n"
            
            "## Validierung der gesamten Aufgabe:\n"
            "- **Konsistenz:** Überprüfen Sie, ob alle Elemente der Aufgabe (Aufgabenstellung, Zusatzinformationen, Beispiel, Zustandsübergangstabelle, Beispielablauftabelle) logisch zusammenpassen und konsistent sind.\n"
            "- **Vollständigkeit:** Stellen Sie sicher, dass keine Inhalte oder notwendige Informationen fehlen.\n\n"

            "## Validierung des Beispiels ('example'):\n"
            "- **Korrektheit:** Prüfen Sie, ob das Beispiel das Ziel der Aufgabe klar und korrekt veranschaulicht.\n"
            "- **Konsistenz mit der Aufgabe:** Überprüfen Sie, ob das Beispiel exakt mit der Aufgabenstellung übereinstimmt.\n"
            "- **Logische Abläufe:** Validieren Sie, ob die im Beispiel dargestellten Schritte logisch und fehlerfrei sind.\n\n"

            "## Validierung der Zustandsübergangstabelle ('solution_state_transition_table'):\n"
            "- **Korrekte Abbildung der Übergangsregeln:** Stellen Sie sicher, dass alle Zustände und Übergänge der Tabelle exakt mit der Aufgabenstellung und den Zusatzinformationen übereinstimmen.\n"
            "- **Spaltenstruktur:** Prüfen Sie, ob die Spalten (Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand) korrekt ausgefüllt und vollständig sind.\n"
            "- **Eindeutigkeit:** Validieren Sie, dass alle Zustandsübergänge präzise und eindeutig definiert sind.\n"
            "- **Fehlerkorrektur:** Falls Fehler oder Unstimmigkeiten vorhanden sind, korrigieren Sie diese und dokumentieren Sie die Änderungen.\n\n"

            "## Validierung der Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- **Übereinstimmung mit der Zustandsübergangstabelle:** Validieren Sie, dass jeder Schritt der Beispielablauftabelle den Übergangsregeln der Zustandsübergangstabelle entspricht.\n"
            "- **Kopfposition:** Überprüfen Sie, ob die Kopfposition korrekt nummeriert ist (beginnend bei 1) und die Bewegungen des Lesekopfes lückenlos dokumentiert sind.\n"
            "- **Bandinhalt:** Validieren Sie, ob der Bandinhalt nach jedem Schritt korrekt aktualisiert wurde und die aktive Kopfposition richtig markiert ist (z. B. `■11[0]1■`).\n"
            "- **Fehlerkorrektur:** Prüfen Sie nach jedem Schritt, ob der Ablauf korrekt ist, und korrigieren Sie Unstimmigkeiten.\n\n"

            "## Abschließende Überprüfung:\n"
            "- **Endzustand:** Validieren Sie, ob die Aufgabe und die Tabellen korrekt den Endzustand der Turingmaschine erreichen.\n"
            "- **Konsistenz der Ergebnisse:** Stellen Sie sicher, dass das Beispiel und die Tabellen gemeinsam das Ziel der Aufgabe erreichen und korrekt das erwartete Ergebnis produzieren.\n\n"

            "Falls Unstimmigkeiten oder Fehler gefunden werden, nehmen Sie die notwendigen Korrekturen vor und validieren Sie die Aufgabe erneut."
        )

    @staticmethod
    def create_prefix_validation_prompt():
        return [
            ValidationPromptBuilder.get_base_description(),
            ValidationPromptBuilder.get_correction_steps(),
        ]

    @staticmethod
    def create_suffix_validation_prompt():
        return [
            ValidationPromptBuilder.get_final_check(),
        ]

    @staticmethod
    def get_base_description():
        return (
            "# Ziel der Validierung:\n\n"

            "Ihre Aufgabe ist es, die Prüfungsaufgabe zu Turingmaschinen vollständig zu korrigieren und zu verbessern. "
            "Die Aufgabe muss vollständig korrekt, logisch konsistent und für Prüfungszwecke geeignet sein.\n\n"

            "**Hauptziele:**\n"
            "- Identifizieren Sie alle Fehler in der Aufgabenstellung, den Zusatzinformationen, dem Beispiel, der Zustandsübergangstabelle und der Beispielablauftabelle.\n"
            "- Beheben Sie alle Fehler, stellen Sie sicher, dass die korrigierte Aufgabe höchsten Ansprüchen genügt.\n"
            "- Garantieren Sie, dass die Zustandsübergangstabelle und die Beispielablauftabelle 100% korrekt zum Beispiel und der Aufgabenstellung passen, einschließlich der korrekten Behandlung von Leerzeichen und Grenzfällen.\n"
            "- Überprüfen Sie, dass keine redundanten oder doppelt vorkommenden Informationen enthalten sind.\n\n"

            "**Verhindern Sie:**\n"
            "- Jegliche Rückgabe der ursprünglichen, unkorrigierten Aufgabe.\n"
            "- Fehlerhafte oder unvollständige Anpassungen, die neue Fehler einführen könnten.\n"
            "- Falsche oder nicht überprüfte Tabellen oder Beispiele.\n"
            "- Eine Rückgabe, in der Aufzählungen (Listen, wie in den Zusatzinformationen oder im Lösungsweg) nummeriert oder mit Aufzählungszeichen versehen sind.\n\n"
        )

    @staticmethod
    def get_correction_steps():
        return (
            "# Schritte zur Korrektur:\n\n"

            "## Aufgabenstellung und Zusatzinformationen validieren und korrigieren:\n"
            "- **Aufgabenstellung überprüfen und korrigieren:**\n"
            "  ⦁ Stellen Sie sicher, dass die Aufgabenstellung das Problem eindeutig, präzise und vollständig beschreibt.\n"
            "  ⦁ Entfernen Sie technische Details, die in die Zusatzinformationen gehören (z. B. Alphabet, Kopfpositionen, Leerzeichen).\n"
            "  ⦁ Ergänzen Sie fehlende Details, wenn diese für die Lösung notwendig sind.\n"
            "  ⦁ Überprüfen Sie, ob die Aufgabenstellung logisch und umsetzbar ist, und korrigieren Sie ungenaue Formulierungen.\n\n"

            "- **Zusatzinformationen validieren und korrigieren:**\n"
            "  ⦁ Stellen Sie sicher, dass alle technischen Details in die Zusatzinformationen ausgelagert wurden (z. B. Alphabet, Bandbegrenzung, Start- und Endposition).\n"
            "  ⦁ Entfernen Sie doppelt vorkommende oder redundante Informationen.\n"
            "  ⦁ Korrigieren Sie die Formatierung der Zusatzinformationen: Listen dürfen keine Nummerierung, Aufzählungszeichen oder Striche enthalten.\n\n"

            "## Beispiel validieren und korrigieren:\n"
            "- **Beispiel anpassen:**\n"
            "  ⦁ Stellen Sie sicher, dass das Beispiel zu 100% mit der Aufgabenstellung übereinstimmt.\n"
            "  ⦁ Ergänzen Sie das Beispiel, falls es unvollständig ist, oder korrigieren Sie Fehler in Eingabe und erwarteter Ausgabe.\n"
            "  ⦁ Überprüfen Sie, ob das Beispiel das Verhalten der Turingmaschine korrekt widerspiegelt, einschließlich der Behandlung von Leerzeichen und Bandgrenzen.\n\n"

            "## Konsistenzprüfung zwischen Aufgabe und Lösung:\n"
            "- **Überprüfung der Lösung:**\n"
            "  ⦁ Vergewissern Sie sich, dass die Lösung exakt die Zielsetzung der Aufgabenstellung umsetzt.\n"
            "  ⦁ Diskrepanzen zwischen Aufgabenstellung und Lösung sind vollständig zu korrigieren.\n"
            "  ⦁ Prüfen Sie, ob alle Zusatzinformationen in die Lösung integriert wurden.\n\n"

            "## Tabellen:\n"
            "- **Einfachheit sicherstellen:**\n"
            "  ⦁ Stellen Sie sicher, dass die Zustandsübergangstabelle und die Beispielablauftabelle die Aufgabe auf dem einfachsten möglichen Weg umsetzen.\n"
            "  ⦁ Entfernen Sie unnötige Zustände, Übergänge oder Komplexitäten, die nicht für die korrekte Umsetzung der Aufgabe erforderlich sind.\n"

            "### Zustandsübergangstabellen validieren und korrigieren:\n"
            "- **Tabelle prüfen und korrigieren:**\n"
            "  ⦁ Stellen Sie sicher, dass alle Zustände vollständig dokumentiert sind: Start-, Zwischen- und Endzustände.\n"
            "  ⦁ Überprüfen Sie, ob alle Übergänge korrekt spezifiziert sind (aktueller Zustand, gelesenes Zeichen, neues Zeichen, Bewegung, neuer Zustand).\n"
            "  ⦁ Ergänzen Sie fehlende Zustände, Übergänge oder Sonderfälle (z. B. Behandlung von Leerzeichen oder Bandgrenzen).\n"
            "  ⦁ Überprüfen Sie, falls die Aufgabe iterative Prozesse enthält, diese korrekt umgesetzt sind und korrigieren Sie diese bei Bedarf.\n\n"

            "- **Tabelleninhalt verbessern:**\n"
            "  ⦁ Stellen Sie sicher, dass keine Lücken oder widersprüchlichen Einträge in der Tabelle vorhanden sind.\n"
            "  ⦁ Validieren Sie die Tabelle anhand der Aufgabenstellung und des Beispiels, um sicherzustellen, dass sie exakt passt.\n\n"

            "### Beispielablauftabellen validieren und korrigieren:\n"
            "- **Überprüfung und Ergänzung:**\n"
            "  ⦁ Vergewissern Sie sich, dass die Tabelle jeden Schritt der Turingmaschine dokumentiert (Schritt, aktueller Zustand, Bandzustand, Kopfposition).\n"
            "  ⦁ Korrigieren Sie die Kopfposition, falls sie inkorrekt angegeben ist. DIE KOPFPOSITION BEGINNT IMMER MIT 1!\n"
            "  ⦁ Ergänzen Sie fehlende Zwischenschritte.\n"
            "  ⦁ In der Spalte Bandinhalt muss der gesamte Bandinhalt einschließlich der Leerzeichen vor und nach der Eingabe angegeben werden. Zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] zu kennzeichnen (Beispiel: ■[1]000■).\n"
            "  ⦁ Stellen Sie sicher, dass die Bandenden korrekt behandelt werden und keine Leerzeichen verloren gehen oder fälschlicherweise entfernt werden.\n\n"

            "- **Korrektheit und Konsistenz sicherstellen:**\n"
            "  ⦁ Überprüfen Sie, ob die Beispielablauftabelle vollständig mit der Zustandsübergangstabelle und dem Beispiel übereinstimmt.\n"
            "  ⦁ Simulieren Sie den Ablauf der Turingmaschine Schritt für Schritt und beheben Sie alle Abweichungen.\n"
            "  ⦁ Verifizieren Sie, dass die Bandinhalt-Darstellung in jedem Schritt logisch konsistent ist, einschließlich der Markierung der Kopfposition und der Behandlung von Bandgrenzen.\n\n"

            "## Gesamtkohärenz sicherstellen:\n"
            "- **Aufgabe und Tabellen abstimmen:**\n"
            "  ⦁ Verifizieren Sie, dass die Aufgabenstellung, die Lösung und das Beispiel inhaltlich übereinstimmen.\n"
            "  ⦁ Korrigieren Sie alle Unstimmigkeiten zwischen der Zielsetzung der Aufgabenstellung und der tatsächlichen Lösung.\n"
            "  ⦁ Stellen Sie sicher, dass die Zustandsübergangstabelle und die Beispielablauftabelle die Zielsetzung der Aufgabe präzise umsetzen.\n\n"
        )

    @staticmethod
    def get_final_check():
        return (
            "# Abschlussprüfung:\n\n"

            "**Vor der Rückgabe:**\n"
            "- Stellen Sie sicher, dass die korrigierte Aufgabe vollständig korrekt und logisch konsistent ist.\n"
            "- Überprüfen Sie, ob die Zustandsübergangstabelle und die Beispielablauftabelle 100% korrekt zur Aufgabenstellung und dem Beispiel passen.\n"
            "- Überprüfen Sie, dass alle Listen (z. B. Zusatzinformationen, Lösungsschritte) keine Nummerierung, Striche oder Aufzählungszeichen enthalten, da diese automatisch formatiert werden.\n"
            "- Simulieren Sie die Turingmaschine, um sicherzustellen, dass die korrigierte Tabelle und der Ablauf alle Anforderungen erfüllen, einschließlich der Leerzeichenbehandlung und Grenzfälle.\n"
            "- GEBEN SIE AUSSCHLIESSLICH DIE KORRIGIERTE UND VERBESSERTE AUFGABE ZURÜCK. EINE UNKORRIGIERTE ODER FEHLERHAFTE RÜCKGABE IST NICHT ZULÄSSIG!\n\n"

            "**Wichtige Hinweise:**\n"
            "- Jede Tabelle muss vollständig, fehlerfrei und konsistent sein.\n"
            "- Die korrigierte Aufgabe muss höchsten Ansprüchen genügen und bereit für den Einsatz in Prüfungen sein.\n"
            "- Fehler oder Abweichungen in der Rückgabe führen dazu, dass die Aufgabe als unbrauchbar gilt.\n\n"
        )

    # @staticmethod
    # def create_refinement_validation_prompt():
    #     return (
    #         "Korrigieren Sie die Zustandsübergangstabelle und darauf basierend die Beispielablauftabelle "
    #         "(inkl. aller Spalten u Zeilen) so, dass beide vollständig, logisch konsistent und exakt auf die "
    #         "Anforderungen der Aufgabenstellung abgestimmt sind! Achte besonders auf den Erwarteten Output im Beispiel um die Aufgabe zu korrigeren!"
    #     )

    # @staticmethod
    # def create_refinement_validation_prompt():
    #     return (
    #         "Überarbeiten Sie die gesamte Aufgabe so, dass sie vollständig konsistent und korrekt ist. "
    #         "Passen Sie dazu die Lösung, den Lösungsweg (falls vorhanden), die Zustandsübergangstabelle und die Beispielablauftabelle "
    #         "komplett an die Anforderungen der Aufgabenstellung an. "
    #         "Gehen Sie dabei davon aus, dass die bisherige Lösung komplett falsch ist, und überprüfen Sie alle Elemente gründlich. "
    #         "Stellen Sie sicher, dass die Zustandsübergangstabelle den korrekten Ablauf der Turingmaschine abbildet, "
    #         "und dass die Beispielablauftabelle exakt mit der Zustandsübergangstabelle und den Vorgaben der Aufgabenstellung übereinstimmt. "
    #         "Berücksichtigen Sie besonders den erwarteten Output im Beispiel, und denken Sie jede Komponente unabhängig von bisherigen Inhalten neu durch. "
    #         "Ziel ist eine logisch konsistente, präzise und fehlerfreie Darstellung aller Elemente.\n\n"
    #
    #         "Zusatzinformation:\n"
    #         "Achte bei der Beispielablauftabelle vorallem auf eine korrekte abfolge der Schritte, richtige darstellung der Bandinhalt und auf die korrekte Nummerierung der Kopfposition (Erste Ziffer ist Nummer 1)."
    #         "Ändere nicht das Leerzeichensymbol ■ ab, außer es ist komplett falsch übergeben."
    #
    #
    #     )
    #
    # @staticmethod
    # def create_second_refinement_validation_prompt():
    #     return (
    #         "Überarbeiten die gesamte Aufgabe so, dass sie vollständig konsistent und korrekt ist. "
    #         "Die komplette Lösung ist sehr wahrscheinlich falsch, optimiere diese, damit die Funktion der Aufgabenstellung u des Beispiels fehlerfrei umgesetzt werden"
    #
    #     )

    # @staticmethod
    # def create_task_validation_prompt():
    #     return (
    #         "Überarbeiten Sie die Aufgabenstellung, Zusatzinformationen und das Beispiel vollständig, sodass sie den höchsten Standards entsprechen.\n"
    #         "Die Aufgabenstellung ('question') muss präzise, klar und frei von technischen Details sein, die ausschließlich in den Zusatzinformationen ('optional_question_additional_infos') enthalten sein dürfen.\n"
    #         "Stellen Sie sicher, dass das Beispiel exakt die Anforderungen der Aufgabenstellung widerspiegelt und den korrekten erwarteten Output zeigt. Das Beispiel soll zudem nur unter 'example' angegeben werden und nicht in der Aufgabenstellung.\n"
    #         "Alle Inhalte müssen logisch, vollständig und für die Lösung mit einer Standard-Turingmaschine geeignet sein.\n"
    #         "Das Symbol für Leerzeichen ist ■! Ändere nicht das Leerzeichensymbol ■ ab, außer es entspricht nicht dem Symbol ■!\n"
    #     )

    @staticmethod
    def create_task_validation_prompt():
        return (
            "Überarbeiten Sie die Aufgabenstellung, die Zusatzinformationen und das Beispiel vollständig, sodass sie höchsten Standards entsprechen.\n"
            "Die Aufgabenstellung ('question') muss präzise, klar und vollständig das zu lösende Problem beschreiben. "
            "Technische Details (z. B. Alphabet, Kopfpositionen, Leerzeichen) dürfen NICHT in der Aufgabenstellung erscheinen und müssen ausschließlich in den Zusatzinformationen ('optional_question_additional_infos') enthalten sein.\n\n"

            "Stellen Sie sicher, dass:\n"
            "- Die Aufgabenstellung logisch, eindeutig und vollständig ist.\n"
            "- Technische Details in die Zusatzinformationen ausgelagert und dort korrekt und vollständig angegeben werden (z. B. Alphabet: {0, 1, ■}, Bandbegrenzung, Startposition des Kopfes).\n"
            "- Doppelte oder redundante Informationen entfernt werden.\n"
            "- Die Zusatzinformationen sauber formatiert sind.\n\n"

            "Überarbeiten Sie das Beispiel ('example') so, dass es zu 100% mit der Aufgabenstellung und den Zusatzinformationen übereinstimmt. "
            "Stellen Sie sicher, dass das Beispiel das erwartete Verhalten der Turingmaschine exakt widerspiegelt, einschließlich der korrekten Darstellung der Leerzeichen vor und nach der Eingabe. "
            "Das Beispiel darf nur unter 'example' angegeben werden und nicht in der Aufgabenstellung wiederholt werden.\n\n"

            "Zusätzliche Hinweise:\n"
            "- Das Symbol für Leerzeichen ist **■**. Ändern Sie dieses Symbol NICHT, außer es entspricht nicht dem Standard.\n"
            "- Stellen Sie sicher, dass die gesamte Aufgabe logisch umsetzbar und vollständig auf die Lösung mit einer Standard-Turingmaschine abgestimmt ist.\n"
            "- Entfernen Sie Unklarheiten oder ungenaue Formulierungen und ergänzen Sie notwendige Details, wenn diese fehlen.\n\n"

            "Darstellung von Aufzählungen:\n"
            "- Überprüfen Sie, dass alle Listen (z. B. Zusatzinformationen, Lösungsschritte) keine Nummerierung, Striche oder Aufzählungszeichen enthalten, da diese automatisch formatiert werden.\n"
        )

    # @staticmethod
    # def create_solution_validation_prompt():
    #     return (
    #         "Überarbeiten Sie die Lösung, einschließlich der Zustandsübergangstabelle und der Beispielablauftabelle, vollständig. "
    #         "Die Zustandsübergangstabelle muss den Ablauf der Turingmaschine exakt und fehlerfrei abbilden, basierend auf der überarbeiteten Aufgabenstellung und dem Beispiel. "
    #         "Die Beispielablauftabelle muss die Zustandsübergangstabelle Schritt für Schritt korrekt nachvollziehen und den erwarteten Output aus der Aufgabenstellung widerspiegeln. "
    #         "Stellen Sie sicher, dass die Lösung vollständig, konsistent und frei von logischen oder technischen Fehlern ist. "
    #         "Jede Tabelle muss vollständig dokumentiert sein, alle möglichen Übergänge abdecken und exakt mit den Anforderungen übereinstimmen."
        # )

    # @staticmethod
    # def create_solution_validation_prompt():
    #     return (
    #         "Überarbeiten Sie die Lösung vollständig, einschließlich der Zustandsübergangstabelle und der Beispielablauftabelle, "
    #         "sodass alle Inhalte präzise, konsistent und vollständig mit der Aufgabenstellung und dem Beispiel abgestimmt sind. "
    #         "Gehen Sie immer davon aus, dass die bestehende Lösung komplett fehlerhaft ist, und erstellen Sie die Tabellen von Grund auf verbessert und neu durchdacht werden MUSS.\n\n"
    #
    #         "## Anforderungen an die Zustandsübergangstabelle:\n"
    #         "- Stellen Sie sicher, dass die Zustandsübergangstabelle den Ablauf der Turingmaschine exakt und fehlerfrei abbildet.\n"
    #         "- Dokumentieren Sie alle Zustände vollständig, einschließlich Start-, Zwischen- und Endzustände.\n"
    #         "- Überprüfen und korrigieren Sie alle Übergänge:\n"
    #         "  ⦁ Aktueller Zustand\n"
    #         "  ⦁ Gelesenes Zeichen\n"
    #         "  ⦁ Neues Zeichen\n"
    #         "  ⦁ Bewegung (links, rechts, keine)\n"
    #         "  ⦁ Neuer Zustand\n"
    #         "- Ergänzen Sie fehlende Zustände, Übergänge oder Sonderfälle, einschließlich der korrekten Behandlung von Leerzeichen und Bandgrenzen.\n"
    #         "- Stellen Sie sicher, dass iterative Prozesse oder Loops korrekt umgesetzt sind und logisch nachvollziehbar abgebildet werden.\n"
    #         "- Vermeiden Sie unnötige Zustände oder Komplexitäten, die nicht zur Lösung der Aufgabe beitragen.\n\n"
    #
    #         "## Anforderungen an die Beispielablauftabelle:\n"
    #         "- Dokumentieren Sie jeden Schritt der Turingmaschine vollständig und nachvollziehbar:\n"
    #         "  ⦁ Schritt (nummeriert).\n"
    #         "  ⦁ Aktueller Zustand.\n"
    #         "  ⦁ Bandinhalt:\n"
    #         "     ⦁ Der gesamte Bandinhalt, einschließlich der Leerzeichen vor und nach der Eingabe, muss angegeben werden.\n"
    #         "     ⦁ Markieren Sie die aktuelle Kopfposition im Bandinhalt zusätzlich durch [ ], z. B. ■[1]000■.\n"
    #         "  ⦁ Kopfposition:\n"
    #         "     ⦁ Geben Sie nur die numerische Position des Lese-/Schreibkopfes an, beginnend mit 1 für die erste Position der Eingabe (nicht das Leerzeichen).\n"
    #         "- Ergänzen Sie fehlende Zwischenschritte, insbesondere bei iterativen Prozessen oder Loops.\n"
    #         "- Stellen Sie sicher, dass die Tabelle exakt den Ablauf der Zustandsübergangstabelle widerspiegelt und den erwarteten Output aus der Aufgabenstellung korrekt darstellt.\n"
    #         "- Verifizieren Sie, dass die Bandenden korrekt behandelt werden und keine Leerzeichen verloren gehen oder fälschlicherweise entfernt werden.\n\n"
    #
    #         "## Konsistenz zwischen Aufgabenstellung, Zustandsübergangstabelle und Beispielablauftabelle:\n"
    #         "- Überprüfen Sie, ob die Lösung exakt die Zielsetzung der Aufgabenstellung umsetzt.\n"
    #         "- Diskrepanzen zwischen Aufgabenstellung, Zustandsübergangstabelle und Beispielablauftabelle müssen vollständig korrigiert werden.\n"
    #         "- Validieren Sie den Ablauf der Turingmaschine durch Simulation Schritt für Schritt und korrigieren Sie alle Abweichungen.\n"
    #         "- Stellen Sie sicher, dass die Bandinhalt-Darstellung in jedem Schritt logisch konsistent ist, einschließlich der Markierung der Kopfposition und der Behandlung von Bandgrenzen.\n\n"
    #
    #         "## Anpassung der Zusatzinformationen und des Lösungswegs:\n"
    #         "- Überarbeiten Sie die Zusatzinformationen der Lösung so, dass sie exakt mit der korrigierten Lösung übereinstimmen und keine redundanten oder widersprüchlichen Angaben enthalten.\n"
    #         "- Passen Sie den Lösungsweg an, um eine klare und vollständige Beschreibung der Korrekturen und der korrekten Funktionsweise der Turingmaschine zu gewährleisten.\n\n"
    #
    #         "Das Symbol für Leerzeichen ist **■**. Ändern Sie dieses Symbol NICHT, außer es entspricht nicht dem Standard!"
    #     )

    @staticmethod
    def create_final_refinement_prompt():
        return (
            # "Überarbeiten Sie die Prüfungsaufgabe zur Turingmaschine so, dass sie vollständig, logisch konsistent und exakt auf die Aufgabenstellung und das Beispiel abgestimmt sind. "
            # "Gehen Sie immer davon aus, dass die bestehende Lösung komplett fehlerhaft ist, und erstellen Sie die Tabellen von Grund auf verbessert und neu durchdacht werden MUSS.\n\n"
            # "Stellen Sie sicher, dass die Tabellen den Ablauf der Turingmaschine korrekt abbilden und das erwartete Ergebnis liefern."
            #
            # "Das Symbol für Leerzeichen ist **■**. Ändern Sie dieses Symbol NICHT, außer es entspricht nicht dem Standard!"

            # alle schritte angeben, auch behandlung von Anfang u End leerzeichen etc

            "Überarbeiten Sie die gesamte Prüfungsaufgabe zur Turingmaschine, einschließlich Aufgabenstellung, Beispiel, Lösung, Zustandsübergangstabelle und Beispielablauftabelle, vollständig. "
            "Alle Inhalte müssen logisch konsistent, vollständig und präzise aufeinander abgestimmt sein. Gehen Sie immer davon aus, dass die bestehende Lösung und alle Tabellen komplett fehlerhaft sind. "
            "Erstellen Sie die Tabellen von Grund auf neu und verbessern Sie sie durchdacht.\n\n"
        )

    @staticmethod
    def create_validation_prompt():
        return [
            ValidationPromptBuilder.create_task_example_validation_prompt(),
            ValidationPromptBuilder.create_solution_table_validation_prompt(),
            ValidationPromptBuilder.create_solution_validation_prompt(),
            ValidationPromptBuilder.create_additional_info_validation_prompt()
        ]

    @staticmethod
    def create_task_example_validation_prompt():
        return (
            "## Korrektur der Aufgabenstellung und des Beispiels:\n"
            "**Aufgabe:** Überprüfen und verbessern Sie die Aufgabenstellung ('question') und das Beispiel ('example').\n\n"
            
            "### Anforderungen an die Aufgabenstellung ('question'):\n"
            "- Stellen Sie sicher, dass die Aufgabenstellung das zu lösende Problem präzise, klar und vollständig beschreibt.\n"
            "- Entfernen Sie technische Details oder Hinweise zur Lösung. Diese gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
            "- Vermeiden Sie mehrdeutige Formulierungen und sicherstellen Sie, dass die Aufgabenstellung für Studierende leicht verständlich ist.\n\n"
            
            "### Anforderungen an das Beispiel ('example'):\n"
            "- Stellen Sie sicher, dass das Beispiel die Aufgabenstellung klar veranschaulicht und mit ihr übereinstimmt.\n"
            "- Überprüfen Sie, ob die Eingabe und der erwartete Output korrekt dargestellt sind, einschließlich der Leerzeichen-Symbole `■` (z. B. `■11010■`).\n"
            "- Das Beispiel muss den Ablauf der Turingmaschine korrekt widerspiegeln und konsistent mit der Lösung sein.\n"
        )

    @staticmethod
    def create_solution_table_validation_prompt():
        return (
            "## Korrektur der Lösungstabellen:\n"
            "**Aufgabe:** Überprüfen und verbessern Sie die Zustandsübergangstabelle ('solution_state_transition_table') und die Beispielablauftabelle ('solution_example_flow_table').\n\n"
            
            "### Anforderungen an die Zustandsübergangstabelle ('solution_state_transition_table'):\n"
            "- **Konsistenz:** Stellen Sie sicher, dass die Zustände und Übergänge exakt mit der Aufgabenstellung und dem Beispiel übereinstimmen.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände (einschließlich Start- und Endzustände) und Übergänge müssen vollständig abgedeckt sein, einschließlich Sonderzeichen wie Leerzeichen `■`.\n"
            "- **Logik und Effizienz:** Wählen Sie die logischste und effizienteste Abfolge der Zustände und Übergänge, ohne notwendige Schritte oder Zustände auszulassen.\n\n"
            
            "### Anforderungen an die Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Kopfposition:** Die Kopfposition muss numerisch beginnend mit 1 angegeben werden.\n"
            "- **Bandinhalt:** Zeigen Sie den gesamten Bandinhalt, einschließlich Leerzeichen an und markieren Sie zusätzlich ist die aktive Kopfposition im Bandinhalt durch [ ] (Beispiel: ■[1]000■)!\n\n"
            "- Überprüfen Sie, ob alle Zwischenschritte korrekt dokumentiert sind und keine Lücken bestehen.\n"

        )

    @staticmethod
    def create_solution_validation_prompt():
        return (
            "## Korrektur der restlichen Lösung:\n"
            "**Primäre Aufgabe:** Überarbeiten Sie die Lösung ('solution') sowie optionale Felder ('optional_solution_additional_infos', 'optional_solution_step_by_step').\n\n"
            
            "### Anforderungen an die Lösung ('solution'):\n"
            "- Geben Sie eine präzise und vollständige konzeptionelle Beschreibung des Lösungsansatzes an.\n"
            "- Stellen Sie sicher, dass die Lösung vollständig mit der Aufgabenstellung, den Zusatzinformationen und den Tabellen übereinstimmt.\n\n"
            
            "### Anforderungen an die optionalen Felder:\n"
            "- **Zusätzliche Informationen ('optional_solution_additional_infos')**:\n"
            "  - Ergänzen Sie relevante Hintergrundinformationen, die das Verständnis der Lösung verbessern.\n"
            "- **Lösungsweg ('optional_solution_step_by_step')**:\n"
            "- Beschreiben Sie den Lösungsweg Schritt für Schritt in Textform, ohne Tabellen oder Aufzählungszeichen.\n"
            "- Überprüfen Sie, ob alle Informationen logisch konsistent sind und keine unnötigen Details enthalten.\n"

        )

    @staticmethod
    def create_additional_info_validation_prompt():
        return (
            "## Weiter Informationen:\n"
            "- Überprüfen Sie, dass alle Listen (z. B. Zusatzinformationen, Lösungsschritte) keine Nummerierung, Striche oder Aufzählungszeichen enthalten, da diese automatisch formatiert werden.\n"
            "- Das Symbol für Leerzeichen ist **■**. Ändern Sie dieses Symbol NICHT, außer es entspricht nicht dem Standard.\n"

        )




