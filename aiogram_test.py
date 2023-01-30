import asyncio
import logging
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6084946021:AAFajYA643e2sD0m_U3xZ5t08cfyOEdELZc')

dp = Dispatcher(bot)

# from aiogram import types
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = "/help"
    keyboard.add(button_1)
    await message.answer("Чем я вам могу помочь?", reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
    await message.answer('Бот временно работает ведутся технические работы')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
