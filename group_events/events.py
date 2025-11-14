from aiogram import Router
from aiogram.types import Message
from utils.infoChatUser import getMessagesByUser, getInfoAboutUser
from db import add_message, add_user
from utils.permission import is_member
from aiogram import F
from aiogram.types import ChatMemberUpdated
from bot import bot

events = Router(name="groupEvents")

@events.message()
async def getMessage(message:Message):
    if message.chat.type in ["group", "supergroup"]:
        await getMessagesByUser(chat_id=message.chat.id, 
                                user_id=message.from_user.id, 
                                message_text=message.text)
        
        add_message(chat_id=message.chat.id, 
                    user_id=message.from_user.id, 
                    text=message.text, 
                    username=message.from_user.username, 
                    chat_title=message.chat.title)
    else:
        return
  
@events.message(F.text)
async def getUser(message:Message):
    if message.chat.type in ["group", "supergroup"]:
        await add_user(getInfoAboutUser(chat_id=message.chat.id, 
                            user_id=message.from_user.id))
    else:
        return

@events.chat_member()
async def joinedUser(event: ChatMemberUpdated):
    if event.new_chat_member.status == "member":
        await bot.send_message(event.chat.id, 
                               text=f"Welcome, {event.from_user.full_name}!")
        for admin in await bot.get_chat_administrators(event.chat.id):
            if admin.status != "bot":
                await bot.send_message(admin.user.id, 
                                    text=f"New user in {event.chat.full_name}: @{event.from_user.first_name}")

@events.chat_member()
async def leftUser(event: ChatMemberUpdated):
    if event.old_chat_member.status == "member":
        for admin in await bot.get_chat_administrators(event.chat.id):
            if admin.status != "bot":
                await bot.send_message(admin.user.id, 
                                    text=f"User left {event.chat.full_name}: @{event.from_user.first_name}")

#TODO need add more comamnds for enteractions with users
