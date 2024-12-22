from Const import SECTION_QUESTION_CONTENT, SECTION_EXAMPLE, SECTION_SOLUTION_STATE_TRANSITION_TABLE, \
    SECTION_SOLUTION_EXAMPLE_FLOW_TABLE


class ValidationPromptBuilder:

    @staticmethod
    def get_minimal_prompt(question_content, state_transition_table_content, example_flow_table_content):
        return (
            f"Aufgabenstellung: {question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"Beispiel: {question_content[SECTION_EXAMPLE]}\n\n"
            f"Zustandsübergangstabelle: {state_transition_table_content[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"
            f"Beispielablauftabelle: {example_flow_table_content[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]}\n\n"

            "Korrigieren Sie die beiden Tabellen auf Basis der Aufgabenstellung und dem gegeben Beispiel\n"
            "Geben Sie anschließend die komplett richtige Aufgabe zurück!\n"
        )

    @staticmethod
    def get_analysis_prompt(question_content):
        return (
            f"Aufgabenstellung: {question_content[SECTION_QUESTION_CONTENT]}\n\n"
            f"Beispiel: {question_content[SECTION_EXAMPLE]}\n\n"
            
            "**Analyse Aufgabenstellung und Beispiel:**\n"
            "- Lesen und analysieren Sie die Aufgabenstellung und das gegebene Beispiel sorgfältig, um die Funktion der Turingmaschine vollständig zu verstehen.\n"
            "- Identifizieren Sie das Ziel der Aufgabe sowie alle relevanten Anforderungen und Bedingungen (z. B. Start- und Endzustände, Bandänderungen, Kopfbewegungen).\n"
            "- Merken Sie sich die Anforderungen um die folgende Zustandsübergangstabelle und Beispielablauftabelle zu korrigieren.\n"
            # "- Achten Sie darauf, dass die Anforderungen der Aufgabenstellung klar und vollständig sind.\n\n"
            #
            # "Sollten Unstimmigkeiten innerhalb der Aufgabenstellung auffallen, korrigieren Sie diese direkt!\n\n"
        )

    @staticmethod
    def get_state_transition_table_prompt(state_transition_table_content):
        return (
            f"Zustandsübergangstabelle: {state_transition_table_content[SECTION_SOLUTION_STATE_TRANSITION_TABLE]}\n\n"
            
            "**Korrektur Zustandsübergangstabelle (`solution_state_transition_table`):**\n"
            "- Basierend auf der analysierten Aufgabenstellung und dem Beispiel KORRIGIEREN Sie die Zustandsübergangstabelle.\n"
            "- Falls die Tabelle bereits korrekt ist, nehmen Sie keine Änderungen vor.\n"
            "- Stellen Sie sicher, dass alle Übergänge logisch, effizient und fehlerfrei sind.\n"
            "- Überprüfen Sie, ob die Tabelle nicht nur auf das gegebene Beispiel zugeschnitten ist, sondern dass es auch für alle anderen Eingaben korrekt funktionieren, die gemäß der Aufgabenstellung erwartet werden.\n"
            "- Validieren Sie, dass die Start- und Endzustände korrekt definiert und erreichbar sind.\n"
            "- Überprüfen Sie die Verarbeitung des Leerzeichens ('■') und stellen Sie sicher, dass die Tabelle keine unnötigen Übergänge hinzufügt.\n"
            "- Korrigieren Sie die Tabelle, dass alle Bandänderungen die Anforderungen der Aufgabenstellung exakt erfüllen.\n\n"
            
            
            "**WICHTIG**: Testen Sie die verbesserte Tabelle mit verschiedenen Eingaben, um sicherzustellen, dass sie die Zielsetzung der Aufgabe vollständig erfüllt.\n"
            "Beheben Sie Unstimmigkeiten in der Abfolge, die bei der Simulation entdeckt werden könnten.\n\n"
        )

    @staticmethod
    def get_example_flow_table_prompt(example_flow_table_content):
        return (
            f"Beispielablauftabelle: {example_flow_table_content[SECTION_SOLUTION_EXAMPLE_FLOW_TABLE]}\n\n"
            
            "**Korrektur Beispielablauftabelle (`solution_example_flow_table`):**\n"
            "- Basierend auf der korrigierten Zustandsübergangstabelle und der analysierten Aufgabenstellung KORRIGIEREN Sie die Beispielablauftabelle.\n"
            "- Stellen Sie sicher, dass jeder Schritt der Tabelle exakt mit der korrigierten Zustandsübergangstabelle übereinstimmt.\n"
            "- Überprüfen Sie, ob alle Kopfbewegungen, Bandänderungen und Zustände korrekt dokumentiert sind und immer an der richtigen Stelle erfolgt.\n"
            "- Achten Sie auf die korrekte Verarbeitung von Leerzeichens ('■') und fügen Sie keine ungewollt hinzu!"
            "- Validieren Sie, dass die Tabelle den Ablauf der Turingmaschine präzise beschreibt und die Start- und Endposition des Kopfes korrekt eingehalten wird.\n"
            "- Korrigieren Sie die Tabelle, dass die Bandänderungen und der Ablauf der Maschine fehlerfrei dokumentiert sind.\n\n"
            
            "**Es dürfen keine Bandänderungen oder Positionsänderungen erfolgen, die nicht mit der Zustandsübergangstabelle übereinstimmen!**\n\n"
            
            "**WICHTIG**: Testen Sie die verbesserte Tabelle anhand der korrigierten Zustandsübergangstabelle und analysierten Aufgabenstellung.\n"
            "Beheben Sie Unstimmigkeiten, die während der Simulation auftreten könnten, und stellen Sie sicher, dass die Tabelle als perfekte Lösung dient.\n\n"

        )

    @staticmethod
    def get_summary_prompt():
        return (
            "### Abschließende Konsistenzprüfung:\n\n"
        
            "- Überprüfen Sie, ob die Aufgabenstellung, die Zustandsübergangstabelle und die Beispielablauftabelle logisch konsistent und vollständig sind.\n"
            "- Simulieren Sie die Turingmaschine basierend auf den korrigierten Tabellen, um sicherzustellen, dass die Lösung fehlerfrei ist und das gewünschte Ergebnis liefert.\n"
            "- Achten Sie darauf, dass keine unnötigen Zustände oder Übergänge eingefügt würden und die Tabellen effizient gestaltet sind.\n\n"
            
            "### WICHTIG:\n"
            "Nach der Korrektur müssen die Tabellen als Musterlösung geeignet sein!"
            "Alle Bestandteile der Aufgabe müssen logisch konsistent und vollständig sein. Fehler oder Unstimmigkeiten dürfen unter keinen Umständen bestehen bleiben. "
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