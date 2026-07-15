from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
class Product(BaseModel):
    description: str
@app.post("/analyze")
async def analyze_product(product: Product):
    prompt = f"""
    Analyze the following product description.
    Product Description:
    {product.description}
    Give the output in this format:
    1. Product Summary
    2. Sentiment (Positive/Negative/Neutral)
    3. Key Features
    4. Pros
    5. Cons
    6. Target Audience
    7. SEO Keywords
    8. Overall Rating (/10)
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return {
        "analysis": response.text
    }