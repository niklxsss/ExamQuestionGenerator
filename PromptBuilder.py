from Const import *


class PromptBuilder:

    # task_message -----------------------------------------------------------------------------------------------------

    @staticmethod
    def get_all_task_prompt(num_questions, difficulty, incorrect_task):
        return (
                PromptBuilder.get_task_base_prompt(num_questions, difficulty) +
                (PromptBuilder.get_incorrect_task_prompt() if incorrect_task else "") +
                PromptBuilder.get_task_general_guidelines_prompt(difficulty) +
                PromptBuilder.get_task_requirements_prompt() +
                PromptBuilder.get_task_request_prompt(num_questions)
        )

    @staticmethod
    def get_task_system_prompt(infos_present):
        base_prompt = (
            "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen für Informatik-Studierende an Universitäten erstellt.\n"
            "Dein Ziel ist es, qualitativ hochwertige und fehlerfreie Aufgaben zu erstellen, die den höchsten akademischen Standards entsprechen.\n"
            "Die Aufgaben müssen die Studierenden herausfordern und ein breites Spektrum an Konzepten und Funktionen von Turingmaschinen abdecken.\n"
            "Du bist dafür verantwortlich, alle Anforderungen des Nutzers präzise umzusetzen, deine Arbeit gründlich zu überprüfen und sicherzustellen, dass alle gelieferten Inhalte korrekt und konsistent sind.\n\n"
        )

        additional_info_prompt = (
            "### Vorgehensweise:\n"
            "1. **Verarbeitung von Zusatzinformationen:**\n"
            "- Du erhältst ein oder mehrere Informationstexte, Base64-kodierte Bilddateien oder PDF-Daten, die relevante Informationen zu den Aufgaben enthalten.\n"
            "- Analysiere diese Inhalte sorgfältig, um alle relevanten Details zu extrahieren, die für die Erstellung der Turingmaschinen-Aufgaben notwendig sind.\n"
            "- Stelle sicher, dass alle wichtigen Informationen aus diesen Quellen in den nächsten Schritten berücksichtigt werden.\n\n"

            "2. **Erstellung der Aufgaben:**\n"
            "- Verwende die analysierten Zusatzinformationen zusammen mit den übergebenen Anforderungen, um Turingmaschinen-Aufgaben zu erstellen.\n"
            "- Die Aufgaben müssen präzise, logisch aufgebaut und vollständig sein.\n"
            "- Achte darauf, dass jede Aufgabe so gestaltet ist, dass sie den Lernzielen und Prüfungsstandards entspricht.\n\n"

            "3. **Qualitätsprüfung:**\n"
            "- Überprüfe deine Arbeit gründlich, um sicherzustellen, dass keine Fehler oder Widersprüche vorliegen.\n"
            "- Validieren Sie alle erstellten Inhalte auf Konsistenz und Relevanz, bevor die Aufgabe abgeschlossen wird.\n\n"
            "Stelle sicher, dass alle Aufgaben und Inhalte den höchsten Qualitätsstandards entsprechen und direkt für den Einsatz in Prüfungen geeignet sind.\n\n"
        )

        if infos_present:
            return base_prompt + additional_info_prompt

        return base_prompt

    @staticmethod
    def get_task_base_prompt(num_questions, difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)
        difficulty_explanation = DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        return (
            "# Ziel der Aufgabe:\n\n"

            f"Generieren Sie genau **{num_questions}** Prüfungsaufgaben zu Turingmaschinen.\n\n"

            f"### Zielgruppe und Anforderungen:\n"
            f"Die Aufgaben sind speziell für Informatik-Studierende an Universitäten gedacht. "
            f"Sie sollen deren Verständnis und Anwendungskompetenz überprüfen und für Prüfungen geeignet sein.\n\n"

            f"### Schwierigkeitsgrad:\n"
            f"Die Aufgaben müssen dem Schwierigkeitsgrad '**{difficulty}**' entsprechen:\n"
            f"{difficulty_explanation}\n\n"

            "### Vielfältigkeit der Aufgaben:\n"
            "- Die generierten Aufgaben sollen unterschiedliche Aspekte und Funktionen von Turingmaschinen abdecken.\n"
            "- Vermeiden Sie Wiederholungen oder ähnliche Aufgabenstellungen innerhalb eines Aufgaben-Sets.\n"
            "- Achten Sie darauf, dass die Aufgaben abwechslungsreich sind und verschiedene Konzepte abdecken.\n\n"
        )

    @staticmethod
    def get_incorrect_task_prompt():
        return (
            "# Zusätzliche Informationen zum Auftrag:\n\n"

            "Erstellen Sie Aufgaben mit absichtlich fehlerhaften Turingmaschinen. Ziel ist es, das Fehlersuch- und "
            "Korrekturvermögen der Studierenden gezielt zu fördern, ohne dass die gesamte Tabelle fehlerhaft oder unverständlich wird.\n\n"

            "## Anforderungen an die Fehlerstruktur:\n"
            "- Die Turingmaschine soll exakt einen oder mehrere spezifische Fehler enthalten, die das gewünschte Ergebnis verhindern oder zu einem falschen Output führen.\n"
            "- **Alle anderen Übergänge und Zustände müssen korrekt sein** und den Anforderungen der Aufgabenstellung entsprechen, damit die Tabelle eine funktionierende Basis hat.\n"
            "- Fehler dürfen nicht zufällig eingefügt werden, sondern müssen gezielt platziert werden, sodass sie logisch nachvollziehbar sind und eine sorgfältige Analyse erfordern.\n"
            "- Fehler können auftreten in:\n"
            "   ⦁ **Zustandsübergängen** (z. B. fehlerhafte Zielzustände oder Übergangsregeln),\n"
            "   ⦁ **Lese- oder Schreibaktionen** (z. B. falsches oder fehlendes Schreib-Symbol),\n"
            "   ⦁ **Bandbewegungen** (z. B. falsche oder fehlende Bewegungsrichtung des Kopfes).\n\n"

            "## Anforderungen an die Tabelle:\n"
            "- **Korrektheit der Basis:** Alle Zustände und Übergänge, die keinen beabsichtigten Fehler enthalten, müssen korrekt und mit der Aufgabenstellung konsistent sein.\n"
            "- **Vollständigkeit:** Alle relevanten Informationen aus der Aufgabenstellung und den Zusatzinformationen müssen in der Tabelle korrekt berücksichtigt werden.\n"
            "- **Fehlergestaltung:** Fehler müssen subtil genug sein, um eine angemessene Herausforderung zu bieten, aber dennoch logisch nachvollziehbar bleiben.\n"
            "- **Formatierung:** Die Tabelle muss klar und präzise strukturiert sein. Alle Spalten und Zeilen (Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand) müssen vollständig und korrekt formatiert sein.\n\n"

            "## Hinweise für die Erstellung:\n"
            "- Führen Sie vor der Generierung der fehlerhaften Tabelle eine vollständige Simulation der Aufgabe durch, um sicherzustellen, dass die Basis korrekt ist.\n"
            "- Platzieren Sie die Fehler gezielt, ohne die grundlegende Funktionsweise der Maschine (außer an den fehlerhaften Stellen) zu beeinträchtigen.\n"
            "- Vermeiden Sie triviale Fehler, die sofort auffallen, sowie unnötig komplexe Fehler, die die Aufgabe übermäßig erschweren.\n"
            "- Überprüfen Sie die Tabelle abschließend darauf, dass nur die vorgesehenen Fehler enthalten sind und die restlichen Zustände und Übergänge korrekt funktionieren.\n\n"

            "Stellen Sie sicher, dass die Aufgabe sowohl eine Herausforderung darstellt als auch didaktisch sinnvoll ist, indem sie gezielt das Verständnis der Studierenden fördert.\n\n"
        )

    @staticmethod
    def get_task_general_guidelines_prompt(difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)

        return (
            "## Allgemeine Richtlinien:\n"
            "- **Sprache:** Alle Inhalte müssen klar und präzise auf Deutsch verfasst sein.\n"
            "- **Korrektheit:** Die Aufgaben und Beispiele müssen präzise, fehlerfrei und konsistent sein.\n"
            "- **Klarheit:** Vermeiden Sie Unklarheiten. Die Aufgabenstellung muss vollständig, eindeutig und für Studierende gut verständlich sein.\n"
            "- **Keine Hinweise:** Vermeiden Sie in der Aufgabenstellung jegliche Hinweise auf die Lösung oder den Lösungsweg. Die Aufgabenstellung soll nur das zu lösende Problem beschreiben.\n"
            "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen keine Nummerierungen, Striche oder Aufzählungszeichen an. Diese werden automatisch hinzugefügt und müssen nicht manuell integriert werden.\n\n"

            "## Einschränkungen und Komplexität:\n"
            "- **Kompatibilität mit Standard-Turingmaschinen:** Die Aufgaben müssen mit einer Standard-Turingmaschine lösbar sein. Zusätzliche Speicher- oder Zählmechanismen, die über den Rahmen einer einbandigen Turingmaschine hinausgehen, sind nicht zulässig.\n"
            f"- **Schwierigkeitsniveau:** Halten Sie die Aufgaben auf dem übergebenen Schwierigkeitsniveau '**{difficulty}**' und vermeiden Sie plötzliche Schwankungen innerhalb desselben Schwierigkeitsgrads.\n"
            "- **Realisierbarkeit:** Vermeiden Sie Operationen oder Berechnungen, die mit einer Standard-Turingmaschine nicht umsetzbar sind.\n\n"

            "Die Aufgaben sind direkt für Prüfungszwecke vorgesehen und müssen höchsten Ansprüchen an Richtigkeit, Vollständigkeit und Konsistenz genügen.\n\n"
        )

    @staticmethod
    def get_task_requirements_prompt():
        return (
            "## Spezifische Anforderungen an die Aufgabenstellung ('question'):\n"
            "- **Strikte Trennung:** Die 'question' muss **ausschließlich** das zu lösende Problem beschreiben und muss vollständig frei von technischen Details, Hinweisen oder Beispielen sein.\n"
            "- **Verbot für technische Details:** Die Frage ('question') darf keine Hinweise zu Leerzeichen, Begrenzungen, Start- oder Endpositionen oder anderen technischen Spezifikationen enthalten. Diese Informationen gehören ausschließlich in die Zusatzinformationen ('optional_question_additional_infos').\n"
            "- **Eindeutigkeit:** Die Formulierungen müssen klar und präzise sein, ohne Interpretationsspielraum.\n\n"

            "## Spezifische Anforderungen an die Zusatzinformationen ('optional_question_additional_infos'):\n"
            "- **Alphabet:** Geben Sie das verwendete Alphabet explizit an. Verwenden Sie für das Leerzeichen ausschließlich das Symbol `■` (Klartext, nicht in anderen Formaten).\n"
            "- **Bandinhalt:** Geben Sie an, dass die Eingabe links und rechts durch ein Leerzeichen `■` begrenzt ist. (Nicht das Band, das ist unendlich!)\n"
            "- **Konzepte und Prinzipien:** Falls die Aufgabe auf spezifischen Konzepten basiert, die möglicherweise nicht allen Studierenden direkt geläufig sind, erläutern Sie diese kurz.\n"
            "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann.\n"
            "  ⦁ Falls die Aufgabe so aufgebaut ist, dass sie in eine Bewegungsrichtung abgeschlossen werden kann, wählen Sie die Startposition entsprechend, um unnötige Bewegungen des Lesekopfes zu vermeiden.\n"
            "  ⦁ Simulieren Sie den Ablauf der Aufgabe basierend auf der Aufgabenstellung, den Zusatzinformationen und der Zielsetzung der Aufgabe. Bestimmen Sie daraufhin die logisch günstigste Startposition des Lese-/Schreibkopfs.\n"
            "  ⦁ Stellen Sie sicher, dass die gewählte Startposition konsistent mit der Zustandsübergangstabelle und dem Beispiel ist.\n"
            "  ⦁ Vermeiden Sie Widersprüche oder ineffiziente Startpositionen, die den Ablauf der Aufgabe unnötig komplizieren oder das Ziel der Aufgabe gefährden könnten.\n"
            "  ⦁ Die gilt auch für die Endposition!\n\n"

            "## Spezifische Anforderungen an das Beispiel ('example'):\n"
            "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar veranschaulicht.\n"
            "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n"
            "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende.\n"
            "- **Formatierung des Beispiels:** Das Beispiel muss immer im folgenden Format angegeben werden: `Eingabe: <Wert> | Ausgabe: <Wert>`.\n\n"
        )

    @staticmethod
    def get_task_request_prompt(num_questions):
        return (
            f"Erstellen Sie die **{num_questions}** Aufgabenstellungen und jeweils ein passendes Beispiel.\n"
            "Stellen Sie sicher, dass alle Inhalte vollständig, präzise und fehlerfrei sind.\n\n"
        )

    @staticmethod
    def get_task_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Aufgaben:\n"
            "Stellen Sie sicher, dass die Aufgabe vollständig, fehlerfrei und konsistent ist. Achten Sie auf folgende Punkte:\n\n"

            "### Aufgabenstellung und Zusatzinformationen:\n"
            "- Ist die Aufgabenstellung klar, präzise und vollständig?\n"
            "- Sind Zusatzinformationen konsistent mit der Aufgabenstellung und korrekt definiert?\n"
            "- Wurde die Start- und Endposition logisch und effizient gewählt, sodass die Aufgabe optimal gelöst werden kann?\n\n"

            "### Beispiel:\n"
            "- Veranschaulicht das Beispiel die Anforderungen der Aufgabe korrekt?\n"
            "- Stimmt das Beispiel mit der Aufgabenstellung und den Zusatzinformationen überein?\n\n"

            "### Verbesserungen:\n"
            "- Beheben Sie Fehler, Unklarheiten oder Widersprüche.\n"
            "- Stellen Sie sicher, dass alle Anpassungen die Qualität und Eignung der Aufgabe für Prüfungszwecke verbessern.\n"
        )

    @staticmethod
    def get_shared_info_text():
        return (
            "Falls die Inhalte direkt Aufgaben zu Turingmaschinen darstellen, dürfen diese nicht wörtlich übernommen werden. "
            "Nutzen Sie die Inhalte lediglich als Inspiration, um eigene, einzigartige Aufgaben zu erstellen.\n\n"
        )

    @staticmethod
    def get_txt_prompt():
        return (
                "## Kontextbezogene Information:\n"
                "Der folgende Abschnitt enthält wichtige Informationen, die bei der Erstellung der Aufgabe berücksichtigt werden sollen."
                "Nutzen Sie diese Inhalte, um die Aufgaben zu gestalten.\n"
                + PromptBuilder.get_shared_info_text()
        )

    @staticmethod
    def get_bas64_prompt():
        return (
                "## Bildbezogene Information:\n"
                "Das folgende Bild enthält kontextbezogene Informationen, die für die Erstellung der Aufgabe von Bedeutung sind. "
                "Analysieren Sie das Bild sorgfältig und integrieren Sie die relevanten Details in die Aufgaben sofern es sinnvoll ist.\n"
                + PromptBuilder.get_shared_info_text()
        )

    @staticmethod
    def get_pdf_texts_prompt():
        return (
                "## Informationen aus einer PDF-Quelle:\n"
                "Der folgende Abschnitt enthält Informationen, die aus einem PDF-Dokument extrahiert wurden. "
                "Nutzen Sie diese Inhalte, um die Aufgabe zu gestalten.\n"
                + PromptBuilder.get_shared_info_text()
        )

    # state_transition_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_all_state_transition_table_prompt(task_parts):
        return (
                PromptBuilder.get_state_transition_table_requirements_prompt() +
                PromptBuilder.get_state_transition_table_request_prompt() +
                PromptBuilder.get_state_transition_table_quality_prompt()
        )

    @staticmethod
    def get_state_transition_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das eine Zustandsübergangstabelle für eine gegebene Turingmaschinen erstellt."
            "Dein Ziel ist es, eine Tabelle zu generieren, die die Anforderungen der Aufgabenstellung, Zusatzinformationen "
            "und des Beispiels vollständig und effizient umsetzt. Die Tabelle muss den höchsten akademischen Standards entsprechen "
            "und für alle möglichen Eingaben die korrekten Ergebnisse liefern.\n\n"

            "### Prozessübersicht:\n"
            "1. **Aufgabenstellung:**\n"
            "   Zunächst erhältst du die vollständige Aufgabenstellung, auf deren Basis du die Zustandsübergangstabelle erstellen sollst.\n\n"
            "2. **Spezifische Anforderungen:**\n"
            "   Anschließend werden dir spezifische Anforderungen übermittelt, die sicherstellen, dass die Tabelle konsistent, korrekt und effizient ist.\n\n"
            "3. **Generierung der Tabelle:**\n"
            "   Erstelle die Zustandsübergangstabelle basierend auf der erhaltenen Aufgabenstellung und den spezifischen Anforderungen.\n\n"
            "4. **Korrektur und Validierung:**\n"
            "   Nach der Generierung überprüfst du die Tabelle auf Fehler oder Unstimmigkeiten und nimmst, falls erforderlich, Korrekturen vor, um eine fehlerfreie und konsistente Tabelle zu gewährleisten.\n\n"
        )

    @staticmethod
    def get_state_transition_table_task_prompt(task_parts):
        return (
            f"AUFGABENSTELLUNG UND BEISPIEL:\n\n{task_parts}\n\n"
        )

    @staticmethod
    def get_state_transition_table_requirements_prompt():
        return (
            "## Anforderungen an die Zustandsübergangstabelle ('solution_state_transition_table'):\n\n"

            "### Analyse der Aufgabenstellung:\n"
            "- Verstehen Sie die Anforderungen und Zielsetzung der Aufgabe vollständig, einschließlich der Start- und Endposition.\n"
            "- Beachten Sie: Wenn in der Aufgabenstellung steht, dass der Kopf auf dem ersten oder letzten Symbol der Eingabe startet, ist damit das **erste tatsächliche Symbol** der Eingabe gemeint und **kein Leerzeichen**, es sei denn, es ist explizit angegeben.\n"
            "- Simulieren Sie den Ablauf der Turingmaschine intern mit verschiedenen Eingaben, um die effizienteste Lösung zu finden.\n\n"

            "### Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Tabelle muss die Zielsetzung der Aufgabe präzise und effizient umsetzen.\n"
            "- Stellen Sie sicher, dass alle Zustände und Übergänge exakt den Vorgaben der Aufgabenstellung und Zusatzinformationen entsprechen.\n"
            "- Erstelle die Tabelle so, dass sie mit der Start- und Endposition der Aufgabenstellung konsistent ist!\n"
            "- Jeder Übergang und jede Zustandsänderung muss darauf ausgelegt sein, das spezifizierte Ziel der Aufgabe zu erreichen.\n"
            "- Vermeiden Sie Annahmen oder Ergänzungen, die nicht explizit in der Aufgabenstellung beschrieben sind.\n\n"

            "### Struktur und Vollständigkeit:\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände, einschließlich Start- und Endzustände, sowie alle Übergänge müssen abgedeckt sein. Sonderzeichen wie Leerzeichen `■` sind einzubeziehen.\n"
            "- **Eindeutigkeit:** Jeder Übergang muss klar definiert sein.\n"
            "- **Handling von Bandgrenzen:** Falls der Schreib-/Lesevorgang über die ursprüngliche Eingabe hinausgeht, stellen Sie sicher, dass Leerzeichen korrekt verarbeitet werden und der Übergang weiterhin konsistent bleibt.\n\n"

            "### Logik und Effizienz:\n"
            "- Die Zustandsübergänge sollten die Aufgabe mit minimalem Aufwand und maximaler Effizienz umsetzen.\n"
            "- Vermeiden Sie unnötige Zustände oder Bewegungen, die die Tabelle komplizierter machen.\n"
            "- Validieren Sie intern jeden Zustand und Übergang, um sicherzustellen, dass keine Fehler oder Lücken vorhanden sind.\n"
            "- Simulieren Sie die Tabelle mit mehreren Eingaben, um sicherzustellen, dass alle möglichen Szenarien korrekt abgedeckt sind.\n\n"

            "### Zusätzliche Hinweise:\n"
            "- **Konsistenz:** Vergewissern Sie sich, dass alle Zustände und Übergänge logisch miteinander verbunden sind.\n"
            "- **Präzision:** Dokumentieren Sie jeden Zustand und jede Änderung ohne Unstimmigkeiten oder Lücken.\n"
            "- **Überprüfung:** Kontrollieren Sie, ob die Tabelle für Prüfungszwecke geeignet ist und höchsten Qualitätsstandards entspricht.\n\n"
        )

    @staticmethod
    def get_state_transition_table_request_prompt():
        return (
            "Erstellen Sie eine korrekte allumfassende Zustandsübergangstabelle auf Basis der Aufgabenstellung, Zusatzinformationen und des Beispiels.\n\n"
        )

    @staticmethod
    def get_state_transition_table_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Zustandsübergangstabelle:\n"
            "Stellen Sie sicher, dass die Zustandsübergangstabelle vollständig, korrekt und konsistent ist.\n"
            "Gehen Sie davon aus, dass Fehler enthalten sind!\n\n"

            "### Fehlerkorrektur:\n"
            "Falls Fehler oder Unstimmigkeiten auftreten, **VERBESSERN** Sie die Tabelle entsprechend und validieren Sie diese erneut!\n\n"

            "# Verbessern Sie folgenden Punkte:\n\n"

            "### Aufgabenbezogene Überprüfung:\n"
            "- Stimmen die Zustände und Übergänge mit der Aufgabenstellung, den Zusatzinformationen und dem Beispiel überein?\n"
            "- Wurden alle relevanten Anforderungen der Aufgabenstellung korrekt berücksichtigt?\n"
            "- Vergewissern Sie sich, dass die Tabelle vollständig konsistent mit der Aufgabenstellung ist, einschließlich der definierten Start- und Endposition.\n\n"

            "### Technische Überprüfung:\n"
            "- **Vollständigkeit:** Sind alle möglichen Zustände und Übergänge abgedeckt, einschließlich Sonderzeichen wie Leerzeichen `■`?\n"
            "- **Logik und Effizienz:** Ist die Abfolge der Zustände logisch und effizient?\n"
            "- **Kopfbewegung:** Sind die Bewegungen des Lesekopfes präzise und entsprechend der Aufgabenstellung definiert?\n\n"

            "### Überprüfung mit Testeingaben:\n"
            "- Validieren Sie die Zustandsübergangstabelle mit mehreren Testeingaben, um sicherzustellen, dass sie für verschiedene Szenarien korrekte Ergebnisse liefert.\n"
            "- Stellen Sie sicher, dass alle möglichen Ergebnisse der Aufgabenstellung korrekt und wie vorgesehen erreicht werden.\n\n"

            "### Abschließende Validierung:\n"
            "- Überprüfen Sie, ob die Tabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Stellen Sie sicher, dass keine logischen Widersprüche oder Fehler vorhanden sind.\n\n"
        )

    # example_flow_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_all_example_flow_table_prompt(task_parts):
        return (
                PromptBuilder.get_example_flow_table_requirements_prompt() +
                PromptBuilder.get_example_flow_table_request_prompt()
        )

    @staticmethod
    def get_example_flow_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das eine Beispielablauftabelle für eine gegebene Turingmaschine erstellt!\n"
            "Dein Ziel ist es, auf Basis der Aufgabenstellung, der Zusatzinformationen, des Beispiels und der Zustandsübergangstabelle, "
            "eine fehlerfreie, konsistente und qualitativ hochwertige Tabelle zu erstellen.\n"
            "Die Tabelle muss den höchsten akademischen Standards entsprechen und für das gegebene Beispiel, den fehlerfreien Ablauf aufzeigen.\n\n"

            "### Prozessübersicht:\n"
            "1. **Aufgabenstellung:**\n"
            "   Zunächst erhältst du die vollständige Aufgabenstellung und Zustandsübergangstabelle, auf deren Basis du die Beispielablauftabelle erstellen sollst.\n\n"
            "2. **Spezifische Anforderungen:**\n"
            "   Anschließend werden dir spezifische Anforderungen übermittelt, die sicherstellen, dass die Tabelle konsistent, korrekt und effizient ist.\n\n"
            "3. **Generierung der Tabelle:**\n"
            "   Erstelle die Beispielablauftabelle basierend auf der erhaltenen Aufgabenstellung, Zustandsübergangstabelle und den spezifischen Anforderungen.\n\n"
            "4. **Korrektur und Validierung:**\n"
            "   Nach der Generierung überprüfst du die Tabelle auf Fehler oder Unstimmigkeiten und nimmst, falls erforderlich, Korrekturen vor, um eine fehlerfreie und konsistente Tabelle zu gewährleisten.\n\n"
        )

    @staticmethod
    def get_example_flow_table_task_prompt(task_parts):
        return (
            f"AUFGABENSTELLUNG UND ZUSTANDSÜBERGANGSTABELLE: {task_parts}\n\n"
        )

    @staticmethod
    def get_example_flow_table_requirements_prompt():
        return (
            "## Anforderungen an die Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle, dem Beispiel, sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Start- Endposition** Die Start- und Endposition muss korrekt und konsistent mit den Angaben in der Aufgabenstellung sein.\n"

            "- **Kopfposition:** Geben Sie die Kopfposition ausschließlich als numerischen Wert der aktuellen Position des Lesekopfes an.\n"
            "  ⦁ Die Nummerierung beginnt immer bei **1** und wird bei jedem Schritt der Turingmaschine fortlaufend aktualisiert.\n"
            "  ⦁ Falls der Lesekopf das linke Ende des sichtbaren Bandbereichs überschreitet, setzen Sie die Nummerierung negativ fort, beginnend mit **0**, **-1**, **-2**, und so weiter. Dadurch wird jede Bewegung des Lesekopfes lückenlos dokumentiert.\n"
            "  ⦁ Die Kopfposition muss für jeden Schritt eindeutig angegeben werden, sodass der gesamte Ablauf der Turingmaschine präzise und nachvollziehbar bleibt.\n"

            "- **Bandinhalt:** Der Bandinhalt muss vollständig angezeigt werden, einschließlich der Begrenzungsleerzeichen (`■`) links und rechts der Eingabe. Markieren Sie die aktive Kopfposition durch eine Umrahmung `[ ]` (z. B. `■11[0]1■`).\n"
            "- **Anwendung der Übergangsregeln:** Setzen Sie die Übergangsregeln korrekt um, indem der Bandinhalt bei jedem Schreibvorgang aktualisiert und die Kopfbewegung dokumentiert wird.\n"
            "- **Vollständigkeit:** Die Tabelle muss alle relevanten Zustandsänderungen, Kopfbewegungen und Übergänge dokumentieren, die erforderlich sind, um die Eingabe korrekt zu verarbeiten.\n"

            "- **Übergangsregeln:**\n"
            "  ⦁ Setzen Sie die Übergangsregeln korrekt um und validieren Sie nach jedem Schritt, ob die aktuellen Änderungen (Zustand, Bandinhalt, Kopfposition) mit der Zustandsübergangstabelle übereinstimmen.\n"
            "  ⦁ Überprüfen Sie jede Zeile einzeln, um sicherzustellen, dass keine Abweichungen oder Fehler auftreten. Falls Anpassungen erforderlich sind, korrigieren Sie diese konsequent.\n\n"

            "## Schrittweise Validierung:**\n"
            "- Validieren Sie nach jedem erstellten Schritt, ob dieser mit der Zustandsübergangstabelle übereinstimmt.\n"
            "- Überprüfen Sie, ob Anpassungen oder Korrekturen erforderlich sind, und übertragen Sie diese in die Tabelle, bevor der nächste Schritt erstellt wird.\n"
        )

    @staticmethod
    def get_example_flow_table_request_prompt():
        return (
            "**Erstellen Sie eine korrekte allumfassende Beispielablauftabelle auf Basis der Zustandsübergangstabelle, Aufgabenstellung, Zusatzinformationen und des Beispiels!**\n\n"
        )

    @staticmethod
    def get_example_flow_table_quality_prompt():
        return (
            "## Überprüfung und Korrektur der Beispielablauftabelle:\n"
            "Die Beispielablauftabelle enthält immer Fehler oder Unstimmigkeiten. Ihre Aufgabe ist es, diese Fehler zu identifizieren und die Tabelle so zu korrigieren, dass sie vollständig, korrekt und konsistent ist. Gehen Sie dabei die folgenden Punkte durch:\n\n"

            "### Fehlerkorrektur:\n"
            "- Identifizieren Sie gezielt alle Fehler in der Tabelle, einschließlich logischer Widersprüche, falscher Übergänge oder inkorrekter Kopfbewegungen.\n"
            "- Korrigieren Sie die Tabelle so, dass sie alle Anforderungen erfüllt und das Ziel der Aufgabe präzise abbildet.\n"
            "- Validieren Sie die Korrekturen abschließend, um sicherzustellen, dass keine weiteren Fehler vorhanden sind.\n\n"

            "### Aufgabenbezogene Überprüfung:\n"
            "- Entspricht die Tabelle den Anforderungen der Aufgabenstellung, den Zusatzinformationen und dem Beispiel?\n"
            "- Ist die Tabelle konsistent mit der Zustandsübergangstabelle und sind alle relevanten Übergänge, Bewegungen und Zustandsänderungen dokumentiert?\n"
            "- Sind Start- und Endposition korrekt und konsistent mit den Angaben in der Aufgabenstellung?\n\n"

            "### Technische Überprüfung:\n"
            "- **Kopfposition:** Ist die Kopfposition korrekt nummeriert und synchron mit der tatsächlichen Position des Lesekopfes in jedem Schritt?\n"
            "- **Bandinhalt:** Wird der Bandinhalt in jedem Schritt korrekt aktualisiert, einschließlich der Markierung der aktiven Kopfposition durch `[ ]`?\n"
            "- **Übergangsregeln:** Sind alle Übergangsregeln korrekt und vollständig umgesetzt?\n"
            "- **Vollständigkeit:** Sind alle Zustandsänderungen und Kopfbewegungen dokumentiert, und gibt es keine Lücken oder Auslassungen?\n\n"

            "### Validierung des Ablaufs:\n"
            "- Überprüfen Sie, ob der Ablauf exakt mit den Vorgaben der Aufgabenstellung, des Beispiels und der Zustandsübergangstabelle übereinstimmt.\n"
            "- Validieren Sie, dass das erwartete Ergebnis des Beispiels (Ausgabe) korrekt erreicht wird.\n"
            "- Prüfen Sie, ob die Tabelle für alle Szenarien und mögliche Eingaben korrekt funktioniert und keine zusätzlichen Fehler auftreten.\n\n"

            "### Abschließende Validierung:\n"
            "- Stellen Sie sicher, dass die Tabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Überprüfen Sie, ob alle Unstimmigkeiten und Fehler beseitigt wurden.\n\n"
        )

    # solution_message ----------------------------------------------------------------------------------

    # @staticmethod
    # def get_all_solution_prompt(task_parts):
    #     return (
    #             PromptBuilder.get_solution_requirements_prompt() +
    #             PromptBuilder.get_solution_request_prompt(task_parts) +
    #             PromptBuilder.get_solution_quality_prompt()
    #     )

    @staticmethod
    def get_solution_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Lösungen für Turingmaschinenaufgaben erstellt. "
            "Dein Ziel ist es, qualitativ hochwertige, fehlerfreie und konsistente Lösungen zu erstellen, "
            "die speziell für akademische Prüfungen im Bereich Informatik geeignet sind.\n\n"
            "Beachte die Vorgaben des Benutzers und stelle sicher, dass alle Ergebnisse präzise, vollständig und nachvollziehbar sind.\n\n"
        )

    @staticmethod
    def get_solution_requirements_prompt():
        return (
            "### Spezifische Anforderungen an die Lösung:\n"
            "- **Lösung ('solution')**: Erstellen Sie eine konzeptionelle Beschreibung des Lösungsansatzes.\n"
            "- **Zusätzliche Informationen ('optional_solution_additional_infos')**: Geben Sie hier optional Details oder Hintergrundinformationen an, die das Verständnis der Lösung verbessern.\n"
            "- **Lösungsweg ('optional_solution_step_by_step')**:Beschreiben Sie den Lösungsweg Schritt für Schritt in Textform (ohne Tabellen oder Aufzählungszeichen).\n"
            "- **Zusätzliche Tabellen ('optional_additional_solution_tables'):** Tabellen können optional verwendet werden, um komplexe Aufgaben klarer darzustellen, z. B. Zustandsbeschreibungstabellen.\n"
            "- **Formatierung von Aufzählungen:** Geben Sie bei Aufzählungen **keine Nummerierungen, Striche oder Aufzählungszeichen an**. Diese werden automatisch hinzugefügt.\n\n"

            "### Überprüfung und Qualitätssicherung:\n"
            "- Stellen Sie sicher, dass die Lösung vollständig, korrekt und konsistent ist.\n"
            "- Prüfen Sie, dass alle Anforderungen erfüllt sind und die Ergebnisse den erwarteten Ausgaben entsprechen.\n"
            "- Verbessern Sie die Lösung, falls Fehler oder Unstimmigkeiten gefunden werden.\n"
        )

    @staticmethod
    def get_solution_request_prompt(task_parts):
        return (
            f"Aufgabenstellung und Tabelle:\n\n {task_parts}\n\n"
            "Erstellten Sie den rest der Lösung wie angegeben auf Basis der übergebenen Inhalte und baue die Aufgabe im übergebenen Format ExamQuestion zusammen!\n"
        )

    @staticmethod
    def get_solution_quality_prompt():
        return (
            "## Überprüfung und Verbesserung der Aufgabe:\n"
            "Stellen Sie sicher, dass die Lösung vollständig, korrekt und konsistent ist. Gehen Sie dabei die folgenden Punkte durch:\n\n"

            "### Fehlerkorrektur:\n"
            "- Falls Fehler oder Unstimmigkeiten auftreten, verbessern Sie die Lösung entsprechend und validieren Sie diese erneut.\n\n"

            "### Aufgabenbezogene Überprüfung:\n"
            "- Ist die konzeptionelle Beschreibung des Lösungsansatzes klar und nachvollziehbar?\n"
            "- Stimmen die zusätzlichen Informationen mit der Aufgabenstellung und den anderen Elementen wie der Zustandsübergangstabelle überein?\n"
            "- Ist der Lösungsweg logisch aufgebaut, fehlerfrei und vollständig beschrieben?\n\n"

            "### Abschließende Validierung:\n"
            "- Entspricht die gesamte Lösung den höchsten Qualitätsstandards und ist sie für Prüfungszwecke geeignet?\n"
            "- Sind alle Abschnitte der Lösung konsistent und frei von logischen Widersprüchen?\n\n"
        )
