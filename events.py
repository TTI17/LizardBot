from aiogram.types import Message
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram import F
from aiogram.enums.chat_member_status import ChatMemberStatus
from get_keyboards import start_vote
from config import chat_status

event = Router()


@event.message()
async def join_chat_member(message: Message):
    if chat_status(message) == "group":
        print("woeifjwoeifj")
        if ContentType.NEW_CHAT_MEMBERS:
            await message.answer(f"Привет, {message.from_user.username}")

@event.message()
async def left_chat_member(message: Message):
    if chat_status(message) == "group":
        if ContentType.LEFT_CHAT_MEMBER:
            await message.answer(f"Пользователь {message.from_user.username} покинул группу")

@event.message(Command("vote"))
async def main(message: Message):
    if chat_status(message) == "group":
        await message.answer(reply_markup=start_vote())