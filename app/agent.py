class TriageAgent:
    def __init__(self, llm):
        self.llm = llm

    def reason(self, enriched_entities):
        # Treat enriched_entities as a list of strings (symptoms)
        symptoms_list = enriched_entities
        symptom_count = len(symptoms_list)

        # Define severity weights for symptoms (example weights)
        severity_weights = {
            "fever": 2,
            "high fever": 3,
            "cough": 1,
            "shortness of breath": 3,
            "chest pain": 4,
            "dizziness": 3,
            "runny nose": 1,
            "sneezing": 1,
            "sore throat": 1,
            "body aches": 2,
            "fatigue": 2,
            "nausea": 2,
            "vomiting": 2,
            "diarrhea": 2,
            "abdominal pain": 2,
            "sudden headache": 3,
            "numbness": 3,
            "confusion": 3
        }

        # Calculate priority score (sum of severity weights, capped at 10)
        priority_score = 0
        for symptom in symptoms_list:
            priority_score += severity_weights.get(symptom.lower(), 1)
        priority_score = min(priority_score, 10)  # Cap at 10

        # Determine priority level based on score
        if priority_score >= 8:
            priority = "emergency"
        elif priority_score >= 5:
            priority = "urgent"
        else:
            priority = "routine"

        # Suggest possible conditions based on symptom patterns
        possible_conditions = self._suggest_conditions(symptoms_list)

        # Generate justification using LLM
        prompt = (
            f"Given the symptoms {', '.join(symptoms_list)}, explain why the triage priority is '{priority}' "
            f"and suggest possible conditions: {possible_conditions}."
        )
        response = self.llm(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        justification = response.strip()

        return {
            "priority": priority,
            "symptom_count": symptom_count,
            "priority_score": priority_score,
            "possible_conditions": possible_conditions,
            "justification": justification
        }

    def _suggest_conditions(self, symptoms):
        symptoms = [s.lower() for s in symptoms]
        if "fever" in symptoms and "cough" in symptoms and "shortness of breath" in symptoms:
            return "pneumonia or severe respiratory infection"
        elif "high fever" in symptoms and "body aches" in symptoms and "fatigue" in symptoms:
            return "influenza (flu)"
        elif "chest pain" in symptoms and "shortness of breath" in symptoms and "dizziness" in symptoms:
            return "cardiac event (e.g., heart attack)"
        elif "runny nose" in symptoms and "sneezing" in symptoms and "sore throat" in symptoms:
            return "common cold or allergies"
        elif "nausea" in symptoms and "vomiting" in symptoms and "diarrhea" in symptoms:
            return "gastroenteritis"
        elif "sudden headache" in symptoms and "numbness" in symptoms and "confusion" in symptoms:
            return "stroke"
        else:
            return "undetermined condition"