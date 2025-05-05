import argparse
import spacy
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from utils.logger import setup_logger
from extractor import extract_entities
from enrichment import enrich_entities
from agent import TriageAgent
from reporter import generate_report
from visualizer import generate_visualization
from pathlib import Path

def main():
    logger = setup_logger()
    logger.info("Starting Intelligent Patient Triage Bot (CPU-optimized)")

    logger.info("Loading spaCy biomedical model...")
    nlp = spacy.load("en_ner_bc5cdr_md")

    logger.info("Loading TinyLlama model from local directory...")
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    local_model_dir = Path.cwd() / "models" / "TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
    model = AutoModelForCausalLM.from_pretrained(
        local_model_dir,
        device_map="cpu",
        torch_dtype="auto"
    )
    llm = pipeline("text-generation", model=model, tokenizer=tokenizer)
    triage_agent = TriageAgent(llm)

    parser = argparse.ArgumentParser(description="Intelligent Patient Triage Bot")
    parser.add_argument("--input", type=str, help="Patient symptom description")
    args = parser.parse_args()

    if args.input:
        logger.info(f"Processing input: {args.input}")
        entities = extract_entities(args.input, nlp)
        logger.info(f"Extracted entities: {entities}")

        enriched_entities = enrich_entities(entities)
        logger.info(f"Enriched entities: {enriched_entities}")

        triage_result = triage_agent.reason(enriched_entities)
        logger.info(f"Triage result: {triage_result}")

        report_path = generate_report(enriched_entities, triage_result)
        logger.info(f"Report generated at: {report_path}")

        viz_path = generate_visualization(enriched_entities, triage_result)
        logger.info(f"Visualization generated at: {viz_path}")

        print(f"Triage Recommendation Priority: {triage_result['priority']}")
        print(f"Symptom Count: {triage_result['symptom_count']}")
        print(f"Priority Score: {triage_result['priority_score']}/10")
        print(f"Possible Conditions: {triage_result['possible_conditions']}")
        print(f"Details: {triage_result['justification']}")
        print(f"Report saved at: {report_path}")
        print(f"Visualization saved at: {viz_path}")
    else:
        print("Please provide a symptom description using --input")

if __name__ == "__main__":
    main()