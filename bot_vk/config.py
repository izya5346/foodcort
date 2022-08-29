from tkinter import image_names
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from settings import Settings
import sys
sys.path.append('/home/izyafroloff/foodcort')
from api_wrapper import ApiWrapper
from utils import generate_keyboard
settings = Settings()
bot = Bot(settings.vk_token)
api = ApiWrapper()
text = Text()