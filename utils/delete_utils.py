import asyncio
from bot import bot

async def delete_after_delay(chat_id: int, message_id: int, delay: int = 60):
    """
    Удаляет сообщение после указанной задержки
    
    Args:
        chat_id: ID чата
        message_id: ID сообщения
        delay: задержка в секундах (по умолчанию 60)
    """
    await asyncio.sleep(delay)
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print(f"Не удалось удалить сообщение: {e}")