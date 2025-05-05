from utils.logger import setup_logger

def enrich_entities(entities):
    logger = setup_logger()
    logger.info(f"Enriching entities: {entities}")
    # Mock enrichment: Map symptoms to possible conditions
    symptom_to_conditions = {
        "fever": ["Influenza", "COVID-19", "Bacterial Infection"],
        "cough": ["Influenza", "COVID-19", "Bronchitis"],
        "shortness of breath": ["COVID-19", "Pneumonia", "Asthma"],
        "headache": ["Migraine", "Tension Headache", "Dehydration"],
        "fatigue": ["Chronic Fatigue Syndrome", "Anemia", "Dehydration"]
    }
    enriched = entities.copy()
    enriched["possible_conditions"] = []
    for symptom in entities.get("symptoms", []):
        conditions = symptom_to_conditions.get(symptom.lower(), [])
        enriched["possible_conditions"].extend(conditions)
    enriched["possible_conditions"] = list(set(enriched["possible_conditions"]))
    logger.info(f"Enriched entities: {enriched}")
    return enriched