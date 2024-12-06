class ValidationPromptBuilder:

    @staticmethod
    def get_validation_system_prompt():
        return (
            "Du bist ein spezialisiertes KI-Modell, das Prüfungsaufgaben zu Turingmaschinen überprüft und korrigiert.\n"
            "Dein Ziel ist es, sicherzustellen, dass alle Bestandteile der Aufgabe (Aufgabenstellung, Zusatzinformationen, "
            "Beispiel, Zustandsübergangstabelle, Beispielablauftabelle und Lösung) logisch konsistent, fehlerfrei und vollständig sind.\n"
        )

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
