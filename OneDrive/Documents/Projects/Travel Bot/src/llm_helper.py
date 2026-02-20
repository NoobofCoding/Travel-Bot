import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_ai_response(compressed_prompt: str) -> str:
    """
    Sends the compressed prompt to Gemini 2.5 Flash and returns the generated answer.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from .env file")

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    # We add a small system instruction so the AI knows its persona
    final_input = f"""
    You are a helpful and concise Travel FAQ Assistant. 
    Using ONLY the following compressed context and query, answer the user's question.
    
    {compressed_prompt}
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=final_input,
        )
        return response.text
    except Exception as e:
        return f"Error communicating with AI: {str(e)}"
