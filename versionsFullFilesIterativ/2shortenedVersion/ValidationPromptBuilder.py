class ValidationPromptBuilder:

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

    @staticmethod
    def create_refinement_validation_prompt():
        return (
            "Korrigieren Sie die Zustandsübergangstabelle und darauf basierend die Beispielablauftabelle "
            "(inkl. aller Spalten u Zeilen) so, dass beide vollständig, logisch konsistent und exakt auf die "
            "Anforderungen der Aufgabenstellung abgestimmt sind! Achte besonders auf den Erwarteten Output im Beispiel um die Aufgabe zu korrigeren!"
        )