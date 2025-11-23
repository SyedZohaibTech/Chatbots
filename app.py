import os
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai

# Load .env file
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

@cl.on_message
async def main(message: cl.Message):
    try:
        response = model.generate_content(message.content)
        await cl.Message(content=response.text).send()
    except Exception as e:
        await cl.Message(content=f"❌ Gemini Error: {e}").send()
