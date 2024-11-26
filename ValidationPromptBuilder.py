class ValidationPromptBuilder:

    @staticmethod
    def create_prefix_validation_prompt():
        return [
            ValidationPromptBuilder.get_base_description(),
            ValidationPromptBuilder.get_correction_steps(),
            # format??
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
            
            "Ihre Aufgabe ist es, die Prüfungsaufgabe zu Turingmaschinen zu korrigieren und zu verbessern. "
            "Die Aufgabe muss vollständig korrekt, logisch konsistent und für Prüfungszwecke geeignet sein.\n\n"
            
            "**Hauptziele:**\n"
            "- Identifizieren Sie alle Fehler in der Aufgabenstellung, Beispiel, Lösung, Zustandsübergangstabelle und Beispielablauftabelle.\n"
            "- Beheben Sie alle Fehler und stellen Sie sicher, dass die korrigierte Aufgabe den höchsten Anforderungen entspricht.\n"
            "- Keine fehlerhafte oder unvollständige Aufgabe darf zurückgegeben werden.\n\n"

            "**Verhindern Sie:** \n"
            "- Jegliche Rückgabe der ursprünglichen, unkorrigierten Aufgabe.\n"
            "- Fehlerhafte oder unvollständige Anpassungen, die neue Fehler einführen könnten.\n"
            "- Dass aufgrund von Mapping- oder Verarbeitungsfehlern die ursprüngliche, unkorrigierte Aufgabe zurückgesendet wird.\n\n"
        )

    @staticmethod
    def get_correction_steps():
        return (
            "# Schritte zur Korrektur:\n\n"
            
            "## Aufgabenstellung und Beispiel validieren und korrigieren:\n"
            "- **Überprüfen Sie die Aufgabenstellung auf Klarheit und Vollständigkeit:**\n"
            "  ⦁ Die Frage muss eindeutig, präzise und ohne Interpretationsspielraum formuliert sein.\n"
            "  ⦁ Alle relevanten Informationen (z. B. Eingabe, gewünschtes Verhalten, Endzustände) müssen enthalten sein.\n"
            "  ⦁ Überprüfen Sie, ob die Anforderungen der Aufgabe logisch und mit einer Turingmaschine umsetzbar sind.\n\n"

            "- **Fehlerbehebung in der Aufgabenstellung:**\n"
            "  ⦁ Passen Sie Formulierungen an, die mehrdeutig oder unklar sind.\n"
            "  ⦁ Ergänzen Sie fehlende Details, die für die Lösung der Aufgabe notwendig sind.\n\n"

            "- **Beispiel validieren und korrigieren:**\n"
            "  ⦁ Überprüfen Sie, ob das Beispiel das erwartete Verhalten der Turingmaschine korrekt abbildet.\n"
            "  ⦁ Vergewissern Sie sich, dass Eingabe und erwartetes Ergebnis logisch und korrekt sind.\n"
            "  ⦁ Ergänzen Sie Beispiele oder korrigieren Sie diese, falls sie fehlerhaft oder unvollständig sind.\n\n"

            "## Zustandsübergangstabellen validieren und korrigieren:\n"
            "- **Überprüfen Sie jede Zustandsübergangstabelle auf Vollständigkeit, Konsistenz und Korrektheit:**\n"
            "  ⦁ Alle Zustände müssen dokumentiert sein, einschließlich Start-, Zwischen- und Endzustände.\n"
            "  ⦁ Jede Übergangsregel muss klar definiert sein: aktueller Zustand, gelesenes Zeichen, neues Zeichen, Bewegung und neuer Zustand.\n"
            "  ⦁ **Keine Lücken:** Vergewissern Sie sich, dass alle möglichen Eingaben (einschließlich Sonderzeichen wie ⋄) für jeden relevanten Zustand abgedeckt sind.\n"
            "  ⦁ Jeder Zustand muss logisch erreichbar sein, und keine redundanten Zustände oder Übergänge dürfen vorhanden sein.\n\n"

            "- **Fehlerbehebung:**\n"
            "  ⦁ Ergänzen Sie fehlende Zustände, Übergänge oder Sonderfälle.\n"
            "  ⦁ Korrigieren Sie fehlerhafte Einträge vollständig, um sicherzustellen, dass die Tabelle konsistent und fehlerfrei ist.\n\n"

            "- **Wenn keine Zustandsübergangstabelle vorhanden ist:**\n"
            "  ⦁ Erstellen Sie eine neue, die den Anforderungen entspricht und die gesamte Aufgabe abdeckt.\n"
            "  ⦁ Verwenden Sie eine strukturierte Darstellung mit klaren Spalten für Zustand, Übergang und Bewegung.\n\n"

            "## Beispielabläufe validieren und ergänzen:\n"
            "- **Korrektheit sicherstellen:**\n"
            "  ⦁ Überprüfen Sie, ob die Beispielausgabe mit dem Endzustand und Bandinhalt der Beispielablauftabelle übereinstimmt.\n"
            "  ⦁ Verifizieren Sie, dass jeder Schritt (Bandzustand, Kopfposition, aktueller Zustand) präzise dokumentiert ist.\n"
            "  ⦁ **Konsistenz:** Alle Schritte müssen mit der Zustandsübergangstabelle und der Aufgabenstellung übereinstimmen.\n\n"

            "- **Fehlende Schritte ergänzen:**\n"
            "  ⦁ Wenn Zwischenschritte fehlen oder unklar sind, erweitern Sie die Tabelle vollständig, um den gesamten Ablauf abzubilden.\n"
            "  ⦁ Jeder Schritt muss den Übergang im Kontext der Zustandsübergangstabelle nachvollziehbar machen.\n"
            "  ⦁ Markieren Sie klar die Position des Kopfes bei jedem Schritt.\n\n"

            "## Konsistenz zwischen Tabellen und Aufgabe sicherstellen:\n"
            "- **Überprüfung der Zusammenhänge:**\n"
            "  ⦁ Vergewissern Sie sich, dass die Zustandsübergangstabelle, Beispielablauftabelle und Aufgabenstellung logisch zusammenpassen.\n"
            "  ⦁ Diskrepanzen zwischen den Tabellen und der Aufgabenstellung müssen vollständig korrigiert werden.\n\n"

            "## Tabellen auf Vollständigkeit und Logik prüfen:\n"
            "- **Detaillierte Überprüfung:**\n"
            "  ⦁ Sicherstellen, dass keine Übergänge oder Zustände fehlen.\n"
            "  ⦁ Überprüfen Sie, ob alle Schritte und Zustände logisch aufeinander aufbauen und keine widersprüchlichen Übergänge enthalten sind.\n\n"

            "- **Iterative Fehlerkorrektur:**\n"
            "  ⦁ Falls Fehler oder Unstimmigkeiten auftreten, überarbeiten Sie die Tabellen iterativ.\n"
            "  ⦁ Testen Sie die korrigierten Tabellen mit der Aufgabenstellung und den Beispielen, um sicherzustellen, dass keine weiteren Probleme bestehen.\n\n"

            "- **Grenzfälle berücksichtigen:**\n"
            "  ⦁ Stellen Sie sicher, dass die Maschine in allen Fällen korrekt reagiert und keine undefinierten Zustände auftreten.\n"
        )

    @staticmethod
    def get_final_check():
        return (
            "# Abschlussprüfung:\n\n"

            "**Vor der Rückgabe:**\n"
            "- **Überprüfen Sie die gesamte Aufgabe, einschließlich aller Tabellen und Beispiele, auf vollständige Korrektheit und Konsistenz.**\n"
            "- Stellen Sie sicher, dass jede Tabelle vollständig ist, alle Zwischenschritte und Übergänge korrekt dokumentiert und keine Lücken oder Inkonsistenzen aufweist.\n"
            "- **Überprüfen und korrigieren Sie die Aufgabe so, dass alle Tabellen mit der Aufgabenstellung und dem Beispiel logisch konsistent sind.**\n"
            "- **Ersetzen Sie die ursprüngliche Aufgabe vollständig durch die korrigierte und verbesserte Version.**\n"
            "- GEBEN SIE AUSSCHLIEßLICH DIE ÜBERARBEITETE AUFGABE ZURÜCK. DIE RÜCKGABE EINER UNVERÄNDERTE FALSCHEN AUFGABE IST NICHT ZULÄSSIG!\n\n"

            "**Wichtige Hinweise:**\n"
            "-**Die Aufgabe MUSS ZWINGEND vollständig fehlerfrei, in sich schlüssig, klar formuliert und logisch konsistent sein.**\n"
            "-**Eine Rückgabe, die nicht den Vorgaben entspricht, ist inakzeptabel!!!**\n\n"
        )