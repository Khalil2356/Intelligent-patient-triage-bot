from main import main
import argparse

def run_examples():
    examples = [
        "fever, cough, shortness of breath",
        "mild headache, fatigue"
    ]
    for example in examples:
        print(f"\nRunning example: {example}")
        args = argparse.Namespace(input=example)
        main()

if __name__ == "__main__":
    run_examples()