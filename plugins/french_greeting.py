import random
import time

from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot.adapters.onebot.v11.message import Message


LUCK_MESSAGES = [
    ("不会被闪击", range(1, 18)),
    ("小概率会被闪击", range(18, 53)),
    ("听到德军坦克的声音了！", range(53, 58)),
    ("准备好防御工事！", range(58, 62)),
    ("准备举起白旗！", range(62, 65)),
    ("vive la france!", range(65, 71))
]

def get_luck_message(luck_num):
    for message, luck_range in LUCK_MESSAGES:
        if luck_num in luck_range:
            return message

today_luck = on_keyword(["今日人品","今日被闪击"], priority=50, block=True)

@today_luck.handle()
async def _(event: MessageEvent):
    rnd = random.Random()
    at_u = MessageSegment.at(event.user_id)
    rnd.seed(int(time.time()) + int(event.get_user_id()))
    luck_num = rnd.randint(1, 100)
    luck_message = get_luck_message(luck_num)
    await today_luck.finish(f"{at_u} {luck_message} 您今日的二战幸运指数是 {luck_num} / 100 (越低越好）")