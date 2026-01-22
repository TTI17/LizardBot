from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message

def get_help_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить бота в группу",callback_data="add_to_group")],
        [InlineKeyboardButton(text="Ваши группы",callback_data="groups")],
        [InlineKeyboardButton(text="FAQ", callback_data="faq")]])

def get_invite_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить 🦎 ረፗጓልዩሏ в группу", url="http://t.me/Iizard_bot?startgroup=botstart")],
        [InlineKeyboardButton(text="🔙 Вернуться в меню", callback_data="back_to_help")]])


def get_user_groups():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в меню", callback_data="back_to_help")]])

# FAQ KEYBOARD

def get_faq_help():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доступные команды", callback_data="current_comms")],
        [InlineKeyboardButton(text="О нас и нашем проекте",callback_data="about_us")],
        [InlineKeyboardButton(text="🔙 Вернуться в меню", callback_data="back_to_help")]
        ])

def get_current_comms():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Команды администратора", callback_data="admin_comms")],
        [InlineKeyboardButton(text="Команды пользователя", callback_data="user_comms")],
        [InlineKeyboardButton(text="🔙 Вернуться в FAQ", callback_data="get_faq_help")]
    ])

def get_admin_comms():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="get_current_comms")]
    ])

def get_user_comms():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="get_current_comms")]
    ])
    
def get_about_us_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="get_current_comms")]
        ])
#
def start_vote():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👍", callback_data="Yes")],
        [InlineKeyboardButton(text="👎", callback_data="NOT")],
    ])

def get_user_language():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇸 EN", callback_data="en")],
        [InlineKeyboardButton(text="🇷🇺 RU", callback_data="ru")]
    ])

def get_rules_keyboard(chat_name:str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Правила {chat_name}", callback_data="rules")],
    ])