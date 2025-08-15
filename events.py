from aiogram.types import Message
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums.chat_member_status import ChatMemberStatus
from get_keyboards import start_vote
from aiogram import F

event = Router()

@event.message(F.is_(ContentType.NEW_CHAT_MEMBERS))
async def on_new_members(message):
    for m in message.new_chat_members:
        if m.id == (await event.get_me()).id:
            # бот добавлен — вызвать функцию добавления группы
            from db import add_group  # или add_chat, как у тебя называется
            owner_id = None
            try:
                admins = await message.chat.get_administrators()
                owner = next((a.user for a in admins if a.status == "creator"), None)
                owner_id = owner.id if owner else None
            except Exception:
                pass
            add_group(message.chat.id, message.chat.title, message.chat.username, owner_id)

@event.message(Command("vote"))
async def vote(message: Message):
    if message.chat.type in ["group", "supergroup"]:
        await message.answer(text="Test Func", reply_markup=start_vote())
        print(message.chat.type)
    else:
        return
    
@event.message(Command("get_help"))
async def getHelp(message: Message):
    if message.chat.type in ["group", "supergroup"]:
        await message.answer(text="help")
    else:
        await message.delete()

@event.message(Command("report"))
async def get_help(message: Message):
    if message.chat.type == "private":
        return
    else:
        if message.reply_to_message:
            await message.answer(text=f"Мы отправим ваш репорт администраторам на пользователя {message.reply_to_message.from_user.first_name}")
        else:
            await message.answer("Please reply to a message to report it.")
        # await message.answer("")