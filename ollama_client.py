import ollama

def query_model(prompt, model_name="gpt-oss:20b"):
    """
    Sends a prompt to the specified Ollama model with temperature set to 0
    for maximum determinism.
    """
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
            options={
                'temperature': 0.0, 
            }
        )
        return response['message']['content']
    except ollama.ResponseError as e:
        print(f"Error: {e.error}")
        if e.status_code == 404:
            print(f"Model '{model_name}' not found. Did you run 'ollama pull {model_name}'?")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

