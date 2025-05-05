import os
import matplotlib.pyplot as plt
from datetime import datetime
from utils.logger import setup_logger

def generate_visualization(entities, triage_result):
    logger = setup_logger()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    viz_dir = "app/visualizations"
    os.makedirs(viz_dir, exist_ok=True)
    viz_path = f"{viz_dir}/triage_viz_{timestamp}.png"

    # Simple bar chart of symptom count and priority
    symptoms = entities.get("symptoms", [])
    priority = triage_result.get("priority", "unknown")
    plt.figure(figsize=(6, 4))
    plt.bar(["Symptom Count", "Priority Score"], [len(symptoms), {"emergency": 3, "urgent": 2, "non-urgent": 1, "unknown": 0}.get(priority, 0)])
    plt.title("Triage Summary")
    plt.ylabel("Value")
    plt.savefig(viz_path)
    plt.close()

    logger.info(f"Visualization generated at: {viz_path}")
    return viz_path