from Const import SECTION_QUESTION_CONTENT, SECTION_EXAMPLE, SECTION_SOLUTION_STATE_TRANSITION_TABLE, \
    SECTION_SOLUTION_EXAMPLE_FLOW_TABLE


class ValidationPromptBuilder:

    # @staticmethod
    # def get_validation_system_prompt_state_transition_table():
    #     return (
    #         "Du bist ein spezialisiertes KI-Modell, das Zustandsübergangstabellen für Turingmaschinen korrigiert und optimiert.\n"
    #         "Dein Ziel ist es, die gegebene Zustandsübergangstabelle vollständig fehlerfrei, konsistent und effizient zu machen, "
    #         "sodass sie exakt die Anforderungen der Aufgabenstellung, der Zusatzinformationen und des Beispiels erfüllt.\n\n"
    #
    #         "Vorgehensweise:\n\n"
    #         "- **Analyse der Aufgabe:** Lies die Aufgabenstellung ('question'), Zusatzinformationen ('optional_question_additional_infos') und das Beispiel ('example') sorgfältig. "
    #         "Identifiziere alle Anforderungen und die Zielsetzung, die die Turingmaschine erfüllen muss.\n"
    #         "- **Analyse der Tabelle:** Untersuche die gegebene Zustandsübergangstabelle (`solution_state_transition_table`) und finde alle Fehler oder Unstimmigkeiten.\n"
    #         "- **Korrektur und Optimierung:** Korrigiere die Tabelle, sodass sie fehlerfrei, vollständig und effizient ist.\n"
    #         "- **Simulation:** Prüfe, ob die Tabelle alle möglichen Eingaben korrekt verarbeitet und das Ziel der Aufgabe erreicht.\n\n"
    #
    #         "Stelle sicher, dass die korrigierte Tabelle perfekt zur Aufgabenstellung passt und als Musterlösung dient.\n"
    #     )

    @staticmethod
    def get_validation_system_prompt_state_transition_table():
        return (
            "Du bist ein spezialisiertes Modell, das Zustandsübergangstabellen für Turingmaschinen korrigiert.\n"
            "Dein Ziel ist es, die Tabelle fehlerfrei und konsistent mit der Aufgabenstellung und Zusatzinformationen zu machen.\n"
        )

    @staticmethod
    def get_validation_user_prompt_state_transition_tableee(task_parts):
        return (
            "Korrigiere die Zustandsübergangstabelle basierend auf der gesamten Aufgabenstellung:\n"
            "- Alle Zustände und Übergänge müssen korrekt sein.\n"
            "- Die Tabelle muss alle möglichen Eingaben verarbeiten können.\n"
            "- Start- und Endzustände müssen erreichbar sein.\n"
            "- Keine unnötigen Zustände oder Übergänge.\n\n"

            "Wenn das Ziel der Aufgabe auch deutlich leichter erreicht werden kann erstelle eine neue passendere Zustandsübergangstabelle!"

            f"{task_parts}\n"
        )

    # @staticmethod
    # def get_validation_user_prompt_state_transition_table(task_parts):
    #     return (
    #         "### Anforderungen an die Korrektur:\n\n"
    #         "Korrigiere die Zustandsübergangstabelle (`solution_state_transition_table`) basierend auf den Anforderungen der Aufgabenstellung und des Beispiels.\n"
    #         "- Korrigiere, dass alle Zustände, Übergänge und Bandänderungen korrekt sind.\n"
    #         "- Stelle sicher, dass die Tabelle für alle möglichen Eingaben funktioniert, nicht nur für das Beispiel.\n"
    #         "- Überprüfe, ob der Endzustand vorhanden ist.\n"
    #         "- Vergewissere dich, dass die definierten Start- und Endzustände korrekt sind und erreicht werden können.\n"
    #         "- Optimiere die Tabelle, sodass sie effizient und leicht verständlich bleibt.\n"
    #         "- Überprüfe abschließend die Konsistenz mit der Aufgabenstellung und Zusatzinformationen.\n\n"
    #
    #         f"Der zu korrigierende solution_state_transition_table + Aufgabenstellung:\n\n {task_parts}\n\n"
    #     )

    @staticmethod
    def get_validation_user_prompt_state_transition_table(task_parts):
        return (
            # "### Korrektur:\n\n"
            # "Analysieren Sie zuerste die übergebene Aufgabenstellung inkl Beispiel und Zusatzinformationen.\n"
            # "Analysiere die gegebene Zustandsübergangstabelle und identifiziere Unstimmigkeiten und Fehler.\n\n"

            # "Korrigiere die Zustandsübergangstabelle (`solution_state_transition_table`) basierend auf den Anforderungen der Aufgabenstellung und des Beispiels.\n"
            # "- Stelle sicher, dass alle Zustände, Übergänge und Bandänderungen korrekt sind und keine Fehler enthalten.\n"
            # "- Vergewissere dich, dass die Start- und Endzustände gemäß der Aufgabenstellung korrekt definiert und erreichbar sind.\n"
            # "- Überprüfe, ob die Tabelle für **alle möglichen Eingaben** funktioniert, nicht nur für das gegebene Beispiel.\n"
            # "- Überprüfe, ob die Übergänge korrekt formuliert sind, z. B. wie der Lese-/Schreibkopf auf Leerzeichen (`■`) reagiert.\n\n"
            # "- Überprüfe, ob die Übergänge effizient gestaltet sind und nur die notwendigen Zustände und Übergänge enthalten.\n"
            # # "- Simuliere den Ablauf der Turingmaschine mit verschiedenen möglichen Eingaben, um die Korrektheit der Tabelle zu gewährleisten.\n"
            #
            # # f"**Aufgabe:**\n{task_parts}\n\n"
            #
            # f"Stellen Sie sicher, dass der Zustandsübergangstabelle nach den Anforderungen der Aufgabenstellung, der Zusatzinformationen und des Beispiels korrekt dargestellt wird!\n"
            # f"**Aufgabe:**\n{task_parts}\n\n"
            # "##Korrigiere die Zustandsübergangstabelle (`solution_state_transition_table`) basierend auf den Anforderungen der Aufgabenstellung ('question'), der Zusatzinformationen ('optional_question_additional_infos') und des Beispiels ('example').\n\n"
            #
            # "### Spezifische Anforderugen an Korrektur:\n\n"
            # "- **Start- und Endzustände:** Vergewissere dich, dass die definierten Start- und Endzustände korrekt definiert und erreichbar sind.\n"
            # "- **Übergänge:** Überprüfe, ob alle Übergänge logisch sind und den Anforderungen entsprechen. Achte darauf, dass keine unnötigen Zustände oder Übergänge hinzugefügt werden.\n"
            # "- **Titel**: Ändere NICHT den Namen der Tabelle sondern passe nur die Inhalte an."
            # "- **Korrektheit für alle Eingaben:** Stelle sicher, dass die Tabelle nicht nur das gegebene Beispiel, sondern auch alle möglichen Eingaben korrekt verarbeitet.\n"
            # "- **Effizienz:** Optimiere die Tabelle, indem nur notwendige Zustände und Übergänge enthalten sind.\n"
            # "- **Simulation:** Simuliere verschiedene mögliche Szenarien und Eingaben, um die Korrektheit und Effizienz der Tabelle zu überprüfen.\n\n"

            "Stelle sicher, dass die korrigierte Zustandsübergangstabelle perfekt zur Aufgabenstellung passt und keine Fehler sowie unnötige Zustände enthält.\n\n"
            f"### Zu korrigierende Aufgabe:\n{task_parts}\n"
        )

    @staticmethod
    def get_validation_user_prompt_state_transition_tablee(task_parts):
        return (
            f"Stellen Sie sicher, dass der Zustandsübergangstabelle nach den Anforderungen der Aufgabenstellung, der Zusatzinformationen und des Beispiels korrekt dargestellt wird!\n"
            f"**Aufgabe:**\n{task_parts}\n\n"
        )

    @staticmethod
    def get_validation_system_prompt_example_flow_table():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Beispielablauftabellen für Turingmaschinen korrigiert und validiert.\n"
            "Dein Ziel ist es, die gegebene Beispielablauftabelle vollständig fehlerfrei, konsistent und präzise zu machen.\n\n"

            # "Die Beispielablauftabelle muss:\n"
            # "- Exakt den Ablauf der Turingmaschine gemäß der Zustandsübergangstabelle und Aufgabenstellung darstellen.\n"
            # "- Jede Kopfbewegung, Bandänderung und den Zustand für jeden Schritt vollständig dokumentieren.\n"
            # "- Exakt an der in der Aufgabenstellung definierten Startposition beginnen und korrekt an der Endposition enden.\n\n"
            #
            # "Simuliere jeden Schritt der Tabelle, um sicherzustellen, dass keine Unstimmigkeiten oder Fehler vorhanden sind.\n"
        )

    # @staticmethod
    # def get_validation_user_prompt_example_flow_table(task_parts):
    #     return (
    #         "### Anforderungen an die Korrektur:\n\n"
    #         "Korrigiere die Beispielablauftabelle (`solution_example_flow_table`) basierend auf der korrigierten Zustandsübergangstabelle, der Aufgabenstellung und des Beispiels.\n"
    #         "- Korrigiere, dass jeder Schritt in der Tabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt (Bandänderung, Bewegungsrichtung, Kopfposition).\n"
    #         "- Korrigiere, dass die Bandänderungen und Kopfbewegungen in jedem Schritt korrekt und vollständig dokumentiert sind.\n"
    #         "- Stelle sicher, dass der Lese-/Schreibkopf an der in der Aufgabenstellung definierten Startposition beginnt und an der Endposition endet.\n"
    #         "- Simuliere den Ablauf der Turingmaschine anhand der Tabelle, um sicherzustellen, dass keine Unstimmigkeiten oder Fehler vorhanden sind.\n"
    #         "- Korrigiere die Tabelle so, dass sie korrekt ist und als perfekte Ergänzung zur Zustandsübergangstabelle und Musterlösung dient.\n\n"
    #
    #         f"Der zu korrigierende solution_example_flow_table + Aufgabenstellung und Zustandsübergangstabelle:\n\n {task_parts}\n\n"
    #     )
    @staticmethod
    def get_validation_user_prompt_example_flow_table(task_parts):
        return (
            "### Aufgabe zur Korrektur:\n\n"
            "Korrigiere die Beispielablauftabelle (`solution_example_flow_table`) basierend auf der korrigierten Zustandsübergangstabelle, der Aufgabenstellung und des Beispiels.\n"
            "- Überprüfe, ob jeder Schritt exakt mit der Zustandsübergangstabelle übereinstimmt.\n"
            "- Stelle sicher, dass jede Kopfbewegung, Bandänderung und Zustandsänderung präzise und nachvollziehbar dokumentiert ist.\n"
            "- Überprüfe, ob der Lese-/Schreibkopf an der in der Aufgabenstellung definierten Startposition beginnt und korrekt endet.\n"
            "- Simuliere den Ablauf der Turingmaschine anhand der Beispielablauftabelle, um sicherzustellen, dass keine Abweichungen oder Fehler vorhanden sind.\n"
            "- Überprüfe, ob die Bandänderungen den Zusatzinformationen entsprechen und korrekt dokumentiert sind.\n"
            "- Korrigiere die Tabelle so, dass sie präzise den Ablauf der Turingmaschine gemäß der Aufgabenstellung beschreibt und als perfekte Ergänzung zur Zustandsübergangstabelle dient.\n\n"
            # f"**Aufgabe:**\n{task_parts}\n\n"
        )

    @staticmethod
    def get_validation_user_prompt_example_flow_tablee(task_parts):
        return (
            f"Stellen Sie sicher, dass der Beispielablauftabelle nach den Anforderungen der Zustandsübergangstabelle, Aufgabenstellung, Zusatzinformationen und des Beispiels korrekt dargestellt wird!\n"
            f"**Aufgabe:**\n{task_parts}\n\n"
        )

    # @staticmethod
    # def get_validation_system_prompt_state_transition_table():
    #     return (
    #         "Du bist ein spezialisiertes KI-Modell, das Zustandsübergangstabellen für Turingmaschinen korrigiert und optimiert.\n"
    #         "Dein Ziel ist es, die gegebene Zustandsübergangstabelle vollständig fehlerfrei, konsistent und effizient zu machen, "
    #         "sodass sie exakt den Anforderungen der Aufgabenstellung entspricht und für alle möglichen Eingaben korrekt funktioniert.\n"
    #     )

    # @staticmethod
    # def get_validation_system_prompt_example_flow_table():
    #     return (
    #         "Du bist ein spezialisiertes KI-Modell, das Beispielablauftabellen für Turingmaschinen korrigiert und validiert.\n"
    #         "Dein Ziel ist es, die gegebene Beispielablauftabelle vollständig fehlerfrei, konsistent und präzise zu machen, "
    #         "sodass sie exakt den Ablauf der Turingmaschine gemäß der Zustandsübergangstabelle und Aufgabenstellung darstellt.\n"
    #     )

    # @staticmethod
    # def get_validation_user_prompt_example_flow_table(task_parts):
    #     return (
    #         "### Aufgabe zur Korrektur:\n\n"
    #         "Korrigiere die Beispielablauftabelle (`solution_example_flow_table`) basierend auf der korrigierten Zustandsübergangstabelle, der Aufgabenstellung und des Beispiels.\n"
    #         "- Überprüfe, ob jeder Schritt in der Tabelle exakt mit der Zustandsübergangstabelle übereinstimmt.\n"
    #         "- Stelle sicher, dass der Lese-/Schreibkopf an der in der Aufgabenstellung definierten Startposition beginnt und korrekt endet.\n"
    #         "- Überprüfe, ob die Bandänderungen in jedem Schritt korrekt sind und mit den Anforderungen der Aufgabenstellung übereinstimmen.\n"
    #         "- Korrigieren Sie, so dass die Tabelle vollständig konsistent ist und den Ablauf der Turingmaschine präzise beschreibt.\n\n"
    #         f"{task_parts}\n\n"
    #     )

    # -----------test------------------------------------
    # @staticmethod
    # def get_validation_system_prompt():
    #     return (
    #         "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen überprüft und korrigiert.\n"
    #         "Dein Ziel ist es, sicherzustellen, dass alle Bestandteile der Aufgabe (Aufgabenstellung, Zusatzinformationen, "
    #         "Beispiel, Zustandsübergangstabelle, Beispielablauftabelle und Lösung) logisch konsistent, fehlerfrei und vollständig sind.\n"
    #     )

    # @staticmethod
    # def get_validation_system_prompt():
    #     return (
    #         "Du bist ein spezialisiertes KI-Modell zur Korrektur von Turingmaschinen-Aufgaben.\n"
    #         "Deine Aufgabe ist es, die gesamte Prüfungsaufgabe zu überprüfen und sicherzustellen, dass sie konsistent, "
    #         "fehlerfrei und vollständig ist. Die Aufgabe besteht aus einer Aufgabenstellung, einer Zustandsübergangstabelle und "
    #         "einer Beispielablauftabelle und der Lösung.\n\n"
    #
    #         "Ziel ist es, die Tabellen so zu korrigieren, dass:\n"
    #         "- Die Zustandsübergangstabelle korrekt und effizient ist.\n"
    #         "- Die Beispielablauftabelle den Ablauf der Zustandsübergangstabelle exakt widerspiegelt.\n"
    #         "- Beide Tabellen exakt den Anforderungen der Aufgabenstellung entsprechen.\n"
    #     )

    @staticmethod
    def get_validation_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Aufgaben zur Turingmaschine validiert und verbessert. "
            "Dein Ziel ist es, die Zustandsübergangstabelle und die Beispielablauftabelle vollständig fehlerfrei, logisch konsistent "
            "und exakt entsprechend der Aufgabenstellung zu korrigieren. Beide Tabellen müssen miteinander übereinstimmen und den Ablauf "
            "der Turingmaschine präzise abbilden.\n\n"
        )

    # @staticmethod
    # def get_validation_user_prompt(task_parts):
    #     return (
    #         "### Analyse der Aufgabe:\n\n"
    #         "1. **Aufgabenstellung und Beispiel:**\n"
    #         "- Lesen und analysieren Sie die Aufgabenstellung und das gegebene Beispiel sorgfältig, um die Funktion der Turingmaschine vollständig zu verstehen.\n"
    #         "- Identifizieren Sie das Ziel der Aufgabe sowie alle relevanten Anforderungen und Bedingungen (z. B. Start- und Endzustände, Bandänderungen, Kopfbewegungen).\n"
    #         "- Achten Sie darauf, dass die Anforderungen der Aufgabenstellung klar und vollständig sind.\n\n"
    #         f"Aufgabenstellung:\n{task_parts[SECTION_QUESTION_CONTENT]}\n\n"
    #         f"Beispiel:\n{task_parts[SECTION_EXAMPLE]}\n\n"
    #
    #         "### Korrektur der Tabellen:\n\n"
    #         "2. **Zustandsübergangstabelle (`solution_state_transition_table`):**\n"
    #         "- Basierend auf der analysierten Aufgabenstellung und dem Beispiel korrigieren Sie die Zustandsübergangstabelle.\n"
    #         "- Stellen Sie sicher, dass alle Übergänge logisch, effizient und fehlerfrei sind.\n"
    #         "- Überprüfen Sie, ob die Tabelle alle möglichen Eingaben korrekt verarbeitet und nicht nur das gegebene Beispiel abdeckt.\n"
    #         "- Validieren Sie, dass die Start- und Endzustände korrekt definiert und erreichbar sind.\n"
    #         "- Achten Sie darauf, dass alle Bandänderungen die Anforderungen der Aufgabenstellung exakt erfüllen.\n\n"
    #         f"Zustandsübergangstabelle:\n{task_parts[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"
    #
    #         "3. **Beispielablauftabelle (`solution_example_flow_table`):**\n"
    #         "- Basierend auf der korrigierten Zustandsübergangstabelle und der analysierten Aufgabenstellung korrigieren Sie die Beispielablauftabelle.\n"
    #         "- Stellen Sie sicher, dass jeder Schritt der Tabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
    #         "- Überprüfen Sie, ob alle Kopfbewegungen, Bandänderungen und Zustände korrekt dokumentiert sind.\n"
    #         "- Validieren Sie, dass die Tabelle den Ablauf der Turingmaschine präzise beschreibt und die Start- und Endposition des Kopfes korrekt eingehalten wird.\n"
    #         "- Achten Sie darauf, dass die Bandänderungen und der Ablauf der Maschine fehlerfrei dokumentiert sind.\n\n"
    #         f"Beispielablauftabelle:\n{task_parts[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]}\n\n"
    #
    #         "### Zusammenfassung und Konsistenzprüfung:\n\n"
    #         "4. **Zusammenfassung und Konsistenz:**\n"
    #         "- Überprüfen Sie, ob die Aufgabenstellung, die Zustandsübergangstabelle und die Beispielablauftabelle logisch konsistent und vollständig sind.\n"
    #         "- Simulieren Sie die Turingmaschine basierend auf den korrigierten Tabellen, um sicherzustellen, dass die Lösung fehlerfrei ist und das gewünschte Ergebnis liefert.\n"
    #         "- Achten Sie darauf, dass keine unnötigen Zustände oder Übergänge eingefügt werden und die Tabellen effizient gestaltet sind.\n\n"
    #
    #         "### Wichtig:\n"
    #         "Die Korrektur muss den höchsten akademischen Standards entsprechen. Alle Bestandteile der Aufgabe (Zustandsübergangstabelle und Beispielablauftabelle) "
    #         "müssen logisch konsistent und vollständig sein. Fehler oder Unstimmigkeiten dürfen unter keinen Umständen bestehen bleiben. "
    #         "Eine fehlerfreie Lösung ist essenziell.\n\n"
    #     )

    @staticmethod
    def get_analysis_prompt(question_content):
        return (
            f"Aufgabenstellung: {question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"Beispiel: {question_content[SECTION_EXAMPLE]}\n\n"

            "**Analyse Aufgabenstellung und Beispiel:**\n"
            "- Lesen und analysieren Sie die Aufgabenstellung und das gegebene Beispiel sorgfältig, um die Funktion der Turingmaschine vollständig zu verstehen.\n"
            "- Identifizieren Sie das Ziel der Aufgabe sowie alle relevanten Anforderungen und Bedingungen (z. B. Start- und Endzustände, Bandänderungen, Kopfbewegungen).\n"
            "- Achten Sie darauf, dass die Anforderungen der Aufgabenstellung klar und vollständig sind.\n\n"
        )

    @staticmethod
    def get_state_transition_table_prompt(state_transition_table_content):
        return (
            f"Zustandsübergangstabelle: {state_transition_table_content[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"

            "**Korrektur Zustandsübergangstabelle (`solution_state_transition_table`):**\n"
            "- Basierend auf der analysierten Aufgabenstellung und dem Beispiel korrigieren Sie die Zustandsübergangstabelle.\n"
            "- Stellen Sie sicher, dass alle Übergänge logisch, effizient und fehlerfrei sind.\n"
            "- Überprüfen Sie, ob die Tabelle alle möglichen Eingaben korrekt verarbeitet und nicht nur das gegebene Beispiel abdeckt.\n"
            "- Validieren Sie, dass die Start- und Endzustände korrekt definiert und erreichbar sind.\n"
            "- Korrigieren Sie die Tabelle, dass alle Bandänderungen die Anforderungen der Aufgabenstellung exakt erfüllen.\n\n"

            "**WICHTIG**: Testen Sie die verbesserte Tabelle mit verschiedenen Eingaben, um sicherzustellen, dass sie die Zielsetzung der Aufgabe vollständig erfüllt.\n"
            "Beheben Sie Unstimmigkeiten in der Abfolge, die bei der Simulation entdeckt werden könnten.\n\n"
        )

    @staticmethod
    def get_example_flow_table_prompt(example_flow_table_content):
        return (
            f"Beispielablauftabelle: {example_flow_table_content[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]}\n\n"

            "**Korrektur Beispielablauftabelle (`solution_example_flow_table`):**\n"
            "- Basierend auf der korrigierten Zustandsübergangstabelle und der analysierten Aufgabenstellung korrigieren Sie die Beispielablauftabelle.\n"
            "- Stellen Sie sicher, dass jeder Schritt der Tabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
            "- Überprüfen Sie, ob alle Kopfbewegungen, Bandänderungen und Zustände korrekt dokumentiert sind und immer an der richtigen Stelle erfolgt.\n"
            "- Validieren Sie, dass die Tabelle den Ablauf der Turingmaschine präzise beschreibt und die Start- und Endposition des Kopfes korrekt eingehalten wird.\n"
            "- Korrigieren Sie die Tabelle, dass die Bandänderungen und der Ablauf der Maschine fehlerfrei dokumentiert sind.\n\n"

            "**Es dürfen keine Bandänderungen oder Positionsänderungen erfolgen, die nicht mit der Zustandsübergangstabelle übereinstimmen!**\n\n"

            "**WICHTIG**: Testen Sie die verbesserte Tabelle anhand der korrigierten Zustandsübergangstabelle und analysierten Aufgabenstellung.\n"
            "Beheben Sie Unstimmigkeiten, die während der Simulation auftreten könnten, und stellen Sie sicher, dass die Tabelle als perfekte Lösung dient.\n\n"

        )

    @staticmethod
    def get_summary_prompt():
        return (
            "### Zusammenfassung und Konsistenzprüfung:\n\n"

            "- Überprüfen Sie, ob die Aufgabenstellung, die Zustandsübergangstabelle und die Beispielablauftabelle logisch konsistent und vollständig sind.\n"
            "- Simulieren Sie die Turingmaschine basierend auf den korrigierten Tabellen, um sicherzustellen, dass die Lösung fehlerfrei ist und das gewünschte Ergebnis liefert.\n"
            "- Achten Sie darauf, dass keine unnötigen Zustände oder Übergänge eingefügt werden und die Tabellen effizient gestaltet sind.\n\n"

            "### WICHTIG:\n"
            "Die Korrektur muss den höchsten akademischen Standards entsprechen. Alle Bestandteile der Aufgabe (Zustandsübergangstabelle und Beispielablauftabelle) "
            "müssen logisch konsistent und vollständig sein. Fehler oder Unstimmigkeiten dürfen unter keinen Umständen bestehen bleiben. "
            "Eine fehlerfreie Lösung ist essenziell.\n\n"
        )

    @staticmethod
    def get_validation_user_prompt(task_parts):
        return (
                ValidationPromptBuilder.get_analysis_prompt(task_parts) +
                ValidationPromptBuilder.get_state_transition_table_prompt(task_parts) +
                ValidationPromptBuilder.get_example_flow_table_prompt(task_parts) +
                ValidationPromptBuilder.get_summary_prompt()
        )

    # @staticmethod
    # def get_validation_user_prompt(task_parts):
    #     return (
    #         "### ANFORDERUNGEN ZUR KORREKTUR:\n\n"
    #         "Korrigieren Sie die gegebene Aufgabe bestehend aus Aufgabenstellung, Zustandsübergangstabelle, Beispielablauftabelle und Lösung.\n"
    #
    #         "1. **Zustandsübergangstabelle:**\n"
    #         "- Prüfen Sie, ob die Tabelle alle möglichen Eingaben korrekt verarbeitet, nicht nur das Beispiel.\n"
    #         "- Validieren Sie, dass alle Übergänge logisch und effizient sind.\n"
    #         "- Stellen Sie sicher, dass die Tabelle den korrekten Start- und Endzustand enthält.\n\n"
    #
    #         "2. **Beispielablauftabelle:**\n"
    #         "- Stellen Sie sicher, dass die Tabelle exakt mit der Zustandsübergangstabelle übereinstimmt.\n"
    #         "- Überprüfen Sie, ob alle Kopfbewegungen, Bandänderungen und Zustände korrekt dokumentiert sind.\n"
    #         "- Validieren Sie, dass die Ablauftabelle den Start- und Endzustand sowie den Ablauf der Turingmaschine korrekt abbildet.\n\n"
    #
    #         "3. **Konsistenz und Vollständigkeit:**\n"
    #         "- Überprüfen Sie, ob die Aufgabenstellung, Zustandsübergangstabelle und Beispielablauftabelle logisch zusammenpassen.\n"
    #         "- Simulieren Sie die Turingmaschine mit verschiedenen Eingaben, um sicherzustellen, dass die Aufgabe korrekt gelöst wird.\n\n"
    #
    #         "### Aufgabe zur Überprüfung:\n\n"
    #         f"{task_parts}\n\n"
    #     )

    # @staticmethod
    # def get_validation_user_prompt(task_parts):
    #     return (
    #         "### ANFORDERUNGEN ZUR KORREKTUR:\n\n"
    #
    #         "Korrigieren Sie die gesamte Aufgabe, einschließlich der Zustandsübergangstabelle und der Beispielablauftabelle, um sicherzustellen, dass diese vollständig konsistent mit der Aufgabenstellung, den Zusatzinformationen und dem Beispiel sind.\n\n"
    #
    #         "1. **Zustandsübergangstabelle:**\n"
    #         "- Prüfen Sie, ob die Tabelle alle möglichen Eingaben korrekt verarbeitet, nicht nur das Beispiel.\n"
    #         "- Überprüfen Sie, ob Übergänge effizient und logisch sind, ohne unnötige Zustände oder Übergänge hinzuzufügen.\n"
    #         "- Vergewissern Sie sich, dass der Start- und Endzustand korrekt definiert und erreichbar sind.\n"
    #         "- Überprüfen Sie, ob alle Übergänge und Bandänderungen präzise und konsistent mit der Aufgabenstellung sind.\n"
    #         "- Achten Sie insbesondere darauf, dass Übergänge bei Sonderzeichen wie Leerzeichen (`■`) den Vorgaben entsprechen.\n\n"
    #
    #         "2. **Beispielablauftabelle:**\n"
    #         "- Validieren Sie, dass die Beispielablauftabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
    #         "- Überprüfen Sie, ob jede Kopfbewegung und jede Bandänderung korrekt dokumentiert ist.\n"
    #         "- Stellen Sie sicher, dass jede Bandänderung und jeder Übergang die korrekte Abfolge abbildet und keine unnötigen Schritte enthält.\n"
    #         "- Stellen Sie sicher, dass die Start- und Endposition des Lese-/Schreibkopfes exakt den Anforderungen der Aufgabenstellung entspricht.\n"
    #         "- Vergewissern Sie sich, dass die Tabelle jeden Übergang und jede Änderung korrekt und nachvollziehbar abbildet.\n\n"
    #
    #         "3. **Konsistenz und Simulation:**\n"
    #         "- Überprüfen Sie die gesamte Aufgabe auf Konsistenz zwischen Aufgabenstellung, Zustandsübergangstabelle, Beispielablauftabelle und Lösung.\n"
    #         "- Simulieren Sie den Ablauf der Turingmaschine mit verschiedenen Eingaben, um sicherzustellen, dass die Aufgabe vollständig und korrekt gelöst werden kann.\n"
    #         "- Validieren Sie abschließend, dass keine widersprüchlichen oder überflüssigen Schritte vorhanden sind.\n\n"
    #
    #         "### Wichtige Hinweise:\n"
    #         "- Es ist von größter Bedeutung, dass alle Bestandteile der Aufgabe (Zustandsübergangstabelle, Beispielablauftabelle, Aufgabenstellung, Lösung) fehlerfrei und aufeinander abgestimmt sind.\n"
    #         "- Jede Abweichung oder Ungenauigkeit kann die Korrektheit der Aufgabe gefährden und ihre Nutzung in Prüfungen beeinträchtigen.\n"
    #         "- Bitte stellen Sie sicher, dass Ihre Korrekturen höchsten Qualitätsstandards entsprechen und die Aufgabe als perfekte Musterlösung dient.\n\n"
    #
    #         "### AUFGABE ZUR ÜBERPRÜFUNG:\n\n"
    #         f"{task_parts}\n\n"
    #     )

    @staticmethod
    def get_validation_task_analysis_prompt():
        return (
            "### Analyse der Aufgabe:\n"
            "- Analysiere die Aufgabenstellung, Zusatzinformationen und das Beispiel sorgfältig, um die Zielsetzung der Aufgabe vollständig zu verstehen.\n"
            "- Stelle sicher, dass die Anforderungen an Start- und Endposition des Lese-/Schreibkopfes vollständig verstanden sind.\n"
            "- Identifiziere potenzielle Fehler in den Tabellen und notiere, welche Bereiche überarbeitet werden müssen.\n"
        )

    @staticmethod
    def get_validation_state_transition_table_prompt():
        return (
            "### Korrektur der Zustandsübergangstabelle (`solution_state_transition_table`):\n"
            "- Überprüfe die Tabelle und behebe alle Fehler, ohne neue Fehler einzufügen.\n"
            "- Stelle sicher, dass die Tabelle vollständig ist und alle möglichen Szenarien abdeckt, nicht nur das gegebene Beispiel.\n"
            "- Verifiziere, dass alle Zustände, Übergänge und Bandänderungen mit den Vorgaben der Aufgabenstellung übereinstimmen.\n"
            "- Überprüfe, ob die Start- und Endzustände korrekt definiert und erreichbar sind.\n"
            "- Simuliere den Ablauf der Tabelle mit verschiedenen Eingaben, um sicherzustellen, dass die Turingmaschine korrekt funktioniert.\n"
            "- Optimiere die Tabelle so, dass sie effizient und klar verständlich bleibt.\n"
        )

    @staticmethod
    def get_validation_example_flow_table_prompt():
        return (
            "### Korrektur der Beispielablauftabelle (`solution_example_flow_table`):\n"
            "- Überprüfe und korrigiere die Beispielablauftabelle vollständig, basierend auf der korrigierten Zustandsübergangstabelle.\n"
            "- Stelle sicher, dass jeder Schritt exakt mit der Zustandsübergangstabelle übereinstimmt.\n"
            "- Verifiziere, dass die Kopfposition und der Bandinhalt in jedem Schritt korrekt dokumentiert sind.\n"
            "- Kontrolliere, dass der Lese-/Schreibkopf an der in der Aufgabenstellung angegebenen Startposition beginnt und in der Endposition korrekt endet.\n"
            "- Korrigiere fälschicherweise zusätzlich hinzugefügte Symbole die nicht dem Zustandsübergang konsistetn sind.\n"
            "- Überprüfe, ob alle Übergänge und Bandänderungen präzise umgesetzt wurden.\n"
            "- Die Tabelle muss vollständig, konsistent und logisch nachvollziehbar sein.\n"
        )

    @staticmethod
    def get_validation_solution_prompt():
        return (
            "### Korrektur der Lösung (`solution_content`):\n"
            "- Überprüfe die gesamte Lösung auf Konsistenz mit der korrigierten Zustandsübergangstabelle und Beispielablauftabelle.\n"
            "- Kontrolliere, ob alle Schritte der Lösung logisch, nachvollziehbar und präzise beschrieben sind.\n"
            "- Optimiere die Lösung, damit sie vollständig, verständlich und frei von Unstimmigkeiten ist.\n"
        )

    @staticmethod
    def get_validation_final_validation_prompt():
        return (
            "### Abschließende Validierung:\n"
            "- Überprüfe, ob die korrigierten Tabellen exakt mit den Vorgaben der Aufgabenstellung übereinstimmen.\n"
            "- Simuliere die gesamte Aufgabe erneut, um sicherzustellen, dass die Zielsetzung vollständig erfüllt ist.\n"
            "- Validieren Sie, dass die gesamte Aufgabe logisch konsistent ist und keine Unstimmigkeiten enthält.\n"
        )

    @staticmethod
    def get_validation_task_prompt(task):
        return (
            "### Aufgabe zur Korrektur:\n\n"
            "Korrigiere die gegebene Aufgabe vollständig, sodass alle Bestandteile logisch konsistent, fehlerfrei und vollständig sind.\n"
            "Achte besonders auf folgende Punkte:\n\n"

            "- **Zustandsübergangstabelle:**\n"
            "  - Überprüfe, ob alle Zustände, Übergänge und Bandänderungen korrekt sind und die Tabelle alle möglichen Eingaben abdeckt.\n"
            "  - Stelle sicher, dass die Start- und Endzustände präzise definiert sind und erreicht werden können.\n\n"

            "- **Beispielablauftabelle:**\n"
            "  - Jeder Schritt muss exakt mit der Zustandsübergangstabelle übereinstimmen.\n"
            "  - Die Kopfposition und Bandänderungen müssen korrekt dokumentiert sein.\n\n"

            "- **Gesamte Lösung:**\n"
            "  - Überprüfe, ob die Lösung vollständig, logisch und präzise formuliert ist.\n\n"

            "Korrigiere die gegebene Aufgabe vollständig entsprechend der vorgegebenen Anforderungen:\n"
            f"{task}\n\n"
        )

