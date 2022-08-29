import asyncio
from ctypes.wintypes import tagSIZE
from pathlib import Path
from unicodedata import category
import aiohttp
import json
import os
import sys
import traceback
from settings import Settings
from .utils import find
class RequiredArgError(Exception):
    pass
class ExcessArgError(Exception):
    pass
class ApiException(Exception):
    pass
def myexcepthook(type, value, tb):
    l = ''.join(traceback.format_exception(type, value, tb))
    print(l)
sys.excepthook = myexcepthook





class ApiWrapper:
    settings = Settings()
    def __init__(self, api_key: str = settings.api_key):
        self.data = json.load(open(str(Path(__file__).resolve().parent) + '/schema.json','r'))
        self.headers = {'content-type' : 'application/json'}
        self.session = aiohttp.ClientSession(headers = self.headers)
        self.api_link = 'https://фудкорт.рф/CHAT_API'
        self.api_key = api_key
    def __getattr__(self, name):
        async def wrapper(*args, **kwargs):
            kwargs.update(command=name)
            return await self.call_api(**kwargs)
        return wrapper
    async def call_api(self, **kwargs):
        reqexcepts = []
        command = kwargs.pop('command')
        excessexcepts = []
        for i in self.data[command]['opts']['required']:
            try:
                kwargs[i]
            except:
                reqexcepts.append(i)
        for i in kwargs.keys():
            if i not in self.data[command]['opts']['optional'] and i not in self.data[command]['opts']['required']:
                excessexcepts.append(i)
        if len(reqexcepts) == 0 and len(excessexcepts) == 0:
            params = {}
            params.update(API_KEY = self.api_key)
            params.update(kwargs)
            req = await self.session.post(self.api_link + self.data[command]['url'], params = params)
            try:
                data = await req.json()
                raise ApiException(data['ERROR'])
            except KeyError:
                if len(await req.json()) == 0:
                    raise ApiException('response is null')
                else:
                    return await req.json()
            except:
                return await req.json()
        else:
            if len(reqexcepts) > 0:
                raise RequiredArgError(', '.join(reqexcepts))
            if len(excessexcepts) > 0:
                raise ExcessArgError(', '.join(excessexcepts))


async def main():
    api = ApiWrapper()
    tags = await api.getTags()
    tag = tags[0]
    print(tag)
    cities = await api.getCities()
    city = cities[0]
    print(cities)
    restaurants = await api.getRestaurants(city_id = city['id'], tag_id = tag['id'])
    restaurant = restaurants[0]
    print(restaurant)
    deliveries = await api.getDeliveries()
    finded = list(filter(lambda item: item['restaurant_id'] == restaurant['restaurant_id'], deliveries))
    print(finded)
    categories = await api.getMenuCategories(restaurant_id = restaurant['restaurant_id'])
    category = categories[0]
    print(category)
    menu = await api.getMenu(restaurant_id = restaurant['restaurant_id'], category_id = category['id'])
    print(menu)
    await api.session.close()
if __name__ == '__main__':
    asyncio.run(main())