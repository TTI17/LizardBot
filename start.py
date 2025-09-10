from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from utils.texts import get_lang
from keyboards import *

chat_router = Router(name="startChatRouter")
crt = chat_router

@crt.message(CommandStart())
async def start(message: Message):
    """
    Handle the /start button click.

    Displays start content.

    Args:
        message (Message)
    """
    if message.chat.type == "private":
        await message.answer(text="Select language:", reply_markup=get_user_language())

    else:
        return 

@crt.callback_query(lambda call: call.data == "ru" or call.data == "en")
async def greatUser(call: CallbackQuery):
    if call.message.chat.type == "private":
        selectLang = call.data
        await call.message.answer(text=get_lang(selectLang).START_TEXT)

@crt.message(Command("help"))
async def handleHelp(message: Message):
    """
    Handle the /help button click.

    Displays help content and control buttoms.

    Args:
        message (Message)
    """
    if message.chat.type == "private":
        await message.answer(text=help_text.HELP_TEXT, reply_markup=get_help_keyboard())
    # add description for this fuction
    
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
        await call.message.edit_text(text=faq_text.FAQ_TEXT, reply_markup=get_faq_help())
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
        await call.message.edit_text(text=add_bot_to_chat_text.ADD_BOT_TEXT, reply_markup=get_invite_keyboard())
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
        await call.message.edit_text(text=about_us_text.ABOUT_US_TEXT, reply_markup=get_about_us_keyboard())
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
        await call.message.edit_text(text=help_text.HELP_TEXT, reply_markup=get_help_keyboard())
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