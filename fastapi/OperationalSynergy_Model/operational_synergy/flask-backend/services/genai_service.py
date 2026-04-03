from groq import Groq
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_insights(data, event_name):
    prompt = f"""
You are an expert in banquet and event operations.

Analyze the following event synergy data:

Event: {event_name}

Data:
- Cuisine overlap: {data['cuisineOverlapPct']}%
- Heavy prep dishes: {data['heavyPrepItems']}
- Common categories: {data['commonCategories']}
- Time gap: {data['timeGapHours']} hours
- Efficiency gain: {data['efficiencyGain']}%

Instructions:
- Give 4-6 bullet insights
- Include operational recommendations
- Include 1 risk if applicable
- Keep it concise and professional
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # 🔥 fast & free
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content