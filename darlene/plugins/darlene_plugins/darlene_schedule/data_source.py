from random import choice
from nonebot.adapters.onebot.v11 import Message

from utils.json_utils import JsonUtils
from .config import WORDS_PATH, Path

async def get_wake_up_msg() -> Message:
    wake_up_json = Path(WORDS_PATH / "wake_up.json")
    words = JsonUtils.read_json(wake_up_json)
    word = Message(choice(words))
    return word


async def get_lunch_msg() -> Message:
    lunch_json = Path(WORDS_PATH / "lunch.json")
    words = JsonUtils.read_json(lunch_json)
    word = Message(choice(words))
    return word


async def get_dinner_msg() -> Message:
    dinner_json = Path(WORDS_PATH / "dinner.json")
    words = JsonUtils.read_json(dinner_json)
    word = Message(choice(words))
    return word

async def sleep_msg() -> Message:
    lunch_json = Path(WORDS_PATH / "lunch.json")
    words = JsonUtils.read_json(lunch_json)
    word = Message(choice(words))
    return word