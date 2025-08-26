from dotenv import load_dotenv
import os
from aiogram import Bot

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
