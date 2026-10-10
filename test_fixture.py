import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

class TestResponse(BaseModel):
    message: str = Field(description="A friendly greeting")

api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents='Say hello',
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=TestResponse,
            ),
        )
        print("API Test Success:", response.text)
    except Exception as e:
        print("API Test Failed:", e)
else:
    print("No GEMINI_API_KEY found, skipping live API test.")
