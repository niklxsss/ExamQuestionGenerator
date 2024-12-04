from Const import *


class PromptBuilder:
    # evtl quality seperat in prompt

    # task_message -----------------------------------------------------------------------------------------------------

    @staticmethod
    def get_all_task_prompt(num_questions, difficulty, incorrect_task):
        return (
                PromptBuilder.get_task_base_prompt(num_questions, difficulty) +
                (PromptBuilder.get_incorrect_task_prompt()if incorrect_task else "") +
                PromptBuilder.get_task_general_guidelines_prompt(difficulty) +
                PromptBuilder.get_task_requirements_prompt() +
                PromptBuilder.get_task_request_prompt(num_questions)
                # PromptBuilder.get_task_quality_prompt()
        )

    @staticmethod
    def get_task_system_prompt(infos_present):
        base_prompt = (
            "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen für Informatik-Studierende an Universitäten erstellt.\n"
            "Dein Ziel ist es, Aufgaben zu generieren, die fehlerfrei, konsistent und von höchster Qualität sind.\n"
            "Diese Aufgaben sind direkt für Prüfungszwecke vorgesehen und müssen den höchsten akademischen Standards entsprechen.\n"
            "Du bist dafür verantwortlich, alle Anforderungen des Nutzers präzise umzusetzen, deine Arbeit gründlich zu überprüfen und sicherzustellen, dass alle gelieferten Inhalte korrekt und konsistent sind.\n\n"
        )

        additional_info_prompt = (
            "### Vorgehensweise:\n"
            "1. **Verarbeitung von Zusatzinformationen:**\n"
            "- Du erhältst entweder Informationstexte, Base64-kodierte Bilddateien oder PDF-Daten, die relevante Informationen zu den Aufgaben enthalten.\n"
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

            # "Beachten Sie, dass diese Aufgaben speziell darauf abzielen, die Analyse- und Problemlösungsfähigkeiten der Studierenden zu überprüfen.\n\n"
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
            "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende (z. B. `■11010■`).\n"
            # "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende.\n"
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
            "Stellen Sie sicher, dass die gesamte Aufgabe korrekt, vollständig und konsistent ist. "
            "Die Überprüfung sollte sich an den folgenden Punkten orientieren:\n\n"

            "### Aufgabenstellung und Beispiel:\n"
            "- Erfüllt die Aufgabe alle Qualitätsstandards und ist sie für Prüfungszwecke geeignet?\n"
            "- Sind alle Abschnitte der Aufgabe konsistent und ohne logische Widersprüche?\n"
            "- Ist die Aufgabenstellung klar, präzise und frei von technischen Details oder Hinweisen, die in die Zusatzinformationen gehören?\n"
            "- Passen die Zusatzinformationen zur Aufgabenstellung, und enthalten sie keine widersprüchlichen oder fehlenden Angaben?\n"
            "- Stimmt das Beispiel mit der Aufgabenstellung überein und veranschaulicht es die Anforderungen korrekt?\n"
            "- Ist die Start- und Endposition so definieren, dass die Startposition des Kopfes so gewählt ist, dass die Aufgabe am effizientesten und logischsten gelöst werden kann.\n\n"
            
            "### Verbesserungen:\n"
            "- Überarbeiten Sie die Aufgabe, wenn Fehler, Unklarheiten oder Widersprüche festgestellt werden.\n"
            "- Stellen Sie sicher, dass alle Änderungen die Qualität und Konsistenz der Aufgabe verbessern.\n\n"
        )

    @staticmethod
    def get_txt_prompt():
        return (
            "## Kontextbezogene Information:\n"
            "Der folgende Abschnitt enthält wichtige Informationen, die bei der Erstellung der Aufgabe berücksichtigt werden sollen. "
            "Nutzen Sie diese Inhalte, um die Aufgaben zu gestalten.\n\n"
        )

    @staticmethod
    def get_bas64_prompt():
        return (
            "## Bildbezogene Information:\n"
            "Das folgende Bild enthält kontextbezogene Informationen, die für die Erstellung der Aufgabe von Bedeutung sind. "
            "Analysieren Sie das Bild sorgfältig und integrieren Sie die relevanten Details in die Aufgaben sofern es sinnvoll ist.\n\n"
        )

    @staticmethod
    def get_pdf_texts_prompt():
        return (
            "## Informationen aus einer PDF-Quelle:\n"
            "Der folgende Abschnitt enthält Informationen, die aus einem PDF-Dokument extrahiert wurden. "
            "Nutzen Sie diese Inhalte, um die Aufgabe zu gestalten.\n\n"
        )

    # state_transition_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_all_state_transition_table_prompt(task_parts):
        return (
                PromptBuilder.get_state_transition_table_requirements_prompt() +
                PromptBuilder.get_state_transition_table_request_prompt(task_parts)
                # PromptBuilder.get_state_transition_table_quality_prompt()
        )

    @staticmethod
    def get_state_transition_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Zustandsübergangstabellen für Turingmaschinen erstellt. "
            "Dein Ziel ist es, Tabellen zu generieren, die die Anforderungen der Aufgabenstellung, Zusatzinformationen "
            "und des Beispiels vollständig und effizient umsetzen. Die Tabellen müssen den höchsten akademischen Standards entsprechen "
            "und für alle möglichen Eingaben die korrekten Ergebnisse liefern.\n\n"

            "## Vorgehensweise:\n"
            "1. **Analyse der Aufgabenstellung:** Analysieren Sie die Zielsetzung, Zusatzinformationen und das Beispiel so wie die Start und Endposition, um die Aufgabe vollständig zu verstehen.\n"
            "2. **Simulation:** Simulieren Sie den Ablauf der Turingmaschine intern mit verschiedenen möglichen Eingaben, um die effizienteste und logischste Lösung zu identifizieren.\n"
            "3. **Effiziente Generierung:** Erstellen Sie die Zustandsübergangstabelle so einfach wie möglich, ohne unnötige Zustände oder Übergänge einzufügen.\n"
            "4. **Validierung:** Überprüfen Sie, ob die Tabelle für alle Eingaben korrekt funktioniert und das spezifizierte Ziel der Aufgabe erreicht.\n"
            "5. **Korrektur:** Passen Sie die Tabelle bei Bedarf an, um Konsistenz und Vollständigkeit sicherzustellen.\n"
        )

    @staticmethod
    def get_state_transition_table_requirements_prompt():
        return (
            "## Anforderungen an die Zustandsübergangstabelle ('solution_state_transition_table'):\n\n"

            "### Analyse der Aufgabenstellung:\n"
            "- Verstehen Sie die Anforderungen und Zielsetzung der Aufgabe vollständig, einschließlich der Start- und Endposition.\n"
            "- Simulieren Sie den Ablauf der Turingmaschine intern mit verschiedenen Eingaben, um die effizienteste Lösung zu finden.\n\n"

            "### Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Tabelle muss die Zielsetzung der Aufgabe präzise und effizient umsetzen.\n"
            "- Stellen Sie sicher, dass alle Zustände und Übergänge exakt den Vorgaben der Aufgabenstellung und Zusatzinformationen entsprechen.\n"
            "- Jeder Übergang und jede Zustandsänderung muss darauf ausgelegt sein, das spezifizierte Ziel der Aufgabe zu erreichen.\n"
            "- Vermeiden Sie Annahmen oder Ergänzungen, die nicht explizit in der Aufgabenstellung beschrieben sind.\n\n"

            "### Struktur und Vollständigkeit:\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände, einschließlich Start- und Endzustände, sowie alle Übergänge müssen abgedeckt sein. Sonderzeichen wie Leerzeichen `■` sind einzubeziehen.\n"
            "- **Eindeutigkeit:** Jeder Übergang muss klar und ohne Mehrdeutigkeit definiert sein.\n\n"

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
    def get_state_transition_table_request_prompt(task_parts):
        return (
            f"AUFGABENSTELLUNG UND BEISPIEL:\n\n{task_parts}\n\n"
            "Erstellen Sie eine Zustandsübergangstabelle auf Basis der Aufgabenstellung, Zusatzinformationen und des Beispiels.\n"
            "Simulieren Sie den Ablauf der Turingmaschine vorab, um die effizienteste und logischste Lösung zu identifizieren.\n"
            "Die Tabelle muss alle möglichen Eingaben korrekt verarbeiten, die Zielsetzung der Aufgabe erfüllen und vollständig, fehlerfrei sowie effizient gestaltet sein.\n\n"
        )

    @staticmethod
    def get_state_transition_table_quality_prompt():
        return (
            "## Überprüfung und Validierung der Zustandsübergangstabelle:\n"
            "Stellen Sie sicher, dass die Zustandsübergangstabelle vollständig, korrekt und konsistent ist. Gehen Sie dabei die folgenden Punkte durch:\n\n"

            "### Aufgabenbezogene Überprüfung:\n"
            "- Stimmen die Zustände und Übergänge mit der Aufgabenstellung, den Zusatzinformationen und dem Beispiel überein?\n"
            "- Wurden alle relevanten Anforderungen der Aufgabenstellung korrekt berücksichtigt?\n\n"

            "### Technische Überprüfung:\n"
            "- **Spaltenstruktur:** Sind alle Spalten (Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand) korrekt und vollständig?\n"
            "- **Vollständigkeit:** Sind alle möglichen Zustände und Übergänge abgedeckt, einschließlich Sonderzeichen wie Leerzeichen `■`?\n"
            "- **Logik und Effizienz:** Ist die Abfolge der Zustände logisch und effizient?\n"
            "- **Kopfbewegung:** Sind die Bewegungen des Lesekopfes präzise und entsprechend der Aufgabenstellung definiert?\n\n"
            
            "### Überprüfung mit Testeingaben:\n"
            "- Validieren Sie die Zustandsübergangstabelle mit mehreren Testeingaben, um sicherzustellen, dass sie für verschiedene Szenarien korrekte Ergebnisse liefert.\n"
            "- Stellen Sie sicher, dass alle möglichen Ergebnisse der Aufgabenstellung korrekt und wie vorgesehen erreicht werden.\n\n"

            "### Abschließende Validierung:\n"
            "- Überprüfen Sie, ob die Tabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Stellen Sie sicher, dass keine logischen Widersprüche oder Fehler vorhanden sind.\n\n"

            "### Fehlerkorrektur:\n"
            "Falls Fehler oder Unstimmigkeiten auftreten, verbessern Sie die Tabelle entsprechend!\n\n"
        )

    # example_flow_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_all_example_flow_table_prompt(task_parts):
        return (
                PromptBuilder.get_example_flow_table_requirements_prompt() +
                PromptBuilder.get_example_flow_table_request_prompt(task_parts)
                # PromptBuilder.get_example_flow_table_quality_prompt()
        )

    @staticmethod
    def get_example_flow_table_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das auf Basis der Aufgabenstellung, der Zusatzinformationen, des Beispiels und der Zustandsübergangstabelle "
            "eine Beispielablauftabelle für eine Turingmaschine erstellt. Dein Ziel ist es, fehlerfreie, konsistente und qualitativ hochwertige Tabellen zu erstellen, "
            "die alle Bewegungen und Zustandsübergänge der Turingmaschine korrekt darstellen.\n\n"
            "Halte dich an alle folgenden Anforderungen und überprüfe gründlich, dass die Tabelle mit der Aufgabenstellung und der Zustandsübergangstabelle übereinstimmt.\n\n"
        )

    @staticmethod
    def get_example_flow_table_requirements_prompt():
        return (
            "## Anforderungen an die Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle, dem Beispiel, sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Kopfposition:** Geben Sie die Kopfposition ausschließlich als numerischen Wert der aktuellen Position des Lesekopfes an.\n"
            "  ⦁ Die Nummerierung beginnt immer bei **1** und wird bei jedem Schritt der Turingmaschine fortlaufend aktualisiert.\n"
            "  ⦁ Falls der Lesekopf das linke Ende des sichtbaren Bandbereichs überschreitet, setzen Sie die Nummerierung negativ fort, beginnend mit **0**, **-1**, **-2**, und so weiter. Dadurch wird jede Bewegung des Lesekopfes lückenlos dokumentiert.\n"
            "  ⦁ Die Kopfposition muss für jeden Schritt eindeutig angegeben werden, sodass der gesamte Ablauf der Turingmaschine präzise und nachvollziehbar bleibt.\n\n"
            
            "- **Bandinhalt:** Der Bandinhalt muss vollständig angezeigt werden, einschließlich der Begrenzungsleerzeichen (`■`) links und rechts der Eingabe. Markieren Sie die aktive Kopfposition durch eine Umrahmung `[ ]` (z. B. `■11[0]1■`).\n"
            "- **Anwendung der Übergangsregeln:** Setzen Sie die Übergangsregeln korrekt um, indem der Bandinhalt bei jedem Schreibvorgang aktualisiert und die Kopfbewegung dokumentiert wird.\n\n"

            "## Schrittweise Validierung:**\n"
            "  - Validieren Sie nach jedem erstellten Schritt, ob dieser mit der Zustandsübergangstabelle übereinstimmt.\n"
            "  - Überprüfen Sie, ob Anpassungen oder Korrekturen erforderlich sind, und übertragen Sie diese in die Tabelle, bevor der nächste Schritt erstellt wird.\n"
            "- **Vollständigkeit:** Die Tabelle darf keine Lücken enthalten und muss alle Zustandsänderungen sowie Kopfbewegungen abbilden.\n\n"

            "- **Übergangsregeln:**\n"
            "  ⦁ Setzen Sie die Übergangsregeln korrekt um und validieren Sie nach jedem Schritt, ob die aktuellen Änderungen (Zustand, Bandinhalt, Kopfposition) mit der Zustandsübergangstabelle übereinstimmen.\n"
            "  ⦁ Überprüfen Sie jede Zeile einzeln, um sicherzustellen, dass keine Abweichungen oder Fehler auftreten. Falls Anpassungen erforderlich sind, korrigieren Sie diese konsequent.\n\n"
            
            "- **Vollständigkeit:** Die Tabelle muss alle relevanten Zustandsänderungen, Kopfbewegungen und Übergänge dokumentieren, die erforderlich sind, um die Eingabe korrekt zu verarbeiten.\n\n"
        )

    @staticmethod
    def get_example_flow_table_request_prompt(task_parts):
        return (
            f"Aufgabenstellung und Zustandsübergangstabelle: {task_parts}\n\n"
            
            "Erstellen Sie die Beispielablauftabelle basierend auf der Aufgabenstellung, den Zusatzinformationen, dem Beispiel und der Zustandsübergangstabelle.\n"
            "Validieren Sie nach jedem erstellten Schritt, ob die Zeile korrekt ist und die Übergangsregeln eingehalten wurden.\n"
            "Nehmen Sie notwendige Anpassungen vor, bevor Sie den nächsten Schritt erstellen.\n\n"
        )

    @staticmethod
    def get_example_flow_table_quality_prompt():
        return (
            "## Überprüfung und Validierung der Beispielablauftabelle:\n"
            "Stellen Sie sicher, dass die Beispielablauftabelle vollständig, korrekt und konsistent ist. Gehen Sie dabei die folgenden Punkte durch:\n\n"

            "### Aufgabenbezogene Überprüfung:\n"
            "- Entspricht die Tabelle den Anforderungen der Aufgabenstellung, den Zusatzinformationen und dem Beispiel?\n"
            "- Ist die Tabelle konsistent mit der Zustandsübergangstabelle und sind alle relevanten Übergänge, Bewegungen und Zustandsänderungen dokumentiert?\n\n"

            "### Technische Überprüfung:\n"
            "- **Spaltenstruktur:** Sind alle Spalten korrekt und vollständig (Schritt, Aktueller Zustand, Bandinhalt, Kopfposition)?\n"
            "- **Kopfposition:** Ist die Kopfposition korrekt nummeriert und mit der tatsächlichen Position des Lesekopfes synchron?\n"
            "- **Bandinhalt:** Ist der Bandinhalt in jedem Schritt korrekt aktualisiert und die aktive Kopfposition durch `[ ]` markiert?\n"
            "- **Übergangsregeln:** Wurden alle Übergangsregeln korrekt umgesetzt und dokumentiert?\n"
            "- **Vollständigkeit:** Sind alle Zustandsänderungen und Kopfbewegungen vollständig dokumentiert?\n\n"

             "### Validierung des Ablaufs:\n"
             "- Überprüfen Sie, ob der Ablauf exakt mit den Vorgaben der Aufgabenstellung, des Beispiels und der Zustandsübergangstabelle übereinstimmt.\n"
             "- Validieren Sie, dass das erwartete Ergebnis des Beispiels (Ausgabe) korrekt erreicht wird.\n\n"

            "### Abschließende Validierung:\n"
            "- Überprüfen Sie, ob die Tabelle den höchsten Qualitätsstandards entspricht und für Prüfungszwecke geeignet ist.\n"
            "- Stellen Sie sicher, dass keine logischen Widersprüche oder Fehler vorhanden sind.\n\n"

            "### Fehlerkorrektur:\n"
            "Falls Fehler oder Unstimmigkeiten auftreten, verbessern Sie die Tabelle entsprechend!\n\n"
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

            "### Aufgabenbezogene Überprüfung:\n"
            "- Ist die konzeptionelle Beschreibung des Lösungsansatzes klar und nachvollziehbar?\n"
            "- Stimmen die zusätzlichen Informationen mit der Aufgabenstellung und den anderen Elementen wie der Zustandsübergangstabelle überein?\n"
            "- Ist der Lösungsweg logisch aufgebaut, fehlerfrei und vollständig beschrieben?\n\n"

            "### Abschließende Validierung:\n"
            "- Entspricht die gesamte Lösung den höchsten Qualitätsstandards und ist sie für Prüfungszwecke geeignet?\n"
            "- Sind alle Abschnitte der Lösung konsistent und frei von logischen Widersprüchen?\n\n"

            "### Fehlerkorrektur:\n"
            "Falls Fehler oder Unstimmigkeiten auftreten, verbessern Sie die Lösung entsprechend und validieren Sie diese erneut.\n\n"
        )