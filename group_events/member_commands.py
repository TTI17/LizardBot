from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.permission import is_member
from keyboards import get_help_keyboard

member = Router(name="memberRouter")

@member.message(Command("get_help"))
async def getHelp(message: Message):
    if not await is_member(chat_id=message.chat.id, user_id=message.from_user.id):
        await message.delete()
    
    if message.chat.type in ["group", "supergroup"]:
        await message.answer(text="help")

    else:
        await message.delete()
        await message.answer("Эта команда работает только в группе. Для получения дополнитльной информации нажмите на один из этих пунктов", reply_markup=get_help_keyboard())
        return
            
@member.message(Command("report"))
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