#
#     @staticmethod
#     def get_validation_system_prompt():
#         return (
#                 "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen überprüft und korrigiert.\n"
#                 "Dein Ziel ist es, sicherzustellen, dass alle Bestandteile der Aufgabe logisch konsistent, fehlerfrei und vollständig sind.\n"
#                 # "Gehe davon aus, dass die Tabellen Fehler enthalten, die korrigiert werden müssen.\n\n"
#                 #
#                 # "### Folgende Schritte:\n"
#                 # "- **Vorgehensweise und Korrekturanforderungen:** Zuerst erhältst du klare Informationen zur Vorgehensweise und was genau korrigiert werden muss.\n"
#                 # "- **Übergabe der zu korrigierenden Aufgabe:** Anschließend erhältst du die gesamte zu verbessernde Aufgabe, einschließlich aller relevanten Bestandteile.\n"
#                 # "- **Aufforderung zur Korrektur:** Du wirst aufgefordert, die Aufgabe zu analysieren und sämtliche Fehler zu korrigieren, um sie vollständig und fehlerfrei zu machen.\n\n"
#         )
#
#     @staticmethod
#     def get_validation_task_analysis_prompt():
#         return (
#             "### Analyse der Aufgabe:\n"
#             "- Analysiere die Aufgabenstellung, Zusatzinformationen und das Beispiel sorgfältig, um die Zielsetzung der Aufgabe vollständig zu verstehen.\n"
#             "- Stelle sicher, dass du die Anforderungen an die Aufgabe, einschließlich der Start- und Endposition des Lese-/Schreibkopfes vollständig verstanden hast.\n"
#             # "- Identifiziere potenzielle Fehler in den Tabellen und notiere, welche Bereiche überarbeitet werden müssen.\n"
#         )
#
#     # @staticmethod
#     # def get_validation_state_transition_table_prompt():
#     #     return (
#     #         "### Korrektur der Zustandsübergangstabelle (`solution_state_transition_table`):\n"
#     #         "- Beginne mit der Zustandsübergangstabelle und behebe alle Fehler, ohne neue Fehler einzufügen.\n"
#     #         "- Überprüfe, ob die Tabelle vollständig ist und alle möglichen Szenarien korrekt abbildet.\n"
#     #         "- Verifiziere, dass alle Zustände und Übergänge mit den Vorgaben der Aufgabenstellung und Zusatzinformationen übereinstimmen.\n"
#     #         "- Stelle sicher, dass die Tabelle effizient ist und nur die notwendigen Zustände und Übergänge enthält.\n"
#     #         "- Simuliere den Ablauf der Turingmaschine mit verschiedenen Eingaben, um die Korrektheit und Konsistenz der Zustandsübergangstabelle zu überprüfen.\n"
#     #     )
#
#     @staticmethod
#     def get_validation_state_transition_table_prompt():
#         return (
#             "### Korrektur der Zustandsübergangstabelle (`solution_state_transition_table`):\n"
#             "- Beginne mit der Zustandsübergangstabelle und behebe alle Fehler, ohne neue Fehler einzufügen.\n"
#             "- Überprüfe, ob die Tabelle vollständig ist und alle möglichen Szenarien korrekt abbildet.\n"
#             "- Verifiziere, dass alle Zustände und Übergänge mit den Vorgaben der Aufgabenstellung und Zusatzinformationen übereinstimmen.\n"
#             "- Stelle sicher, dass die Tabelle effizient ist und nur die notwendigen Zustände und Übergänge enthält.\n"
#             "- Simuliere den Ablauf der Turingmaschine mit verschiedenen möglichen Eingaben, um sicherzustellen, dass die Tabelle das Ziel der Aufgabe vollständig erfüllt.\n\n"
#
#             "#### Prüfung auf Start- und Endzustände:\n"
#             "- Überprüfe, ob die in den Zusatzinformationen der Aufgabenstellung definierten Start- und Endzustände korrekt in der Tabelle abgebildet sind.\n"
#             "- Stelle sicher, dass die Turingmaschine zuverlässig vom definierten Startzustand aus beginnt und korrekt im Endzustand endet.\n"
#             "- Validieren Sie, dass die Turingmaschine das gewünschte Verhalten zeigt, unabhängig davon, welche Eingabe übergeben wird.\n\n"
#
#             "#### Prüfung auf Aufgabenanforderungen:\n"
#             "- Vergewissere dich, dass die Tabelle das Ziel der Aufgabenstellung vollständig erfüllt.\n"
#             "- Überprüfe, ob alle möglichen Eingaben korrekt verarbeitet werden und nicht nur das angegebene Beispiel.\n"
#             "- Stelle sicher, dass alle Übergänge und Bandänderungen präzise und den Vorgaben entsprechend umgesetzt sind.\n"
#             "- Achte darauf, dass die Handhabung von Leerzeichen (`■`) und Bandgrenzen korrekt ist, insbesondere wenn der Lese-/Schreibkopf über die ursprüngliche Eingabe hinausgeht.\n\n"
#
#             "#### Perfekte Musterlösung:\n"
#             "- Die Tabelle muss als perfekte Musterlösung für die Aufgabenstellung dienen.\n"
#             "- Alle Zustände, Übergänge und Bandänderungen müssen fehlerfrei, vollständig und logisch nachvollziehbar sein.\n"
#             "- Optimiere die Zustandsübergangstabelle so, dass sie effizient und leicht verständlich ist, ohne unnötige Zustände oder Übergänge einzufügen.\n"
#             "- Vermeide jegliche Abweichungen von den Anforderungen der Aufgabenstellung oder unklare Zustandsdefinitionen.\n\n"
#         )
#
#     # @staticmethod
#     # def get_validation_example_flow_table_prompt():
#     #     return (
#     #         "### 3. Korrektur der Beispielablauftabelle (`solution_example_flow_table`):\n"
#     #         "- Basierend auf der korrigierten Zustandsübergangstabelle überprüfst und korrigierst du die Beispielablauftabelle neu.\n"
#     #         "- Stelle sicher, dass jeder Schritt in der Beispielablauftabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
#     #         "- Überprüfe die Kopfpositionen und den Bandinhalt in jedem Schritt, um sicherzustellen, dass sie korrekt aktualisiert und dokumentiert sind.\n"
#     #         "- Behebe alle Fehler und Unstimmigkeiten, ohne die Ablauftabelle unnötig kompliziert zu machen.\n"
#     #         bandänderungen müssen immer wie erwartet aktualisiert werden etc... der kopf soll in der in der gegebenen Startposition starten und nicht irgendwo und so auch enden wie in der aufgabenstellung angegeben
#     #     )
#
#     @staticmethod
#     def get_validation_example_flow_table_prompt():
#         return (
#             "### 3. Korrektur der Beispielablauftabelle (`solution_example_flow_table`):\n"
#             "- Basierend auf der korrigierten Zustandsübergangstabelle überprüfst und korrigierst du die Beispielablauftabelle vollständig neu.\n"
#             "- Stelle sicher, dass jeder Schritt in der Beispielablauftabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
#             "- Überprüfe, dass der Ablauf der Turingmaschine korrekt dargestellt wird und alle Schritte logisch und nachvollziehbar sind.\n\n"
#
#             "#### Prüfung der Kopfpositionen:\n"
#             "- Stelle sicher, dass der Lese-/Schreibkopf an der in der Aufgabenstellung definierten Startposition beginnt und die in den Zusatzinformationen angegebene Endposition korrekt erreicht.\n"
#             "- Dokumentiere die Kopfbewegungen in jedem Schritt präzise und nachvollziehbar.\n\n"
#
#             "#### Prüfung der Bandänderungen:\n"
#             "- Überprüfe, ob der Bandinhalt in jedem Schritt korrekt aktualisiert wird, einschließlich der richtigen Handhabung von Leerzeichen (`■`) und Bandgrenzen.\n"
#             "- Stelle sicher, dass Bandänderungen wie erwartet durchgeführt werden und keine inkonsistenten Werte oder unlogischen Änderungen auftreten.\n\n"
#
#             "#### Konsistenz und Präzision:\n"
#             "- Verifiziere, dass die Beispielablauftabelle konsistent mit der korrigierten Zustandsübergangstabelle und der Aufgabenstellung ist.\n"
#             "- Stelle sicher, dass alle Schritte exakt beschrieben sind und keine Unklarheiten oder Widersprüche enthalten.\n"
#             "- Behebe alle Fehler und Unstimmigkeiten, ohne die Ablauftabelle unnötig kompliziert zu machen.\n\n"
#
#             "#### Perfekte Musterlösung:\n"
#             "- Die Beispielablauftabelle muss als perfekte Ergänzung zur korrigierten Zustandsübergangstabelle und der Aufgabenstellung dienen.\n"
#             "- Alle Schritte, Kopfbewegungen und Bandänderungen müssen präzise, logisch und vollständig dokumentiert sein.\n"
#             "- Achte darauf, dass die Tabelle universell korrekt ist und als Musterlösung höchsten Qualitätsstandards entspricht.\n"
#         )
#
#     @staticmethod
#     def get_validation_solution_prompt():
#         return (
#             "### Korrektur der Lösung (`solution_content`):\n"
#             "- Überprüfe die gesamte Lösung auf Konsistenz mit der korrigierten Zustandsübergangstabelle und der Beispielablauftabelle.\n"
#             "- Kontrolliere, ob alle Schritte der Lösung präzise, logisch und nachvollziehbar beschrieben sind.\n"
#             "- Stelle sicher, dass die Lösung vollständig und frei von Unstimmigkeiten ist.\n"
#             "- Optimiere die Lösung, damit sie klar und verständlich formuliert ist und den höchsten akademischen Standards entspricht.\n"
#         )
#
#     @staticmethod
#     def get_validation_final_validation_prompt():
#         return (
#             "### 5. Abschließende Validierung:\n"
#             "- Überprüfe, ob die korrigierten Tabellen exakt mit den Vorgaben der Aufgabenstellung übereinstimmen und das Beispiel korrekt abbilden.\n"
#             "- Validieren Sie, dass die gesamte Aufgabe logisch konsistent ist und keine Unstimmigkeiten enthält.\n"
#             "- Simuliere abschließend die gesamte Aufgabe erneut, um sicherzustellen, dass die Korrekturen vollständig sind und die Zielsetzung der Aufgabe erfüllt wird.\n"
#         )
#
#     @staticmethod
#     def get_full_validation_requirements_prompt():
#         return (
#             f"{ValidationPromptBuilder.get_validation_task_analysis_prompt()}\n"
#             f"{ValidationPromptBuilder.get_validation_state_transition_table_prompt()}\n"
#             f"{ValidationPromptBuilder.get_validation_example_flow_table_prompt()}\n"
#             f"{ValidationPromptBuilder.get_validation_solution_prompt()}\n"
#             f"{ValidationPromptBuilder.get_validation_final_validation_prompt()}\n"
#             "Korrigiere die Aufgabe so, dass sie den höchsten Qualitätsstandards entspricht und keine unnötigen Änderungen oder Verschlechterungen enthält. "
#             "Die Korrektur darf ausschließlich dazu dienen, die ursprüngliche Zielsetzung der Aufgabe vollständig zu erfüllen."
#         )
#
#     @staticmethod
#     def get_validation_requirements_prompt(incorrect_task):
#         return (
#             "### Vorgehensweise zur Korrektur:\n\n"
#
#             "1. **Analyse der Aufgabe:**\n"
#             "- Lies die Aufgabenstellung, Zusatzinformationen und das Beispiel sorgfältig, um die Zielsetzung der Aufgabe vollständig zu verstehen.\n"
#             "- Stelle sicher, dass du die Anforderungen an die Zustandsübergangstabelle und die Beispielablauftabelle, einschließlich der Start- und Endposition des Lese-/Schreibkopfes und aller Bandgrenzen, vollständig verstanden hast.\n"
#             "- Identifiziere potenzielle Fehler in den Tabellen und notiere, welche Bereiche überarbeitet werden müssen.\n\n"
#
#             "2. **Korrektur der Zustandsübergangstabelle (solution_state_transition_table):**\n"
#             "- Beginne mit der Zustandsübergangstabelle und behebe alle Fehler, ohne neue Fehler einzufügen.\n"
#             "- Überprüfe, ob die Tabelle vollständig ist und alle möglichen Szenarien korrekt abbildet.\n"
#             "- Verifiziere, dass alle Zustände und Übergänge mit den Vorgaben der Aufgabenstellung und Zusatzinformationen übereinstimmen.\n"
#             "- Stelle sicher, dass die Tabelle effizient ist und nur die notwendigen Zustände und Übergänge enthält.\n"
#             "- Simuliere den Ablauf der Turingmaschine mit verschiedenen Eingaben, um die Korrektheit und Konsistenz der Zustandsübergangstabelle zu überprüfen.\n\n"
#
#             "3. **Korrektur der Beispielablauftabelle (solution_example_flow_table):**\n"
#             "- Basierend auf der korrigierten Zustandsübergangstabelle überprüfst oder erstellst du die Beispielablauftabelle neu.\n"
#             "- Stelle sicher, dass jeder Schritt in der Beispielablauftabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
#             "- Überprüfe die Kopfpositionen und den Bandinhalt in jedem Schritt, um sicherzustellen, dass sie korrekt aktualisiert und dokumentiert sind.\n"
#             "- Behebe alle Fehler und Unstimmigkeiten, ohne die Ablauftabelle unnötig kompliziert zu machen.\n\n"
#
#             "4. **Korrektur der Lösung (solution_content):**\n"
#             "- Überprüfe die gesamte Lösung auf Konsistenz mit der korrigierten Zustandsübergangstabelle und der Beispielablauftabelle.\n"
#             "- Kontrolliere, ob alle Schritte der Lösung präzise, logisch und nachvollziehbar beschrieben sind.\n"
#             "- Stelle sicher, dass die Lösung vollständig und frei von Unstimmigkeiten ist.\n"
#             "- Optimiere die Lösung, damit sie klar und verständlich formuliert ist und den höchsten akademischen Standards entspricht.\n\n"
#
#             "5. **Abschließende Validierung:**\n"
#             "- Überprüfe, ob die korrigierten Tabellen exakt mit den Vorgaben der Aufgabenstellung übereinstimmen und das Beispiel korrekt abbilden.\n"
#             "- Validieren Sie, dass die gesamte Aufgabe logisch konsistent ist und keine Unstimmigkeiten enthält.\n"
#             "- Simuliere abschließend die gesamte Aufgabe erneut, um sicherzustellen, dass die Korrekturen vollständig sind und die Zielsetzung der Aufgabe erfüllt wird.\n\n"
#
#             "Korrigiere die Aufgabe so, dass sie den höchsten Qualitätsstandards entspricht und keine unnötigen Änderungen oder Verschlechterungen enthält. "
#             "Die Korrektur darf ausschließlich dazu dienen, die ursprüngliche Zielsetzung der Aufgabe vollständig zu erfüllen."
#         )
#
#     @staticmethod
#     def get_validation_incorrect_task_prompt():
#         return (
#             "### Zusätzliche Informationen:\n"
#             "Bei dieser Aufgabe handelt es sich um eine bewusst fehlerhafte Turingmaschine, die speziell für die Fehlersuche und -korrektur durch Studierende entworfen wurde. "
#             "Daher sollen die Fehler, die absichtlich in der Zustandsübergangstabelle der Aufgabenstellung enthalten sind, nicht vollständig korrigiert werden. "
#             "Die Tabelle soll nur so überarbeitet werden, dass die integrierten Fehler logisch nachvollziehbar und angemessen herausfordernd sind, "
#             "während die restliche Struktur und Funktionalität der Tabelle mit der Aufgabenstellung konsistent bleibt. "
#             "Stelle sicher, dass nur die relevanten Fehler bestehen bleiben und keine zusätzlichen oder unerwünschten Fehler enthalten sind."
#         )
#
#     @staticmethod
#     def get_validation_task_prompt(task):
#         return (
#             # f"ZU KORRIGIERENDE AUFGABE:\n\n"
#             # "KORRIGIERE DIE GEGEBENE AUFGABE KOMPLETT nach den gegebenen Anforderungen: \n\n"
#             # "KORRIGIERE DIE GEGEBENE AUFGABE KOMPLETT (mit besonderem Fokus auf die Tabellen) nach den gegebenen Anforderungen: \n\n"
#             # f"{task}\n\n"
#             # "Korrigiere die gegebene Aufgabe so, dass die Zustandsübergangstabelle und die Beispielablauftabelle vollständig zusammenpassen "
#             # "und exakt nach der Aufgabenstellung funktionieren. Achte dabei besonders darauf, dass der Start- und Endzustand korrekt sind "
#             # "und alle Übergänge sowie der Ablauf der Turingmaschine die Anforderungen der Aufgabenstellung erfüllen.\n\n"
#             # f"{task}\n\n"
#
#
#                 # "Korrigiere die gegebene Aufgabe so, dass die Zustandsübergangstabelle und die Beispielablauftabelle "
#                 # "vollständig zusammenpassen und exakt nach der Aufgabenstellung funktionieren. Achte dabei besonders darauf:\n"
#                 # "- **Start- und Endzustand:** Überprüfe, ob die in der Aufgabenstellung definierten Start- und Endzustände "
#                 # "in der Tabelle vorhanden sind und korrekt erreicht werden.\n"
#                 # "- **Korrekte Übergänge:** Stelle sicher, dass alle Übergänge und Bandänderungen die Anforderungen der Aufgabenstellung "
#                 # "erfüllen und die Tabelle für alle möglichen Eingaben funktioniert, nicht nur für das Beispiel.\n"
#                 # "- **Beispielablauftabelle:** Validiere, dass die Beispielablauftabelle mit der korrigierten Zustandsübergangstabelle "
#                 # "übereinstimmt und den Ablauf der Maschine korrekt beschreibt, einschließlich der Kopfpositionen und Bandinhalte.\n"
#                 # "- **Lösungskonsistenz:** Überprüfe abschließend die gesamte Lösung und stelle sicher, dass sie logisch konsistent, "
#                 # "vollständig und fehlerfrei ist.\n\n"
#                 # f"{task}\n\n"
#
#                 # "Korrigiere die gegebene Aufgabe so, dass die Zustandsübergangstabelle und die Beispielablauftabelle "
#                 # "vollständig zusammenpassen und exakt nach der Aufgabenstellung funktionieren. Achte dabei besonders darauf:\n"
#                 # "- **Start- und Endzustand:** Überprüfe, ob die in der Aufgabenstellung definierten Start- und Endzustände "
#                 # "in der Tabelle vorhanden sind und korrekt erreicht werden.\n"
#                 # "- **Korrekte Übergänge:** Stelle sicher, dass alle Übergänge und Bandänderungen die Anforderungen der Aufgabenstellung "
#                 # "erfüllen und die Tabelle für alle möglichen Eingaben funktioniert, nicht nur für das Beispiel.\n"
#                 #
#                 # "- **Beispielablauftabelle:** Validiere, dass die Beispielablauftabelle mit der korrigierten Zustandsübergangstabelle "
#                 # "übereinstimmt und den Ablauf der Maschine korrekt beschreibt. Achte dabei genau darauf, dass pro Zustand konsequent "
#                 # "das gelesene Zeichen, das neue Zeichen, die Bewegung und der neue Zustand exakt mit der Zustandsübergangstabelle "
#                 # "übereinstimmen. Achte auch auf den Start- und Endzustand des Kopfes.\n"
#                 #
#                 # "- **Lösungskonsistenz:** Überprüfe abschließend die gesamte Lösung und stelle sicher, dass sie logisch konsistent, "
#                 # "vollständig und fehlerfrei ist.\n\n"
#                 # f"{task}\n\n"
#
#             "### Korrigieren Sie die gegebene Aufgabe vollständig:\n"
#             "Die Zustandsübergangstabelle und die Beispielablauftabelle müssen korrekt zusammenpassen und exakt gemäß der Aufgabenstellung funktionieren. "
#             "Achten Sie auf die folgenden Qualitätsanforderungen:\n\n"
#
#             "#### 1. Qualitätsanforderungen an die Zustandsübergangstabelle:\n"
#             "- **Start- und Endzustände**: Vergewissern Sie sich, dass die in der Aufgabenstellung definierten Start- und Endzustände korrekt definiert und erreichbar sind.\n"
#             "- **Übergänge und Konsistenz**: Alle Übergänge müssen den Vorgaben der Aufgabenstellung und Zusatzinformationen entsprechen. "
#             "Stellen Sie sicher, dass die Tabelle effizient ist und nur notwendige Zustände und Übergänge enthält (inkl. Start- und Endzustand).\n"
#             "- **Verarbeitung aller Eingaben**: Die Tabelle muss alle möglichen Eingaben verarbeiten können, nicht nur das Beispiel.\n"
#             "- **Korrekte Bandänderungen**: Vergewissern Sie sich, dass alle Lese- und Schreiboperationen sowie Bewegungen des Kopfes korrekt dokumentiert sind.\n"
#             "- **Musterlösung**: Die Tabelle soll als perfekte Lösung für die Aufgabenstellung dienen und darf keine Fehler enthalten.\n\n"
#
#             "#### 2. Qualitätsanforderungen an die Beispielablauftabelle:\n"
#             "- **Übereinstimmung mit der Zustandsübergangstabelle**: Jeder Schritt der Beispielablauftabelle muss exakt mit der korrigierten Zustandsübergangstabelle übereinstimmen.\n"
#             "- **Konsequente Einhaltung**: Achten Sie darauf, dass das gelesene Zeichen, das neue Zeichen, die Bewegung und der neue Zustand in jedem Schritt präzise mit der Tabelle übereinstimmen.\n"
#             "- **Start- und Endzustand des Kopfes**: Der Lesekopf muss in der gegebenen Startposition beginnen und korrekt in der Endposition gemäß der Aufgabenstellung stoppen.\n"
#             "- **Korrekte Bandänderungen**: Bandänderungen müssen in jedem Schritt korrekt aktualisiert werden und dürfen keine unerwarteten Zeichen hinzufügen.\n\n"
#
#             "#### 3. Qualitätsanforderungen an die restliche Lösung:\n"
#             "- **Logische Konsistenz**: Alle Bestandteile der Lösung (Aufgabenstellung, Beispiel, Tabellen und Beschreibung) müssen logisch zusammenpassen und die Anforderungen der Aufgabenstellung präzise umsetzen.\n"
#             "- **Fehlerfreie Beschreibung**: Die Lösung muss präzise, verständlich und vollständig formuliert sein.\n"
#             "- **Keine zusätzlichen Fehler**: Es dürfen keine zusätzlichen Fehler oder unnötigen Änderungen eingeführt werden.\n"
#             "- **Höchste Qualität**: Die Lösung soll den höchsten akademischen Standards entsprechen und für Prüfungszwecke geeignet sein.\n\n"
#
#             "### Aufgabe:\n"
#             f"{task}\n\n"
#
#
#
#
#         )
#
#     @staticmethod
#     def get_validation_request_prompt():
#         return (
#             "KORRIGIERE DIE GEGEBENE AUFGABE KOMPLETT!"
#         )
