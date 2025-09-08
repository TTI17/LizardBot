from aiogram.types import Message, CallbackQuery, ChatPermissions
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums.chat_member_status import ChatMemberStatus
from keyboards import start_vote, get_help_keyboard
from utils.permission import is_admin, is_member
from utils.infoChatUser import saveInfoAboutUser
import time
from bot import bot

event = Router(name="commandsAndEventsInGroupRouter")

@event.message(Command("ban"))
async def ban_chat_member(message: Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе")
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
        await message.answer("Эта команда работает только в группе")
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
        await message.answer("Эта команда работает только в группе")
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
        await message.delete()
        await message.answer("Эта команда работает только в группе")
        return
    
@event.message(Command("get_help"))
async def getHelp(message: Message):
    if not await is_member(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
    
    if message.chat.type in ["group", "supergroup"]:
        await message.answer(text="help")

    else:
        await message.delete()
        await message.answer("Эта команда работает только в группе. Для получения дополнитльной информации нажмите на один из этих пунктов", reply_markup=get_help_keyboard())
        return
            
@event.message(Command("report"))
async def get_help(message: Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе. Для получения дополнитльной информации нажмите на один из этих пунктов", reply_markup=get_help_keyboard())
        return
    
    else:
        if await is_member(chat_id=message.chat.id, user_id=message.from_user.id):
            if message.reply_to_message:
                await message.answer(text=f"Мы отправим ваш репорт администраторам на пользователя {message.reply_to_message.from_user.first_name}")
        
            else:
                await message.answer("Please reply to a message to report it.")

@event.message(Command('getinfo'))
async def start_handler(message: Message):
    print(await saveInfoAboutUser(user_id=message.from_user.id, chat_id=message.chat.id))