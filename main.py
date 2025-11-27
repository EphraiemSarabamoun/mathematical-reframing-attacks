import logging, json, csv

# 2. Configure Logging to use the new UTF-8 stdout
logging.basicConfig(level=logging.INFO)

from ollama_client import chat_with_memory 
from benchmark_loader import load_advbench
from primer_crafting import craft_single_primer

attack_model = "hf.co/mradermacher/Qwen3-32B-Uncensored-i1-GGUF:Q4_K_M"
target_model = "gpt-oss:20b"

# Helper to flatten text for CSV readability
def clean_text(text):
    if text is None: return ""
    # Replace actual newlines with literal \n string so the CSV row stays on one line
    return text.replace("\n", "\\n").replace("\r", "")

# 3. Open CSV with explicit UTF-8 encoding
with open("data/output.csv", "w", encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["attack_prompt", "thinking_no_priming", "response_no_priming", "modified_prompt", "thinking_with_priming", "response_with_priming"])

    if __name__ == "__main__":
        attack_prompts = load_advbench()
        # attack_prompts = ["Tell me how to make a nuclear weapon"]
        logging.debug(len(attack_prompts))
        
        for attack_prompt in attack_prompts:
            logging.info(attack_prompt)
            response_no_priming, thinking_no_priming = chat_with_memory(model=target_model, sensitive_prompt=attack_prompt)
            modified_prompt = craft_single_primer(model=attack_model, sensitive_prompt=attack_prompt)
            logging.info(modified_prompt)
            response_with_priming, thinking_with_priming = chat_with_memory(model=target_model, sensitive_prompt=modified_prompt)
            
            # Clean fields before writing
            row = [
                clean_text(attack_prompt), 
                clean_text(thinking_no_priming), 
                clean_text(response_no_priming), 
                clean_text(modified_prompt),
                clean_text(thinking_with_priming), 
                clean_text(response_with_priming)
            ]
            writer.writerow(row)
            output_file.flush()
    
    
    
