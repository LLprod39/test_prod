# handlers/new_project.py
from aiogram import types
from loader import dp, bot
from utils.db_api import Database
from utils.project_manager import ProjectManager

db = Database()
pm = ProjectManager()

@dp.message_handler(commands=['new_project'])
async def new_project(message: types.Message):
    user_id = message.from_user.id
    project_name = message.text.split()[1]  # Получаем имя проекта из сообщения
    if db.can_create_project(user_id):  # Проверяем, может ли пользователь создать новый проект
        db.create_project(user_id, project_name)  # Создаем запись в базе данных
        pm.create_project_folder(project_name)  # Создаем папку для проекта
        pm.create_venv(project_name)  # Создаем виртуальное окружение
        await bot.send_message(user_id, "Проект успешно создан!")
    else:
        await bot.send_message(user_id, "Вы не можете создать больше проектов!")
