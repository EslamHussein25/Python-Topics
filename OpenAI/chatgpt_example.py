from openai import OpenAI
import os

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    print("OPENAI_API_KEY is not set.")
    exit(1)

# Initialize the OpenAI client
openai_client = OpenAI(api_key=api_key)

def get_best_books():
    prompt = "I need the best books to read in 2024."
    agent = "You are a helpful assistant."

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": agent},
            {"role": "user", "content": prompt},
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

# Call the function and print the response
books_recommendation = get_best_books()
print(books_recommendation)
