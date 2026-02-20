import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def compress_travel_context(user_prompt: str, context_filepath: str = "data/travel_context.txt") -> str:
    """
    Reads the heavy travel context and uses Scaledown to compress it against the user's prompt.
    Returns the compressed prompt.
    """
    # 1. Read the heavy travel data
    try:
        with open(context_filepath, 'r') as file:
            travel_context = file.read()
    except FileNotFoundError:
        return "Error: Could not find the travel context file."

    # 2. Prepare the Scaledown API request
    url = "https://api.scaledown.xyz/compress/raw/"
    api_key = os.getenv("SCALEDOWN_API_KEY")
    
    if not api_key:
        raise ValueError("SCALEDOWN_API_KEY is missing from .env file")

    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }

    payload = {
        "context": travel_context,
        "prompt": user_prompt,
        "model": "gemini-2.5-flash",
        "scaledown": {
            "rate": "auto"
        }
    }

    # 3. Make the request and extract the compressed prompt
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            # Extract compressed prompt from the nested results object
            if "results" in result and "compressed_prompt" in result["results"]:
                compressed = result["results"]["compressed_prompt"]
            else:
                # Fallback to try different possible keys
                compressed = result.get("compressed_prompt") or result.get("compressed") or str(result)
            return compressed
        else:
            raise Exception(f"Scaledown API failed: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request error: {str(e)}")
