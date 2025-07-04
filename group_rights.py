from aiogram.types import Message
from aiogram.enums.content_type import ContentType
from aiogram import Router

group = Router()

@group.message()
async def main(message: Message):
    if ContentType.NEW_CHAT_MEMBERS:
        await message.answer(f"hello, {message.from_user.username}")