import random
from datetime import date

from nonebot.plugin import on_keyword

from nonebot.adapters.onebot.v11 import Event, MessageSegment
from nonebot.adapters.onebot.v11.message import Message


def luck_simple(num):
    if num < 18:
        return "不会被闪击"

    elif num < 53:
        return "小概率会被闪击"
    
    elif num < 58:
        return  "听到德军坦克的声音了！"
    
    elif num < 62:
        return "准备好防御工事！"

    elif num < 65:
        return "准备举起白旗！"
    
    elif num < 71:
        return "vive la france!"


today_luck = on_keyword(["今日人品","今日被闪击"], priority=50, block=True)
@today_luck.handle()
async def _(event: Event):
    rnd = random.Random()
    at_u = MessageSegment.at(event.user_id)
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1,100)
    await today_luck.finish(Message(f'{at_u}您今日的二战幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'))