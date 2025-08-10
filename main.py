import asyncio
import logging, sys
from aiogram import Bot, Dispatcher
from start import chat_router
from events import event
from dotenv import load_dotenv
import os
from aiogram.fsm.storage.memory import MemoryStorage
from db import init_db

load_dotenv()
TOKEN = os.getenv("TOKEN")
dp = Dispatcher(storage=MemoryStorage())

async def main() -> None:
    init_db()
    dp.include_router(chat_router)
    dp.include_router(event)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())