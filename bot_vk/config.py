from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError, OpenLink, KeyboardButtonColor
from vkbottle.bot import Bot, Message
from settings import Settings
import sys
import aioredis as redis
sys.path.append('/home/foodcort')
from api_wrapper import ApiWrapper
settings = Settings()
bot = Bot(settings.vk_token)
api = ApiWrapper()
conn = redis.Redis()