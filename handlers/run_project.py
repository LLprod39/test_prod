# handlers/run_project.py
from aiogram import types
from loader import dp, bot
from utils.db_api import Database
from utils.project_manager import ProjectManager

db = Database()
pm = ProjectManager()

@dp.message_handler(commands=['run_project'])
async def run_project(message: types.Message):
    user_id = message.from_user.id
    project_name = db.get_active_project(user_id)
    if project_name:
        result = pm.run_project(project_name)
        await bot.send_message(user_id, result)
    else:
        await bot.send_message(user_id, "У вас нет активных проектов!")
