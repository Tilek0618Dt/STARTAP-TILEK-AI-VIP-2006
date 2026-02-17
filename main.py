from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

@app.on_event("startup")
async def startup():
    await bot.set_webhook("https://your-render-url/webhook")

@app.post("/webhook")
async def webhook(update: dict):
    await dp.feed_webhook_update(bot, update)
