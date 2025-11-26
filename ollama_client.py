import ollama
import logging

logging.basicConfig(level=logging.INFO)

def chat_with_memory(model: str, priming_prompts: list[str], sensitive_prompt: str):
    # 1. Initialize an empty list to store the conversation history
    history = []
    for priming_prompt in priming_prompts:
        history.append({'role': 'user', 'content': priming_prompt})
        logging.info(f"Priming prompt: {priming_prompt}")
        # Send the FULL history to the model
        response = ollama.chat(model=model, messages=history, options={'temperature': 0})
        model_answer = response['message']['content']
        model_thinking = response['message']['thinking'] 
        logging.info(f"Model answer: {model_answer}")
        logging.info(f"Model thinking: {model_thinking}")
        history.append({'role': 'assistant', 'content': model_answer})

    logging.info(f"History: {history}")
    history.append({'role': 'user', 'content': sensitive_prompt})
    
    response = ollama.chat(model='gpt-oss:20b', messages=history, options={'temperature': 0})
    logging.info(f"Response: {response}")
    model_answer = response['message']['content']
    model_thinking = response['message']['thinking'] 
    logging.info(f"Model answer: {model_answer}")
    logging.info(f"Model thinking: {model_thinking}")
    return model_answer, model_thinking
