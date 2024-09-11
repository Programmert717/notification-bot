import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TOKEN

MSG = "Милая,таблеточки пила сегодня?"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет котик, твой парень создал меня, чтобы напоминать тебе пить таблеточки!\n"f"Каждый часик я буду отправлять тебе напоминалочку!")

    for i in range(4):
        await asyncio.sleep(60*60 )
        await bot.send_message(user_id, MSG.format(user_name))


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())