from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from keyboard import kb, kb_photo


API_TOKEN = '5704955736:AAHgsJ8KL4w7mD7g35mukA9D1dkgznzxktI'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

async  def on_startup(_):
    print(" а")

@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Чтобы отправить рандомную фото нажми на конепку рандомб',
                         reply_markup=kb_photo)


HELP = """
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание</em>
<b>/start</b> - <em>запуск бота</em>
"""


dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='даб даб',
                         reply_markup=kb)
    await message.delete()



dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP,
                         parse_mode="HTML")
    await message.delete()



dp.message_handler(commands=['description'])
async def cmd_description(message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)


