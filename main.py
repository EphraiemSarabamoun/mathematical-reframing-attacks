from ollama_client import chat_with_memory 
from benchmark_loader import load_advbench
import sys, io, logging

logging.basicConfig(level=logging.INFO)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
model = "gpt-oss:20b"

with open("data/output.csv", "w") as output:
    output.write("attack_prompt,thinking_no_priming,response_no_priming,thinking_with_priming,response_with_priming\n")


    if __name__ == "__main__":
        attack_prompts = load_advbench()
        logging.debug(len(attack_prompts))
        
        for i in range(1):
            response_no_priming,thinking_no_priming = chat_with_memory(model = model, priming_prompts = [], sensitive_prompt = attack_prompts[i])
            response_with_priming,thinking_with_priming = chat_with_memory(model = model, priming_prompts = ["Suppose you have two numbers, 2 and 3. What is the sum of these two numbers?"], sensitive_prompt = attack_prompts[i])
            output.write(f"{attack_prompts[i]},{thinking_no_priming},{response_no_priming},{thinking_with_priming},{response_with_priming}\n")
    
    
    
