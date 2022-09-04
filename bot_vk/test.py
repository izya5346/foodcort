import asyncio
# from config import api
import sys
sys.path.append('/home/foodcort')
from api_wrapper import ApiWrapper

async def main():
    api = ApiWrapper()
    cities = await api.getCities()
    print(cities)
    print('-'* 100)
    restaurants = await api.getRestaurants(city_id = cities[3]['id'])
    print(restaurants)
    print('-'* 100)
    restaurants = [i['restaurant_id'] for i in restaurants]
    print(restaurants)
    print('-'* 100)
    tags = await api.getTags()
    print(tags)
    print('-'* 100)
    tags = list(filter(lambda item: item['restaurant_id'] in restaurants, tags))
    print(tags)
    print('-'* 100)
    _ = [i.pop('restaurant_id') for i in tags]
    print(tags)
    print('-'* 100)
    tags = list({v['id']:v for v in tags}.values())
    print(tags)
    print('-'* 100)
    restaurants = await api.getRestaurants(city_id = cities[0]['id'], tag_id = '1759')
    print(restaurants)
    print(len(restaurants))
    print('-'* 100)
    await api.session.close()

asyncio.run(main())
