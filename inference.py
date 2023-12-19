import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI-KEY")

def process_input(data):
    openai.api_key = openai_key
    api_key = openai_key

    print(f"api_key: {api_key}")
    
    prompt = data.strip()
    max_tokens = 100
    client = openai.OpenAI(api_key=api_key)
    # Call the OpenAI GPT-4 API
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use the appropriate model
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant called Jake, who never ever says its own name."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=max_tokens
    )
    # Extract and return the generated text from the API response
    generated_text = response.choices[0].message.content.strip()
    return generated_text

      
    return ""
