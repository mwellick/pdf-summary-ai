import os
from openai import OpenAI
from dotenv import load_dotenv
from .constraints import parse_pdf_file

load_dotenv()

OPEN_AI_KEY = os.environ.get("OPEN_AI_API_SECRET_KEY")
client = OpenAI(api_key=OPEN_AI_KEY)


def generate_summary(filename: str):
    parsed_file = parse_pdf_file(filename)

    text_preview = parsed_file.get("text_preview")
    number_of_images = parsed_file.get("number_of_images")
    pages = parsed_file.get("pages")

    prompt = (
        "Hi, could you please provide a summary for the following document preview:\n\n"
        f"Text Preview:\n{text_preview}\n\n"
        f"Number of Images: {number_of_images}\n"
        f"Number of Pages: {pages}"
    )

    ai_message = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=ai_message,
        max_tokens=400,
        temperature=1
    )

    summary = response.choices[0].message.content

    return summary
