from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from get_texts import*
from get_keyboards import *
# from make_info_to_json import tracking

chat_router = Router()
crt = chat_router

@crt.message(CommandStart())
async def start(message: Message):
    await message.answer(text=start_text)

@crt.message(Command("help"))
async def handleHelp(message: Message):
    await message.answer(text=help_text, reply_markup=get_help_keyboard())

@crt.callback_query(lambda call: call.data == "/faq")
async def get_help_by_authors(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=faq_text, reply_markup=get_faq_help())
    
@crt.callback_query(lambda call: call.data == "add")
async def handleAdd(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=add_text, reply_markup=get_invite_keyboard())

@crt.callback_query(lambda call: call.data == "about_us")
async def handleAboutUs(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=about_us_text, reply_markup=get_about_us_keyboard())

@crt.callback_query(lambda call: call.data == "back_to_help")
async def handleBackToHelp(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=help_text, reply_markup=get_help_keyboard())

@crt.callback_query(lambda call: call.data == "groups")
async def handleGroups(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text=f"Группы в которые вы меня добавили:\nПока что эта функция на стадии разработки", reply_markup=get_user_groups())