import aiohttp
import hashlib
import base64
from config import CRYPTOMUS_API_KEY, CRYPTOMUS_MERCHANT_ID

async def create_invoice(amount, order_id):

    url = "https://api.cryptomus.com/v1/payment"

    payload = {
        "amount": str(amount),
        "currency": "USD",
        "order_id": order_id
    }

    sign = hashlib.md5(
        base64.b64encode(str(payload).encode()) +
        CRYPTOMUS_API_KEY.encode()
    ).hexdigest()

    headers = {
        "merchant": CRYPTOMUS_MERCHANT_ID,
        "sign": sign,
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            return await resp.json()
