from aiogram.types import Message, CallbackQuery, ChatPermissions
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums.chat_member_status import ChatMemberStatus
from get_keyboards import start_vote
from utils.permission import is_admin
import time
from bot import bot

event = Router()

@event.message(Command("ban"))
async def ban_chat_member(message: Message):
    if message.chat.type == "private":
        await message.delete()
        return
    
    if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
    
    if not message.reply_to_message:
        await message.delete()
    
    else:
        # await message.answer("Проводим голосование", reply_markup=start_vote())
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        
@event.message(Command("unban"))
async def unban_chat_member(message:Message):
    if message.chat.type == "private":
        await message.delete()
        return
    
    if message.reply_to_message:
        await bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, only_if_banned=True)
        await bot.send_message(chat_id=message.reply_to_message.from_user.id, text="Вы были разбанены!")
    
    else:
        await message.delete()
        
@event.message(Command("mute"))
async def mute_chat_member(message: Message):
    if message.chat.type == "private":
        await message.delete()
        return
    if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()

    if message.reply_to_message:
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
            ),
            until_date=time.time() + 60 * 10,
        )
        await message.answer(text=f"Пользователь:<i>{message.reply_to_message.from_user.username}</i> замучен на 10 минут")

@event.message(Command("vote"))
async def vote(message: Message):
    if message.chat.type in ["group", "supergroup"]:
        if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
            await message.delete()

        await message.answer(text="Test Func", reply_markup=start_vote())
    
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