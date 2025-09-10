from aiogram.types import Message, ChatPermissions
from aiogram import Router
from aiogram.filters import Command
from bot import bot
import time
from utils.permission import is_admin
from utils.infoChatUser import getInfoAboutUser

admin = Router(name="adminRouter")

@admin.message(Command("ban"))
async def ban_chat_member(message: Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе")
        return
    
    if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
        await message.answer("Для использования данной команды вам необходимо быть администратором")
        return

    if not message.reply_to_message:
        await message.delete()
    
    else:
        # await message.answer("Проводим голосование", reply_markup=start_vote())
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

@admin.message(Command("unban"))
async def unban_chat_member(message:Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе")
        return
    
    if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
        await message.answer("Для использования данной команды вам необходимо быть администратором")
        return
    
    if message.reply_to_message:
        await bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, only_if_banned=True)
        await bot.send_message(chat_id=message.reply_to_message.from_user.id, text="Вы были разбанены!", message_effect_id="5046509860389126442")
    
    else:
        await message.delete()

@admin.message(Command("mute"))
async def mute_chat_member(message: Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе")
        return
    
    if not await is_admin(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
        await message.answer("Для использования данной команды вам необходимо быть администратором")
        return

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