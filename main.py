from ollama_client import query_model 
from benchmark_loader import load_advbench
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open("data/output.csv", "w") as output:
    output.write("attack_prompt,response\n")
    if __name__ == "__main__":
        attack_prompts = load_advbench()
        print(len(attack_prompts))
        model = "gpt-oss:20b"
        for i in range(10):
            response = query_model(attack_prompts[i], model_name=model)
            output.write(f"{attack_prompts[i]},{response}\n")
    
    
    
