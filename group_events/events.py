from aiogram import Router
from aiogram.types import Message
from utils.infoChatUser import getMessagesByUser, getInfoAboutUser
from db import add_message, add_user
from utils.permission import is_member
from aiogram import F
from aiogram.types import ChatMemberUpdated
from bot import bot
from keyboards import get_rules_keyboard

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
async def joined_user(event: ChatMemberUpdated):
    if event.new_chat_member.status == "member":
        await bot.send_message(event.chat.id, 
                               text=f"Добро Пожаловать, {event.from_user.full_name} в <i>{event.chat.full_name}</i>!\n\nДля ознакомления с правилами группы введи команду /rules или нажми кнопку ниже", reply_markup=get_rules_keyboard(chat_name=event.chat.full_name))
        for admin in await bot.get_chat_administrators(event.chat.id):
            if not admin.user.is_bot:
                await bot.send_message(chat_id=admin.user.id, 
                                    text=f"Поздравляю <b>{admin.user.username}</b>\n \n В группу {event.chat.full_name} присоединился новый пользователь:\nИмя: {event.from_user.first_name}\nФамилия: {event.from_user.last_name if event.from_user.last_name != "" else "Не записана"}\nЮзернейм: @{event.from_user.username if event.from_user.username != None else "Нет юзернейма"}")

@events.chat_member()
async def left_user(event: ChatMemberUpdated):
    if event.old_chat_member.status == 'left':
        await bot.delete_message(event.chat.id, 
                                event.message.message_id)
        for admin in await bot.get_chat_administrators(event.chat.id):
            if not admin.user.is_bot:
                await bot.send_message(chat_id=admin.user.id, 
                                    text=f"Пользователь <b>{event.from_user.full_name}</b> покинул группу {event.chat.full_name}")

@events.chat_member()
async def restricted_user(event: ChatMemberUpdated):
    """ this function work with restricted users event
        need a make handler about this status
        Right now its not work and need fix left user in other branch
    """
    return

#TODO need add more comamnds for enteractions with users
