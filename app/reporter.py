import os
from datetime import datetime
from pathlib import Path

def generate_report(enriched_entities, triage_result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = Path.cwd() / "app" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"triage_report_{timestamp}.txt"

    symptoms = enriched_entities  # Now a list of strings
    with open(report_path, "w") as f:
        f.write("=== Triage Report ===\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("Symptoms:\n")
        for symptom in symptoms:
            f.write(f"- {symptom}\n")
        f.write(f"\nSymptom Count: {triage_result['symptom_count']}\n")
        f.write(f"Priority Score: {triage_result['priority_score']}/10\n")
        f.write(f"Triage Priority: {triage_result['priority']}\n")
        f.write(f"Possible Conditions: {triage_result['possible_conditions']}\n")
        f.write(f"\nJustification:\n{triage_result['justification']}\n")

    return str(report_path)