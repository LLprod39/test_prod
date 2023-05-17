# handlers/upload_project.py
from aiogram import types
from loader import dp, bot
from utils.db_api import Database
from utils.project_manager import ProjectManager

db = Database()
pm = ProjectManager()

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def upload_project(message: types.Message):
    user_id = message.from_user.id
    project_name = db.get_active_project(user_id)  # Допустим, у нас есть функция, которая возвращает активный проект пользователя
    if project_name:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id)
        await bot.download_file(file_info.file_path, f"projects/{project_name}/{message.document.file_name}")
        await bot.send_message(user_id, "Файл успешно загружен!")
    else:
        await bot.send_message(user_id, "У вас нет активных проектов!")
