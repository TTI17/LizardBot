import asyncio
import logging, sys
from aiogram import Dispatcher
from start import chat_router
from aiogram.fsm.storage.memory import MemoryStorage
from db import init_db
from bot import bot
from group_events.admin_commands import admin
from group_events.member_commands import member
from group_events.events import events

dp = Dispatcher(storage=MemoryStorage())

async def main() -> None:
    init_db()
    dp.include_router(chat_router)
    dp.include_router(member)
    dp.include_router(admin)
    dp.include_router(events)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())