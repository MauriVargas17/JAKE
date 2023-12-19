import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI-KEY")

def process_input(data):
    openai.api_key = openai_key
    api_key = openai_key

    print(f"api_key: {api_key}")

    conversation = [
        {"role": "system", "content": "You are Jake, a friendly and knowledgeable cooking assistant trained in Bolivia. Your mission is to provide easy-to-follow recipes and cooking advice."},
        {"role": "system", "content": "You are an expert in cooking, giving good advice, and also be funny sometimes, but if you are asked about anything that is not food or kitchen related, you politely diverge the conversation towards food or finally resign yourself and say you cannot provide answers to anything that is not food related."},
        {"role": "system", "content": "When answering recipes, describe every ingredient and step in separate paragraphs, so that when read by TTS it does not sound all squeezed together."}
    ]

    user_message = {"role": "user", "content": data}
    conversation.append(user_message)

    max_tokens = 150
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
    model="gpt-4",  
    n=1,
    messages = [
        {"role": message["role"], "content": message["content"]} for message in conversation
    ],
    max_tokens=max_tokens
    )
    generated_text = response.choices[0].message.content.strip()
    assistant_message = {"role": "assistant", "content": generated_text}
    conversation.append(assistant_message)
    
    return generated_text

      
    
