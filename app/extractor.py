import spacy
from utils.logger import setup_logger

def extract_entities(text, nlp):
    logger = setup_logger()
    logger.info(f"Extracting entities from text: {text}")
    doc = nlp(text)
    entities = {"symptoms": [], "conditions": []}
    for ent in doc.ents:
        if ent.label_ == "DISEASE":
            entities["conditions"].append(ent.text.lower())
        elif ent.label_ == "CHEMICAL":  # Proxy for symptoms in this model
            entities["symptoms"].append(ent.text.lower())
    # Fallback: Extract symptoms from text if no entities found
    if not entities["symptoms"]:
        for token in doc:
            if token.text.lower() in ["fever", "cough", "headache", "fatigue", "shortness of breath"]:
                entities["symptoms"].append(token.text.lower())
    entities["symptoms"] = list(set(entities["symptoms"]))
    entities["conditions"] = list(set(entities["conditions"]))
    logger.info(f"Extracted entities: {entities}")
    return entities