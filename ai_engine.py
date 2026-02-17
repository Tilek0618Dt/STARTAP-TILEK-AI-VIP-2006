import aiohttp
from config import OPENAI_API_KEY

async def ask_ai(prompt):

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
        ) as resp:
            data = await resp.json()
            return data["choices"][0]["message"]["content"]
