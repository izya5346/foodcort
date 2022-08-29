from pprint import pprint
from config import *
@bot.on.message()
async def echo(message: Message):
    match message.text:
        case 'Начать':
            cities = await api.getCities()
            
            keyboard = Keyboard(one_time = True).schema(generate_keyboard(cities)).get_json()
            pprint(generate_keyboard(cities))
            await message.answer('Из какого вы города?', keyboard  = keyboard)
        case _:
            await message.answer(message.text)
bot.run_forever()