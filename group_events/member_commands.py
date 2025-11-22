from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from utils.permission import is_member
from keyboards import get_help_keyboard, get_rules_keyboard
from bot import bot
from utils.delete_utils import delete_after_delay
import asyncio

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
async def send_report(message: Message):
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

@member.message(Command("rules"))
async def get_rules(message: Message):
    if message.chat.type == "private":
        await message.delete()
        await message.answer("Эта команда работает только в группе. Для получения дополнитльной информации нажмите на один из этих пунктов", reply_markup=get_help_keyboard())
        return
    
    else:
        try:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id-1, text="Данные правила были созданы владельцем данной группы.\n\nРазработчик бота не несет ответственности за написанное в данных правилах.\n\nПРАВИЛА:\nНа данный момент данная функция разрабатвается")
            asyncio.create_task(delete_after_delay(chat_id=message.chat.id,
                                                   message_id=message.message_id-1))
        except Exception as e:
            await message.answer(text="Данные правила были созданы владельцем данной группы.\n\nРазработчик бота не несет ответственности за написанное в данных правилах.\n\nПРАВИЛА:\nНа данный момент данная функция разрабатвается")
            asyncio.create_task(delete_after_delay(chat_id=message.chat.id,
                                                   message_id=message.message_id-1))

@member.callback_query(lambda call: call.data == "rules")
async def get_rules_callback(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Данные правила были созданы владельцем данной группы.\n\nРазработчик бота не несет ответственности за написанное в данных правилах.\n\nПРАВИЛА:\nНа данный момент данная функция разрабатвается")
    asyncio.create_task(delete_after_delay(chat_id=call.message.chat.id, message_id=call.message.message_id))