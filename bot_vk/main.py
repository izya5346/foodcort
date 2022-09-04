import json
from pprint import pprint
from config import *
from utils import generate_keyboard
@bot.on.message()
async def echo(message: Message):
    if message.payload:
        match json.loads(message.payload)['command']:
            case 'get_cities':
                user = {'city_id': json.loads(message.payload)['id']}
                await conn.hmset(message.peer_id, user)
                restaurants = await api.getRestaurants(city_id = user['city_id'])
                restaurants = [i['restaurant_id'] for i in restaurants]
                tags = await api.getTags()
                tags = list(filter(lambda item: item['restaurant_id'] in restaurants, tags))
                _ = [i.pop('restaurant_id') for i in tags]
                tags = list({v['id']:v for v in tags}.values())
                await message.answer('Какую кухню предпочитаете?', keyboard  = generate_keyboard(tags, 'get_tags'))
            case 'get_tags':
                user = await conn.hgetall(message.peer_id)
                user.update({'tag_id': json.loads(message.payload)['id']})
                await conn.hmset(message.peer_id, user)
                user = await conn.hgetall(message.peer_id)
                user = {key.decode('utf-8'): value.decode('utf-8') for key, value in user.items()}
                restaurants = await api.getRestaurants(city_id = user['city_id'], tag_id = user['tag_id'])
                # print(f'Ту мач: {len(restaurants)}')
                await message.answer('Выберите ресторан: ', keyboard = generate_keyboard(restaurants, 'get_restaurants'))
            case 'get_restaurants':
                link = await api.getLink(restaurant_id = json.loads(message.payload)['id'])
                keyboard = Keyboard(inline = True)
                keyboard.add(OpenLink(link = f"https://фудкорт.рф/{link['url']}", label = 'Перейти'))
                await message.answer('Приятного аппетита!', keyboard = keyboard)
                keyboard = Keyboard(one_time = True, inline = False)
                keyboard.add(Text(label = 'Назад', payload = {'command': 'back', 'to': 'get_restaurants'}))
                await message.answer('Вернуться назад', keyboard = keyboard)
            case 'back':
                match json.loads(message.payload)['to']:
                    case 'get_cities':
                        cities = await api.getCities()
                        await message.answer('Из какого вы города?', keyboard  = generate_keyboard(cities, 'get_cities'))
                    case 'get_tags':
                        user = await conn.hgetall(message.peer_id)
                        user = {key.decode('utf-8'): value.decode('utf-8') for key, value in user.items()}
                        restaurants = await api.getRestaurants(city_id = user['city_id'])
                        restaurants = [i['restaurant_id'] for i in restaurants]
                        tags = await api.getTags()
                        tags = list(filter(lambda item: item['restaurant_id'] in restaurants, tags))
                        _ = [i.pop('restaurant_id') for i in tags]
                        tags = list({v['id']:v for v in tags}.values())
                        await message.answer('Какую кухню предпочитаете?', keyboard  = generate_keyboard(tags, 'get_tags'))
                    case 'get_restaurants':
                        user = await conn.hgetall(message.peer_id)
                        user = {key.decode('utf-8'): value.decode('utf-8') for key, value in user.items()}
                        restaurants = await api.getRestaurants(city_id = user['city_id'], tag_id = user['tag_id'])
                # print(f'Ту мач: {len(restaurants)}')
                        await message.answer('Выберите ресторан: ', keyboard = generate_keyboard(restaurants, 'get_restaurants'))
            case 'start':
                cities = await api.getCities()
                await message.answer('Из какого вы города?', keyboard  = generate_keyboard(cities, 'get_cities'))
                            
    else:
        match message.text:   
            case 'Начать':
                cities = await api.getCities()
                await message.answer('Из какого вы города?', keyboard  = generate_keyboard(cities, 'get_cities'))
            case _:
                keyboard = Keyboard(one_time = True)
                keyboard.add(Text('Начать', payload = {'command': 'start'}), color = KeyboardButtonColor.POSITIVE)
                await message.answer('Я тебя не понимаю, может вернуться в начало?', keyboard = keyboard)
bot.run_forever()