from aiogram.types import Message, CallbackQuery
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums.chat_member_status import ChatMemberStatus
from get_keyboards import start_vote
# from aiogram import F
from bot import bot

event = Router()

@event.message(Command("ban"))
async def ban_chat_member(message: Message):
    if not message.reply_to_message:
        await message.delete()
    else:
        await message.answer("Проводим голосование", reply_markup=start_vote())
        
@event.message(Command("unban"))
async def unban_chat_member(message:Message):
    if message.reply_to_message:
        await bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, only_if_banned=True)
    else:
        await message.delete()

@event.callback_query(lambda call: call.data == "Yes")
async def yes_ban_chat_member(call: CallbackQuery):
        await bot.ban_chat_member(chat_id=call.message.chat.id, user_id=call.message.reply_to_message.from_user.id)
        await call.message.edit_text(text="Пользователь забанен")

@event.callback_query(lambda call: call.data == "NOT")
async def no_ban_chat_member(call: CallbackQuery):
        await call.answer("Пользователь не будет забанен в результате голосования", show_alert=True)
        return

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