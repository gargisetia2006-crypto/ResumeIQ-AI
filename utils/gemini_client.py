import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)