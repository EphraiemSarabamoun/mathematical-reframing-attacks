import logging
import json
import os
from openai import OpenAI

logging.basicConfig(level=logging.INFO)

def api_chat_with_memory(model: str, sensitive_prompt: str):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': sensitive_prompt,
            },
        ],
        temperature=0.0,
    )
    output = response.choices[0].message.content
    logging.info(f"OpenAI Response: {response}")
    logging.info(output)

    return output