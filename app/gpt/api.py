import os

import requests
from dotenv import load_dotenv


load_dotenv()
GPT_API_KEY = os.getenv("GPT_API_KEY")


def query_gpt(prompt, max_tokens=50):
    headers = {
        "Authorization": f"Bearer {GPT_API_KEY}",
        "Content-Type": "application/json",
    }

    json_data = {"prompt": prompt, "max_tokens": max_tokens}

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers=headers,
        json=json_data,
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        raise Exception(f"Error in GPT API call: {response.text}")


prompt = "How are you?"
try:
    gpt_response = query_gpt(prompt)
    print(gpt_response)
except Exception as e:
    print(e)
