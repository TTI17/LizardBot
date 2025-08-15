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

def start_vote():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👍", callback_data="Yes")],
        [InlineKeyboardButton(text="👎", callback_data="NOT")],
    ])

from db import get_connection

def groups_keyboard(owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.chat_id, c.title, COUNT(u.user_id) as members_count
        FROM chats c
        LEFT JOIN users u ON c.chat_id = u.chat_id
        WHERE c.owner_id = ?
        GROUP BY c.chat_id
    """, (owner_id,))
    groups = cur.fetchall()
    conn.close()

    if not groups:
        return None

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=f"{title} ({members_count})",
                callback_data=f"group_{chat_id}"
            )]
            for chat_id, title, members_count in groups
        ]
    )