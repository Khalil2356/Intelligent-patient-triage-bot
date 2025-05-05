
# Intelligent Patient Triage Bot

## Overview
The Intelligent Patient Triage Bot is an AI-powered tool designed to assist medical professionals in emergency departments by triaging patients based on their symptoms. It processes symptom inputs (e.g., "fever, cough, shortness of breath") and provides:
- Triage priority (emergency, urgent, routine)
- Priority score (out of 10)
- Possible conditions (e.g., pneumonia)
- Generated reports and visualizations
- Natural language justifications using TinyLlama-1.1B

*Note*: This is a prototype and not intended for real medical use without professional validation.

## Features
- *Symptom Analysis*: Extracts symptoms using spaCy’s en_ner_bc5cdr_md model.
- *Triage Logic*: Uses Rule-Based Reasoning to calculate priority scores and suggest conditions.
- *Text Generation*: Leverages TinyLlama-1.1B-Chat-v1.0 to provide natural language explanations.
- *Reports & Visualizations*: Generates detailed reports and symptom severity visualizations.

## Tech Stack
- *Python*: 3.10
- *NLP*: spaCy, scispacy (en_ner_bc5cdr_md model)
- *Machine Learning*: TinyLlama-1.1B-Chat-v1.0 (via transformers)
- *Visualization*: Matplotlib
- *Dependencies*: Managed via requirements.txt
## input
python app/main.py --input "fever, cough, shortness of breath"
## output
Triage Recommendation Priority: urgent
Symptom Count: 3
Priority Score: 6/10
Possible Conditions: pneumonia or severe respiratory infection
Details: Given the symptoms fever, cough, shortness of breath, the triage priority is 'urgent'...
Report saved at: app/reports/triage_report_<timestamp>.txt
Visualization saved at: app/visualizations/triage_viz_<timestamp>.png

