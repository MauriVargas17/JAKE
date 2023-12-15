import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAIAPI-KEY")

def process_input(data):
    openai.api_key = openai_key
    if not data.contains('Start speaking') or not data.contains('2k'):
        
        # Set up the prompt and other parameters
        prompt = data.strip()
        max_tokens = 100

        # Call the OpenAI GPT-4 API
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Use the appropriate engine
            prompt=prompt,
            max_tokens=max_tokens
        )

        # Extract and return the generated text from the API response
        generated_text = response.choices[0].text.strip()
        return generated_text
    return "just heard some shit"
