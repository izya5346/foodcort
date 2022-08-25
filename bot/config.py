from aiogram import *
from aiogram import Dispatcher
from aiogram.types import *
from aiogram.dispatcher.filters import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.fsm.storage.redis import RedisStorage
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters.callback_data import CallbackData
import aioredis as redis
connection = redis.from_url('redis://localhost:6379')
storage = RedisStorage(connection, state_ttl = 30*60, data_ttl = 30*60)
bot = Bot(token='5531328946:AAGh49cMI0wtlbODR2SHq41yjLl-D7oUIy0')
dp = Dispatcher(storage=storage)
inline = InlineKeyboardMarkup(inline_keyboard =[[InlineKeyboardButton(text = 'test', web_app = WebAppInfo(url = 'https://73cc-178-205-242-191.eu.ngrok.io'))]])