TOKEN = "7578059970:AAH8dzPWmzmlKB7dYL5ywXvD8fsipn8_t4o"
from aiogram import Router
from aiogram.types import Message

config = Router()
@config.message()
async def chat_status(message: Message):
    return message.chat.type