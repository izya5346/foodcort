import asyncio
import json
import logging
from unicodedata import category
import aiohttp
API_KEY = 'OOF5vax24o6Q'
class ApiWrapper:
    def __init__(self) -> None:
        self.headers = {'content-type' : 'application/json'}
        self.session: aiohttp.ClientSession = aiohttp.ClientSession(trust_env = True)
        self.api_link = 'https://фудкорт.рф/CHAT_API'
    def format(self, text:str) -> dict:
        text = text.split('>')[1].split('<')[0]
        return json.loads(text)
    async def fetch(self, link: str, params: dict, data: dict = {}):
        r = await self.session.get(f'{self.api_link}{link}', params = params, headers = self.headers)
        logging.info(f"Success: {r.status == 200}")
        logging.info(f"Url: {r.url}")
        return await r.json()

async def main():
    api = ApiWrapper()
    print(await api.fetch('/menu/head/', params = {'API_KEY': API_KEY, 'restaurant_id': 'q1'}))
    await api.session.close()
asyncio.run(main())