from Const import *


class PromptBuilder:

    # Schwierigkeitsstufen ---------------------------------------------------------------------------------------------

    DIFFICULTY_EXPLANATION_MAP = {

        DIFFICULTY_EASY:
            (
                "Aufgaben auf diesem Niveau sollen sich auf die grundlegendsten Mechanismen von Turingmaschinen beschränken.\n"
                "- Es dürfen keine Schleifen oder komplexe Logik enthalten sein.\n"
                "- Die Aufgaben müssen mit einer kleinen Anzahl an Zuständen lösbar sein.\n"
                "- Die Bandbewegung darf sich nur in eine Richtung vollziehen (kein Wechsel der Bewegungsrichtung).\n"
                "- Keine zusätzlichen logischen Operationen wie Überträge oder Berechnungen sind erlaubt.\n"
                "- Ziel ist es, einfache Konzepte wie das Schreiben und Lesen von Zeichen oder Bewegen des Kopfes in eine Richtung zu verdeutlichen.\n"
                "- Vermeide Eingaben, die nur aus einem Symbol bestehen.\n"
                "- Validieren Sie, dass die Aufgaben so einfach wie möglich gestaltet sind und der Zielgruppe von Einsteigern entsprechen.\n"
                "**Prüfen Sie sorgfältig, ob die Aufgabe den Kriterien entspricht, bevor Sie fortfahren.**\n\n"
            ),

        DIFFICULTY_MEDIUM:
            (
                "Aufgaben auf diesem Niveau sollen das Verständnis der grundlegenden Konzepte der Turingmaschine vertiefen und moderate Herausforderungen einführen.\n"
                "- Die Aufgaben können einfache Verzweigungen und Schleifen beinhalten, die logisch und klar strukturiert sind.\n"
                "- Zustandsübergänge bleiben überschaubar und klar nachvollziehbar, wobei unnötige Komplexität vermieden wird.\n"
                "- Der Bandkopf kann sich in beide Richtungen bewegen.\n"
                "- Alle Übergänge müssen klar definiert und auf wenige, eng miteinander verknüpfte Zustände begrenzt sein.\n"
                "- Das Ziel ist es, die Fähigkeit der Studierenden zu fördern, einfache Logiken und Bedingungen korrekt umzusetzen, ohne sie zu überfordern.\n"
                "**Prüfen Sie sorgfältig, ob die Aufgabe wirklich nur moderate Herausforderungen bietet und die Komplexität nicht unnötig gesteigert wird!**\n\n"
            ),

        DIFFICULTY_HARD:
            (
                "Aufgaben auf diesem Niveau sollen anspruchsvolle Szenarien darstellen, die ein tiefgehendes Verständnis der Turingmaschine und hohe Problemlösefähigkeiten erfordern.\n"
                "- Die Zustandsübergänge sind komplex und können mehrere Bedingungen, verschachtelte Schleifen sowie dynamische Richtungswechsel umfassen.\n"
                "- Die Aufgaben können längere Sequenzen mit mehreren Zwischenzielen und Zustandsgruppen umfassen, die zur Lösung erforderlich sind.\n"
                "- Der Fokus liegt auf strategischem Denken, indem die Teilnehmenden vielschichtige Abläufe analysieren und effizient umsetzen müssen.\n"
                "- Es müssen Grenzfälle und Sonderbedingungen berücksichtigt werden, um die Funktion der Maschine in allen Szenarien sicherzustellen.\n"
                "- Das Ziel ist es, Aufgaben zu erstellen, die die Herausforderungen der Turingmaschine demonstrieren und die Studierenden an die Grenzen ihres Verständnisses bringen.\n"
                "**Vergewissern Sie sich, dass die Aufgabe wirklich anspruchsvoll ist und die Komplexität angemessen erhöht wurde, ohne unlösbar zu sein.**\n\n"
            )

    }

    # task_message -----------------------------------------------------------------------------------------------------

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
        difficulty_explanation = PromptBuilder.DIFFICULTY_EXPLANATION_MAP.get(difficulty_eng)

        return (
            "# Ziel der Aufgabe:\n\n"

            f"Generieren Sie genau **{num_questions}** Prüfungsaufgaben zu Turingmaschinen.\n\n"

            f"### Zielgruppe und Anforderungen:\n"
            f"Die Aufgaben sind speziell für Informatik-Studierende an Universitäten gedacht. "
            f"Sie sollen deren Verständnis und Anwendungskompetenz überprüfen und für Prüfungen geeignet sein.\n\n"

            f"### Schwierigkeitsgrad:\n"
            f"Die Aufgaben müssen dem Schwierigkeitsgrad '**{difficulty}**' entsprechen!\n"
            f"Anforderungen: {difficulty_explanation}\n\n"
            "Achten Sie unbedingt darauf, dass der Schwierigkeitsgrad eingehalten wird!\n"

            "### Vielfältigkeit der Aufgaben:\n"
            "- Die generierten Aufgaben sollen unterschiedliche Aspekte und Funktionen von Turingmaschinen abdecken.\n"
            "- Vermeiden Sie Wiederholungen oder ähnliche Aufgabenstellungen innerhalb eines Aufgaben-Sets.\n"
            "- Achten Sie darauf, dass die Aufgaben abwechslungsreich sind und verschiedene Konzepte abdecken.\n\n"
        )

    @staticmethod
    def get_incorrect_task_prompt(difficulty_eng):
        difficulty = DIFFICULTY_TRANSLATION_MAP.get(difficulty_eng)

        return (
            "# Zusätzliche Informationen zum Auftrag:\n\n"

            f"Erstellen Sie Aufgaben mit absichtlich fehlerhaften Turingmaschinen, die dem Schwierigkeitsnivea '**{difficulty}**' entsprechen. Ziel ist es, das Fehlersuch- und "
            "Korrekturvermögen der Studierenden gezielt zu fördern, ohne dass die gesamte Tabelle fehlerhaft oder unverständlich wird. (Nutze eine Tabelle um die fehlerhafte Turingmaschine darzustellen!)\n\n"

            "## Anforderungen an die Fehlerstruktur:\n"
            "- Die Turingmaschine soll einen oder mehrere spezifische Fehler enthalten, die das gewünschte Ergebnis verhindern oder zu einem falschen Output führen "
            "(**Gebe auch explizit in der Aufgabenstellung an, dass Fehler enthalten sind!**).\n"
            "- **Alle anderen Übergänge und Zustände müssen korrekt sein** und den Anforderungen der Aufgabenstellung entsprechen, damit die Tabelle eine funktionierende Basis hat.\n"
            "- Fehler dürfen nicht zufällig eingefügt werden, sondern müssen gezielt platziert werden, sodass sie logisch nachvollziehbar sind und eine sorgfältige Analyse erfordern.\n"
            "- Fehler können auftreten in:\n"
            "   ⦁ **Zustandsübergängen**\n"
            "   ⦁ **Lese- oder Schreibaktionen** (z. B. falsches Schreib und/oder Lese-Symbol)\n"
            "   ⦁ **Bandbewegungen** (z. B. falsche Bewegungsrichtung des Kopfes)\n"
           "    ⦁ **Zustände** (z. B. zusätzliche oder fehlende Zustände)\n\n"

            "## Anforderungen an die Tabelle:\n"
            "- **Korrektheit der Basis:** Alle Zustände und Übergänge, die keinen beabsichtigten Fehler enthalten, müssen korrekt und mit der Aufgabenstellung konsistent sein.\n"
            "- **Vollständigkeit:** Alle relevanten Informationen aus der Aufgabenstellung und den Zusatzinformationen müssen in der Tabelle korrekt berücksichtigt werden (inkl Bewegungsrichtung und Start- sowie Endzustand).\n"
            "- **Fehlergestaltung:** Fehler müssen subtil genug sein, um eine angemessene Herausforderung zu bieten, aber dennoch logisch nachvollziehbar bleiben.\n"
            "- **Formatierung:** Die Tabelle muss klar und präzise strukturiert sein. Alle Spalten und Zeilen (Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand) müssen vollständig und korrekt formatiert sein.\n\n"

            "## Hinweise für die Erstellung:\n"
            "- Führen Sie vor der Generierung der fehlerhaften Tabelle eine vollständige Simulation der Aufgabe durch, um sicherzustellen, dass die Basis korrekt ist.\n"
            "- Erstellen Sie daraufhin zuerst eine fehlerfreie Tabelle und füge erst danach Fehler ein, um sicherzustellen, dass die Tabelle grundsätzlich richtig funktioniert!\n"
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
            "- **Start- und Endposition:** Definieren Sie klar, wo der Lese-/Schreibkopf startet und endet. Die Startposition des Kopfes soll immer so gewählt werden, dass die Aufgabe effizient und logisch gelöst werden kann. "
            "Die Endposition muss auch logisch zur Abfolge passen und präzise ohne unnötige Informationen angegeben werden!\n"
            "  ⦁ Falls die Aufgabe so aufgebaut ist, dass sie in eine Bewegungsrichtung abgeschlossen werden kann, wählen Sie die Startposition entsprechend, um unnötige Bewegungen des Lesekopfes zu vermeiden.\n"
            "  ⦁ Simulieren Sie den Ablauf der Aufgabe basierend auf der Aufgabenstellung, den Zusatzinformationen und der Zielsetzung der Aufgabe. Bestimmen Sie daraufhin die logisch günstigste Startposition des Lese-/Schreibkopfs.\n"
            "  ⦁ Stellen Sie sicher, dass die gewählte Startposition konsistent mit der Zustandsübergangstabelle und dem Beispiel ist.\n"
            "  ⦁ Vermeiden Sie Widersprüche oder ineffiziente Startpositionen, die den Ablauf der Aufgabe unnötig komplizieren oder das Ziel der Aufgabe gefährden könnten.\n"
            "  ⦁ Die gilt auch für die Endposition!\n\n"

            "## Spezifische Anforderungen an das Beispiel ('example'):\n"
            "- **Sinnvolles Beispiel:** Wählen Sie ein Beispiel, das die Anforderungen der Aufgabenstellung klar und korrekt veranschaulicht.\n"
            "- **Eindeutigkeit:** Stellen Sie sicher, dass das Beispiel den Ablauf und das Ergebnis der Aufgabe korrekt widerspiegelt und die Funktion der Aufgabe am besten veranschaulicht. Vermeiden Sie widersprüchliche Darstellungen, die von der Aufgabenbeschreibung oder Lösung abweichen.\n"
            "- **Korrekte Darstellung:** Stellen Sie sicher, dass die Eingabe und der erwartete Output korrekt sind, einschließlich Leerzeichen-Symbole `■` am Anfang und Ende.\n"
            "- **Leerzeichen** Wenn Leerzeichen als Trennungszeichen genutzt werden ist dies auch mit dem Symbol `■` darzustellen.\n\n"
            "- **Formatierung des Beispiels:** Das Beispiel muss immer im folgenden Format angegeben werden: `Eingabe: <Wert> | Ausgabe: <Wert>`.\n\n"
             # (Falls der Bandinhalt gleich bleibt und der Inhalt )

            "**Füge KEINE Tabellen (optional_question_tables) hinzu, außer es ist ausdrücklich verlangt!**\n\n"
        )

    @staticmethod
    def get_task_request_prompt(num_questions):
        return (
            f"Erstellen Sie die **{num_questions}** Aufgabenstellungen und jeweils ein passendes Beispiel.\n"
            "Stellen Sie sicher, dass alle Inhalte vollständig, präzise und fehlerfrei sind.\n\n"
        )

    @staticmethod
    def get_shared_info_text():
        return (
            "Falls die Inhalte direkt Aufgaben zu Turingmaschinen darstellen, dürfen diese nicht wörtlich übernommen werden. "
            "Nutzen Sie die Inhalte als Orientierung, um eigene Aufgaben zu erstellen.\n\n"
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
    def get_state_transition_table_system_context_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das eine Zustandsübergangstabelle für eine gegebene Turingmaschine erstellt."
            "Dein Ziel ist es, eine Tabelle zu generieren, die die Anforderungen der Aufgabenstellung, der Zusatzinformationen "
            "und des Beispiels vollständig und effizient umsetzt. Die Tabelle muss den höchsten akademischen Standards entsprechen "
            "und für alle möglichen Eingaben die korrekten Ergebnisse liefern.\n\n"
        )

    @staticmethod
    def get_state_transition_table_system_requirements_prompt():
        return (
            "# Richtlinien für die Zustandsübergangstabelle ('solution_state_transition_table'):\n\n"

            "### Analyse der Aufgabenstellung:\n"
            "- Verstehen Sie die Anforderungen und Zielsetzung der Aufgabe vollständig, einschließlich der Start- und Endposition.\n"
            "- Beachten Sie: Wenn in der Aufgabenstellung steht, dass der Kopf auf dem ersten oder letzten Symbol der Eingabe startet, ist damit das **erste tatsächliche Symbol** der Eingabe gemeint und **kein Leerzeichen**, es sei denn, es ist explizit angegeben.\n"
            "- Simulieren Sie den Ablauf der Turingmaschine intern mit verschiedenen Eingaben, um die effizienteste Lösung zu finden.\n\n"

            "### Konsistenz zwischen Aufgabenstellung und Lösung:\n"
            "- Die Tabelle muss die Zielsetzung der Aufgabe präzise und effizient umsetzen.\n"
            "- Stellen Sie sicher, dass alle Zustände und Übergänge exakt den Vorgaben der Aufgabenstellung und Zusatzinformationen entsprechen.\n"
            "- Erstelle die Tabelle so, dass sie mit der START- und END-Position der Aufgabenstellung konsistent ist! Achte auch auf eine präzise Rückführung in die Endpostition falls genauer bechrieben!\n"
            "- Jeder Übergang und jede Zustandsänderung muss darauf ausgelegt sein, das spezifizierte Ziel der Aufgabe zu erreichen.\n"
            "- Vermeiden Sie Annahmen oder Ergänzungen, die nicht explizit in der Aufgabenstellung beschrieben sind.\n\n"

            "### Struktur und Vollständigkeit:\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Aktueller Zustand, Gelesenes Zeichen, Neues Zeichen, Bewegung, Neuer Zustand.\n"
            "- **Vollständigkeit:** Alle möglichen Zustände, einschließlich Start- und Endzustände, sowie alle Übergänge müssen abgedeckt sein. Sonderzeichen wie Leerzeichen `■` sind einzubeziehen.\n"
            "- **Eindeutigkeit:** Jeder Übergang muss klar definiert sein und es darf nicht vorkommen dass es pro Zustand zweimal das gleiche einzulesende Zeichen gibt (Fehler wie diese sind inakzeptabel!).\n"
            "- **Allgemeingültigkeit**: Die Zustandsübergangstabelle darf nicht nur auf das gegebene Beispiel zugeschnitten sein, sondern muss auch für anderen potenzielle Eingaben korrekt funktionieren, die gemäß der Aufgabenstellung erwartet werden.\n"
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
    def get_state_transition_table_system_process_prompt():
        return (
            "# Prozessübersicht:\n"
            "1. **Aufgabenstellung:**\n"
            "   Zunächst erhältst du die vollständige Aufgabenstellung, auf deren Basis du die Zustandsübergangstabelle erstellen sollst. Anaylsiere diese bis du die Anforderungen genau verstanden hast!\n\n"
            "2. **Generierung der Tabelle:**\n"
            "   Erstelle die Zustandsübergangstabelle basierend auf der erhaltenen Aufgabenstellung und den spezifischen Anforderungen.\n\n"
            "3. **Korrektur und Validierung:**\n"
            "   Nach der Generierung überprüfst du die Tabelle auf Fehler oder Unstimmigkeiten und nimmst, falls erforderlich, Korrekturen vor, um eine fehlerfreie und konsistente Tabelle zu gewährleisten.\n\n"
        )

    @staticmethod
    def get_state_transition_table_request_prompt():
        return (
            "**Erstelle eine vollständige und präzise Zustandsübergangstabelle, die die Aufgabenstellung effizient und korrekt umsetzt!!!**\n\n"

            "[WICHTIG] Beachte Folgendes vor der Erstellung genau:\n"
            "  - Plane die benötigten Zustände so, dass sie die Funktion der Aufgabe vollständig abdecken, ohne redundante oder doppelte Zustände für das gleiche Szenario.\n"
            "  - Definiere die Übergänge klar und konsistent, sodass jeder Zustand nur einmal pro gelesenem Zeichen spezifiziert ist.\n"
            "  - Vermeide doppelte Zustände für das gleiche gelesene Zeichen.\n"
            "  - Stelle sicher, dass Start- und Endzustand korrekt nach der Aufgabenstellung definiert sind. Die Maschine muss am Ende an der spezifizierten Endposition stehen bleiben (Stelle dies auch in der Tabelle dar).\n"
            "  - **Beachte, dass die Rückführung der Bandposition zum gewünschten Endzustand (inkl. aller Zwischenschritte) zwingend korrekt und vollständig umgesetzt wird.**\n\n"
            # "  - Vermeide unnötige Komplexität um das Ziel zu erfüllen!\n\n"
            "  - Falls Überträge in der Aufgabe nötig sind, arbeite mit Hilfssymbolen!\n\n"

            "[WICHTIG] Zusätzlich:\n"
            "  - Überprüfe gedanklich die gesamte Tabelle Schritt für Schritt, um sicherzustellen, dass alle Übergänge und Grenzfälle korrekt berücksichtigt werden.\n"
            "  - Beachte, dass die Rückführung der Bandposition zum gewünschten Endzustand (inkl. aller Zwischenschritte) zwingend korrekt und vollständig umgesetzt wird.\n\n"
            "  - Teste gedanklich verschiedene Szenarien, um sicherzustellen, dass die Tabelle für alle möglichen Eingaben korrekt funktioniert.\n\n"

            "Stelle sicher, dass die Tabelle logisch aufgebaut, effizient und nachvollziehbar ist. Überprüfe alle Schritte vor Abschluss der Tabelle, "
            "um sicherzustellen, dass die Aufgabenstellung vollständig erfüllt wird und die Tabelle als Musterlösung dient.\n\n"
        )

    @staticmethod
    def get_state_transition_table_task_prompt(question_content):
        return (
            f"AUFGABENSTELLUNG: {question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"BEISPIEL: {question_content[SECTION_EXAMPLE]}\n\n"
        )

    # example_flow_table_message ----------------------------------------------------------------------------------

    @staticmethod
    def get_example_flow_table_system_context_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das eine Beispielablauftabelle für eine gegebene Turingmaschine erstellt!\n"
            "Dein Ziel ist es, auf Basis der Aufgabenstellung, der Zusatzinformationen, des Beispiels und der Zustandsübergangstabelle, "
            "eine fehlerfreie, konsistente und qualitativ hochwertige Tabelle zu erstellen.\n"
            "Die Tabelle muss den höchsten akademischen Standards entsprechen und für das gegebene Beispiel, den fehlerfreien Ablauf aufzeigen.\n\n"
        )

    @staticmethod
    def get_example_flow_table_system_requirements_prompt():
        return (
            "## Anforderungen an die Beispielablauftabelle ('solution_example_flow_table'):\n"
            "- **Konsistenz:** Die Tabelle muss den Ablauf der Turingmaschine genau widerspiegeln und mit der Zustandsübergangstabelle, dem Beispiel, sowie der Aufgabenstellung übereinstimmen.\n"
            "- **Spaltenstruktur:** Die Tabelle muss folgende Spalten enthalten: Schritt, Aktueller Zustand, Bandinhalt, Kopfposition.\n"
            "- **Start- Endposition** Die Start- und Endposition muss korrekt und konsistent mit den Angaben in der Aufgabenstellung sein. (Der Start erfolgt immer an einer Randposition der Eingabe!)\n"

            "- **Kopfposition:** Geben Sie die Kopfposition ausschließlich als numerischen Wert der aktuellen Position des Lesekopfes an.\n"
            "  ⦁ Die Nummerierung beginnt immer bei **1** und wird bei jedem Schritt der Turingmaschine fortlaufend aktualisiert.\n"
            "  ⦁ Falls der Lesekopf das linke Ende des sichtbaren Bandbereichs überschreitet, setzen Sie die Nummerierung negativ fort, beginnend mit **0**, **-1**, **-2**, und so weiter. Dadurch wird jede Bewegung des Lesekopfes lückenlos dokumentiert.\n"
            "  ⦁ Die Kopfposition muss für jeden Schritt eindeutig angegeben werden, sodass der gesamte Ablauf der Turingmaschine präzise und nachvollziehbar bleibt.\n"

            "- **Bandinhalt:** Der Bandinhalt muss vollständig angezeigt werden, einschließlich der Begrenzungsleerzeichen (`■`) links und rechts der Eingabe. Markieren Sie die aktive Kopfposition durch eine Umrahmung `[ ]` (z. B. `■11[0]1■`).\n"
            "- **Anwendung der Übergangsregeln:** Setzen Sie die Übergangsregeln korrekt um, indem der Bandinhalt bei jedem Schreibvorgang aktualisiert und die Kopfbewegung dokumentiert wird.\n"
            "  ⦁ Prüfe den aktuellen Zustand und das Zeichen unter dem Lesekopf, schreibe das neue Zeichen, führe die Bewegung gemäß der Anweisung aus und wechsle in den nächsten Zustand laut der Zustandstabelle.\n"
            "  ⦁ Der Bandinhalt muss immer auf dem vorherigen Inhalt aufbauen!\n"
            "  ⦁ Beachten Sie, dass Richtungswechsel des Lesekopfes nicht nur am Bandende, sondern auch an beliebigen Positionen auf dem Band stattfinden können.\n"

            "- **Vollständigkeit:** Die Tabelle muss alle relevanten Zustandsänderungen, Kopfbewegungen und Übergänge dokumentieren, die erforderlich sind, um die Eingabe korrekt zu verarbeiten.\n"

            "- **Relevanz der Zustandsübergangstabelle:**\n"
            "  ⦁ Verwenden Sie nur die Zustände und Übergänge der Zustandsübergangstabelle, die für das Beispiel relevant sind.\n"
            "  ⦁ Nicht alle Zustände der Tabelle sind notwendig, um das Beispiel vollständig zu dokumentieren. Stellen Sie sicher, dass nur die tatsächlich verwendeten Zustände und Übergänge in der Beispielablauftabelle enthalten sind.\n"
            "  ⦁ Beachten Sie, dass der Endzustand je nach Beispiel unterschiedlich schnell erreicht werden kann. Dokumentieren Sie den Ablauf bis zum Abschluss des Beispiels, auch wenn dies nur wenige Schritte oder viele Schritte je nach Beispiel erfordert!\n"

            "- **Übergangsregeln prüfen:**\n"
            "  ⦁ Setzen Sie die Übergangsregeln korrekt um und validieren Sie nach jedem Schritt, dass die aktuellen Änderungen (Zustand, Bandinhalt, Kopfposition) mit der Zustandsübergangstabelle übereinstimmen.\n"
            "  ⦁ Überprüfen Sie jede Zeile einzeln, um sicherzustellen, dass keine Abweichungen oder Fehler auftreten. Falls Anpassungen erforderlich sind, korrigieren Sie diese konsequent.\n\n"

            "## Schrittweise Validierung:**\n"
            "- Validieren Sie nach jedem erstellten Schritt, ob dieser mit der Zustandsübergangstabelle übereinstimmt.\n"
            "- Überprüfen Sie, ob Anpassungen oder Korrekturen erforderlich sind, und übertragen Sie diese in die Tabelle, bevor der nächste Schritt erstellt wird.\n"
        )

    @staticmethod
    def get_example_flow_table_system_process_prompt():
        return (
            "### Prozessübersicht:\n"
            "1. **Aufgabenstellung:**\n"
            "   Zunächst erhältst du die vollständige Aufgabenstellung und Zustandsübergangstabelle, auf deren Basis du die Beispielablauftabelle erstellen sollst. Anaylsiere diese bis du die Anforderungen genau verstanden hast!\n\n"
            "2. **Generierung der Tabelle:**\n"
            "   Erstelle die Beispielablauftabelle basierend auf der erhaltenen Aufgabenstellung, Zustandsübergangstabelle und den spezifischen Anforderungen.\n\n"
            "3. **Korrektur und Validierung:**\n"
            "   Nach der Generierung überprüfst du die Tabelle auf Fehler oder Unstimmigkeiten und nimmst, falls erforderlich, Korrekturen vor, um eine fehlerfreie und konsistente Tabelle zu gewährleisten.\n\n"
        )

    @staticmethod
    def get_example_flow_table_request_prompt():
        return (
            "**Erstellen Sie eine korrekte und allumfassende Beispielablauftabelle auf Basis der Zustandsübergangstabelle, Aufgabenstellung, Zusatzinformationen und des Beispiels!**\n\n"
            
            "[WICHTIG] Beachten Sie Folgendes bei der Erstellung:\n"
            "  - Jede Bandänderung muss exakt der in der Zustandsübergangstabelle definierten Operation entsprechen! Wende jede Regel des Zustands konsequent an!\n"
            "  - Überprüfen Sie für jeden Schritt, dass das richtige Zeichen am richtigen Ort geschrieben wird und der Kopf gemäß den Vorgaben der Tabelle verschoben wird (Alle Änderungen am Band müssen klar und vollständig dokumentiert werden).\n"
            "  - Das Zeichen muss in jedem Schritt mit dem neuem Zeichen überschrieben werden, auch wenn es sich um das gleiche Zeichen handelt\n"
            "  - Der Lese-/Schreibkopf muss immer auf der definierten Startposition beginnen und am Ende der Operation korrekt im gewünschten Endzustand stehen.\n"
            "  - Achten Sie darauf, dass keine unlogischen oder redundanten Operationen stattfinden (z. B. doppelte Änderungen an derselben Bandposition).\n\n"
            
            "Stellen Sie sicher, dass die Beispielablauftabelle logisch aufgebaut, vollständig und konsistent mit allen Vorgaben ist.\n\n"
        )

    @staticmethod
    def get_example_flow_table_task_prompt(question_content, state_transition_table_content):
        return (
            f"AUFGABENSTELLUNG: {question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"BEISPIEL: {question_content[SECTION_EXAMPLE]}\n\n"
            f"ZUSTANDSÜBERGANGSTABELLE: {state_transition_table_content[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"
        )

    # solution_message ----------------------------------------------------------------------------------

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
    def get_solution_task_prompt(question_content, state_transition_table_content, example_flow_table_content):
        return (
            f"AUFGABENSTELLUNG:\n\n{question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"BEISPIEL:\n\n{question_content[SECTION_EXAMPLE]}\n\n"
            f"ZUSTANDSÜBERGANGSTABELLE\n\n{state_transition_table_content[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"
            f"BEISPIELABLAUFTABELLE\n\n{example_flow_table_content[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]}\n\n"
        )

    @staticmethod
    def get_solution_request_prompt():
        return (
            "Erstellten Sie den rest der Lösung (solution, optional_solution_additional_infos, "
            "optional_solution_step_by_step) wie angegeben auf Basis der übergebenen Inhalte und baue die Aufgabe "
            "im übergebenen Format ExamQuestion wieder zusammen!\n\n"
        )
