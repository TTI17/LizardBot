import asyncio
import logging, sys
from aiogram import Dispatcher
from start import chat_router
from group_events import event
from aiogram.fsm.storage.memory import MemoryStorage
from db import init_db
from bot import bot

dp = Dispatcher(storage=MemoryStorage())

async def main() -> None:
    init_db()
    dp.include_router(chat_router)
    dp.include_router(event)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())