import os
import requests
import base64
from env import API_KEY, API_ENDPOINT
def get_response(endpoint):
        # Configuration

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    # Payload for the request
    payload = {
    "messages": [
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": endpoint
            }
        ]
        }
    ],
    "temperature": 0.1,
    "top_p": 0.95,
    "max_tokens": 2000
    }


    # Send request
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response as needed (e.g., print or process)
    answer = response.json()["choices"][0]["message"]["content"]
    return answer