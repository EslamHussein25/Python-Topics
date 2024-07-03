from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    print("OPENAI_API_KEY is not set.")

openai_client = OpenAI(api_key=api_key)

def process_gpt_3_5_turbo(text, agent):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=
        [
            {"role": "system", "content": agent},
            {"role": "user", "content": text},
        ],
        temperature=0.5,
        n=1,
        stop=None,
    )
    try:
        completion_text = response.choices[0].message.content
    except KeyError:
        completion_text = "Error processing completion."
    return completion_text

