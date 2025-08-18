from aiogram.types import Message
from aiogram.enums.content_type import ContentType
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums.chat_member_status import ChatMemberStatus
from get_keyboards import start_vote
from aiogram import F as Filter

event = Router()

event.message.filter(Filter.)

@event.message(F.is_(ContentType.NEW_CHAT_MEMBERS))
async def on_new_members(message):
    for m in message.new_chat_members:
        if m.id == (await event.get_me()).id:
            # бот добавлен — вызвать функцию добавления группы
            from db import add_group  # или add_chat, как у тебя называется
            owner_id = None
            try:
                admins = await message.chat.get_administrators()
                owner = next((a.user for a in admins if a.status == "creator"), None)
                owner_id = owner.id if owner else None
            except Exception:
                pass
            add_group(message.chat.id, message.chat.title, message.chat.username, owner_id)

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
        # await message.answer("")

from aiogram import Dispatcher
from db import get_group_stats
from get_keyboards import groups_keyboard
from aiogram.types import CallbackQuery

# CallbackData для кнопок групп
group_cb = ("group", "chat_id")

async def start_handler(message: Message):
    await message.answer("Привет! Выбери действие:")

async def my_groups_handler(callback_query: CallbackQuery):
    owner_id = callback_query.from_user.id
    groups = get_owner_groups(owner_id)

    if not groups:
        await callback_query.message.answer("У тебя нет групп.")
        return

    await callback_query.message.answer("Выбери группу:", reply_markup=groups_keyboard(groups))

async def group_info_handler(callback_query: CallbackQuery, callback_data: dict):
    chat_id = int(callback_data["chat_id"])
    stats = get_group_stats(chat_id)

    if not stats:
        await callback_query.message.answer("Информация о группе не найдена.")
        return

    text = (
        f"📊 Статистика группы:\n"
        f"Название: {stats['title']}\n"
        f"ID: {stats['chat_id']}\n"
        f"Всего участников: {stats['members_count']}\n"
        f"Администраторов: {stats['admins_count']}\n"
        f"Покинули: {stats['left_count']}\n"
        f"Присоединились: {stats['joined_count']}\n"
    )
    await callback_query.message.answer(text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_callback_query_handler(my_groups_handler, text="my_groups")
    dp.register_callback_query_handler(
        group_info_handler, group_cb.filter()
    )