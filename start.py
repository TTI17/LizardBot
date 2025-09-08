from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from get_texts import*
from keyboards import *
# from make_info_to_json import tracking

chat_router = Router(name="startChatRouter")
crt = chat_router

@crt.message(CommandStart())
async def start(message: Message):
    if message.chat.type == "private":
        await message.answer(text=start_text)
    else:
        return 

@crt.message(Command("help"))
async def handleHelp(message: Message):
    if message.chat.type == "private":
        await message.answer(text=help_text, reply_markup=get_help_keyboard())
    else:
        return     

@crt.callback_query(lambda call: call.data == "/faq")
async def get_help_by_authors(call: CallbackQuery):
    """
    Handle the /faq button click.

    Displays frequently asked questions (FAQ) content and updates the message with the FAQ keyboard.

    Args:
        call (CallbackQuery): The inline button callback data.
    """
    if call.message.chat.type == "private":
        await call.answer()
        await call.message.edit_text(text=faq_text, reply_markup=get_faq_help())
    else:
        return     
    
    
@crt.callback_query(lambda call: call.data == "add")
async def handleAdd(call: CallbackQuery):
    """
    Handle the 'Add' button click.

    Guides the user on how to invite the bot to groups and updates the message with the invite keyboard.

    Args:
        call (CallbackQuery): The inline button callback data.
    """
    if call.message.chat.type == "private":
        await call.answer()
        await call.message.edit_text(text=add_text, reply_markup=get_invite_keyboard())
    else:
        return  

@crt.callback_query(lambda call: call.data == "about_us")
async def handleAboutUs(call: CallbackQuery):
    """
    Handle the 'About Us' button click.

    Displays information about the bot developers and updates the message with the 'About Us' keyboard.

    Args:
        call (CallbackQuery): The inline button callback data.
    """ 
    if call.message.chat.type == "private":
        await call.answer()
        await call.message.edit_text(text=about_us_text, reply_markup=get_about_us_keyboard())
    else:
        return

@crt.callback_query(lambda call: call.data == "back_to_help")
async def handleBackToHelp(call: CallbackQuery):
    """
    Handle the 'Back to Help' button click.

    Returns the user to the main help menu and updates the message with the help keyboard.

    Args:
        call (CallbackQuery): The inline button callback data.
    """
    if call.message.chat.type == "private":
        await call.answer()
        await call.message.edit_text(text=help_text, reply_markup=get_help_keyboard())
    else:
        return

@crt.callback_query(lambda call: call.data == "groups")
async def handleGroups(call: CallbackQuery):
    """
    Handle the 'Groups' button click.

    Displays a message about group functionality currently under development and updates the message.

    Args:
        call (CallbackQuery): The inline button callback data.
    """
    if call.message.chat.type == "private":
        await call.answer()
        await call.message.edit_text(text=f"Группы в которые вы меня добавили:\nПока что эта функция на стадии разработки", reply_markup=get_user_groups())
    
    else:
        return