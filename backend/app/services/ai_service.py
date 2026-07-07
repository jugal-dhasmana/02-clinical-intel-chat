from openai import OpenAI
import os
import json


def generate_therapy_response(question: str, therapy_data: dict):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = """
    You are a clinical therapy intelligence assistant.

    Use ONLY the curated therapy data provided.
    Do not invent facts.
    If information is missing, say the curated therapy data does not contain enough detail.
    Do not provide medical advice or treatment recommendations.
    Keep responses professional, concise, and clinically grounded.
    """

    user_prompt = f"""
    USER QUESTION:
    {question}

    CURATED THERAPY DATA:
    {json.dumps(therapy_data, indent=2, default=str)}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_output_tokens=500
    )

    return response.output_text