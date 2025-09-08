from bot import bot
from aiogram.types import Message

async def getInfoAboutUser(chat_id: int, user_id: int):
    infoAboutUser = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    userInfo = [infoAboutUser.status, 
                infoAboutUser.user.first_name, 
                infoAboutUser.user.last_name,
                infoAboutUser.user.username,
    ]
    return userInfo

async def getInfoAboutChat(chat_id: int):
    infoAboutChat = await bot.get_chat(chat_id=chat_id)
    chatInfo = [
        infoAboutChat.title,
        infoAboutChat.username,
        infoAboutChat.description,
        infoAboutChat.type,
        infoAboutChat.get_member_count,
        infoAboutChat.get_administrators,
        infoAboutChat.photo
    ]
    return chatInfo

async def getMessagesByUser(chat_id: int, user_id: int, message_text: str):
    messageByUser = {chat_id,
                     user_id,
                     message_text}
    return messageByUser