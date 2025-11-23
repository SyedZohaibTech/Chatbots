import chainlit as cl
import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AIzaSyC06Izwiyw977s41OyNxm9ZGjDJxVSc_ZM")

# Correct model name and syntax
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")


@cl.on_message
async def main(message: cl.Message):
    try:
        response = model.generate_content(message.content)
        await cl.Message(content=response.text).send()
    except Exception as e:
        await cl.Message(content=f"❌ Gemini Error: {e}").send()
