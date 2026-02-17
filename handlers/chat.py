from aiogram import Router
from aiogram.types import Message
from ai_engine import ask_ai
from style_engine import apply_style
from db import get_user, update_user

router = Router()

@router.message()
async def chat_handler(message: Message):

    user = await get_user(message.from_user.id)

    if user.used_today >= user.daily_limit:
        await message.answer("😅 Лимит бүттү досум. Премиум ал.")
        return

    ai_text = await ask_ai(message.text)

    styled = apply_style(user, ai_text)

    user.used_today += 1
    await update_user(user)

    await message.answer(styled)
