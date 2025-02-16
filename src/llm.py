import openai
import os
from dotenv import load_dotenv
import pytesseract
from PIL import Image

load_dotenv()
API_KEY = os.getenv("AIPROXY_TOKEN")

def extract_email(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Extract the sender's email address."},
                  {"role": "user", "content": text}],
        api_key=API_KEY
    )
    return response["choices"][0]["message"]["content"].strip()

def extract_text_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)
