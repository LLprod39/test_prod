import logging
import sys
sys.path.append('.')

from aiogram import executor
from loader import dp
import handlers  # импортируем handlers чтобы они зарегистрировались в dp

# Включаем логирование
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Запускаем диспетчер для обработки событий
    executor.start_polling(dp, skip_updates=True)
