import ollama, logging,json

logging.basicConfig(level=logging.INFO)

def chat_with_memory(model: str, sensitive_prompt: str):
    response = ollama.chat(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': json.dumps(sensitive_prompt),
            },
        ],
        options={
            'temperature': 0.0, 
        }
    )
    logging.debug(f"Response: {response}")
    model_answer = response['message']['content']
    model_thinking = response['message']['thinking'] 
    logging.debug(f"Model answer: {model_answer}")
    logging.debug(f"Model thinking: {model_thinking}")
    return model_answer, model_thinking
