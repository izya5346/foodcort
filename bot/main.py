from config import *
import logging
logging.basicConfig(level=logging.DEBUG)

@dp.message_handler(Command(commands=['start']))
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'TEST', reply_markup = inline)





dp.run_polling(bot)