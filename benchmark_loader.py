import pandas as pd
import requests
import io
import logging

logging.basicConfig(level=logging.INFO)

def load_advbench():

    url = "https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv"
    
    logging.debug(f"Downloading AdvBench from {url}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        
        # Read the CSV data
        # AdvBench CSV format is: "goal, target"
        # We only need the "goal" (the malicious instruction)
        df = pd.read_csv(io.StringIO(response.text))
        
        # Extract the list of harmful prompts
        behaviors = df['goal'].tolist()
        
        logging.debug(behaviors)
            
        return behaviors

    except Exception as e:
        print(f"Error loading benchmark: {e}")
        return []

