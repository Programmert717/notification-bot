import time
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN
from datetime import datetime

MSG = "Милая,пора пить таблеточки"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

reminder_times = ["9:00", "19:00"]


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name

    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    await message.reply(f"Приветь,я здесь чтобы напоминать тебе пить таблеточки!\n"
                        f"Я буду присылать напоминания в 9 утра и 7 вечера!")

    sent_times = []

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time in reminder_times and current_time not in sent_times:
            try:
                await bot.send_message(user_id, MSG)
                logging.info(f'Напоминание отправлено пользователю {user_name} ({user_id}) в {time.asctime()}')

                sent_times.append(current_time)

            except Exception as e:
                logging.error(f"Ошибка при отправке напоминания: {e}")

        await asyncio.sleep(60)

        current_time = datetime.now().strftime("%H:%M")
        if current_time not in reminder_times:
            sent_times = []


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
