# handlers/start.py
from aiogram import types
from loader import dp, bot
from utils.db_api import Database

db = Database()

@dp.message_handler(commands=['start'])
async def register_user(message: types.Message):
    user_id = message.from_user.id
    if not db.user_exists(user_id):
        db.add_user(user_id)
        await bot.send_message(user_id, "Вы успешно зарегистрированы!")
    else:
        await bot.send_message(user_id, "Вы уже зарегистрированы!")
