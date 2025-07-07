from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def get_help_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить бота в группу",callback_data="add")],
        [InlineKeyboardButton(text="О нас и нашем проекте",callback_data="about_us")],
        [InlineKeyboardButton(text="Ваши группы",callback_data="groups")],
        [InlineKeyboardButton(text="FAQ", callback_data="/faq")]])

def get_invite_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить 🦎 ረፗጓልዩሏ в группу", url="http://t.me/Iizard_bot?startgroup=botstart")],
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="back_to_help")]])

def get_about_us_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="back_to_help")]])

def get_user_groups():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="back_to_help")]])

def get_faq_help():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Вернуться в список", callback_data="back_to_help")]])