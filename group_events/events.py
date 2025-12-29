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

# @events.message()
# async def getMessage(message:Message):
#     if message.chat.type in ["group", "supergroup"]:
#         await getMessagesByUser(chat_id=message.chat.id, 
#                                 user_id=message.from_user.id, 
#                                 message_text=message.text)
        
#         add_message(chat_id=message.chat.id, 
#                     user_id=message.from_user.id, 
#                     text=message.text, 
#                     username=message.from_user.username, 
#                     chat_title=message.chat.title)
#     else:
#         return
  
# @events.message(F.text)
# async def getUser(message:Message):
#     if message.chat.type in ["group", "supergroup"]:
#         await add_user(getInfoAboutUser(chat_id=message.chat.id, 
#                             user_id=message.from_user.id))
#     else:
#         return

@events.chat_member()
async def handle_chat_member_update(event: ChatMemberUpdated):
    """
    Centralized handler for all chat member updates.
    Processes member joins, leaves, and status changes.
    """
    # Handle new member joins
    if event.new_chat_member.status == "member" and event.old_chat_member.status != "member":
        await handle_new_member(event)
    
    # Handle member leaves
    elif event.new_chat_member.status == "left" and event.old_chat_member.status == "member":
        await handle_member_left(event)
    
    # Handle member restrictions
    elif event.new_chat_member.status == "restricted" and event.old_chat_member.status != "restricted":
        await handle_member_restricted(event)

async def handle_new_member(event: ChatMemberUpdated):
    """Handle when a new member joins the group"""
    try:
        # Send welcome message to the group
        await bot.send_message(
            event.chat.id,
            text=f"Добро Пожаловать, {event.from_user.full_name} в <i>{event.chat.full_name}</i>!\n\nДля ознакомления с правилами группы введи команду /rules или нажми кнопку ниже",
            reply_markup=get_rules_keyboard(chat_name=event.chat.full_name)
        )
        
        # Notify administrators
        await notify_admins_about_new_member(event)
        
    except Exception as e:
        print(f"Error handling new member: {e}")

async def handle_member_left(event: ChatMemberUpdated):
    """Handle when a member leaves the group"""
    try:
        # Notify administrators about member leaving
        await notify_admins_about_left_member(event)
        
    except Exception as e:
        print(f"Error handling member left: {e}")

async def handle_member_restricted(event: ChatMemberUpdated):
    """Handle when a member gets restricted"""
    # TODO: Implement restriction handling
    pass

async def notify_admins_about_new_member(event: ChatMemberUpdated):
    """Send notification to admins when a new member joins"""
    try:
        for admin in await bot.get_chat_administrators(event.chat.id):
            if not admin.user.is_bot:
                await bot.send_message(
                    chat_id=admin.user.id,
                    text=f"Поздравляю <b>{admin.user.username}</b>\n \n В группу {event.chat.full_name} присоединился новый пользователь:\nИмя: {event.from_user.first_name}\nФамилия: {event.from_user.last_name if event.from_user.last_name else 'Не записана'}\nЮзернейм: @{event.from_user.username if event.from_user.username else 'Нет юзернейма'}"
                )
    except Exception as e:
        print(f"Error notifying admins about new member: {e}")

async def notify_admins_about_left_member(event: ChatMemberUpdated):
    """Send notification to admins when a member leaves"""
    try:
        for admin in await bot.get_chat_administrators(event.chat.id):
            if not admin.user.is_bot:
                await bot.send_message(
                    chat_id=admin.user.id,
                    text=f"Пользователь <b>{event.from_user.full_name}</b> покинул группу {event.chat.full_name}"
                )
    except Exception as e:
        print(f"Error notifying admins about left member: {e}")

#TODO need add more comamnds for enteractions with users
