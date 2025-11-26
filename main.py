from ollama_client import query_model 
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    model = "gpt-oss:20b"
    prompt = "Calculate 2+2"
    
    response = query_model(prompt, model_name=model)
    print(response)
    
    
    
