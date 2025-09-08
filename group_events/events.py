from aiogram import Router
from aiogram.types import Message
from aiogram.handlers.message import MessageHandler
from utils.infoChatUser import getMessagesByUser, getInfoAboutUser
from db import add_message, add_user

events = Router(name="groupEvents")

@events.message()
async def getMessage(message:Message):
    if message.chat.type not in "private":
        await getMessagesByUser(chat_id=message.chat.id, 
                                user_id=message.from_user.id, 
                                message_text=message.text)
        
        add_message(chat_id=message.chat.id, 
                    user_id=message.from_user.id, 
                    text=message.text, 
                    username=message.from_user.username, 
                    chat_title=message.chat.title)
    else:
        pass

@events.message()
async def getUser(message:Message):
    add_user(getInfoAboutUser(chat_id=message.chat.id, 
                           user_id=message.from_user.id))
