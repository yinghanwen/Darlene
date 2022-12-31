import requests

from nonebot import on_regex
from nonebot.typing import T_State

from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot

daily = on_regex(pattern=r'^每日一句$')

daily.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_daily()
    await daily.send(msg[0])
    await daily.send(msg[1])

async def get_daily():
    daily_sentence = get_content()
    return daily_sentence

async def get_content():
    url = "http://open.iciba.com/dsapi"
    res = requests.get(url)
    content_e = res.json()["content"]
    content_c = res.json()["note"]

    return [content_c, content_e]