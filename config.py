from aiogram import Router
from aiogram.types import Message

config = Router()
@config.message()
async def chat_status(message: Message):
    return message.chat.type