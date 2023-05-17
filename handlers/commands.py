from aiogram import types
from loader import dp

# Затем добавьте обработчики команд
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Обработка команды /start
    pass
