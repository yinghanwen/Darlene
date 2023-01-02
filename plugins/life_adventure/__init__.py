from nonebot import on_command
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment

import random
from datetime import datetime

marry = on_command("marry", aliases={"结婚","你好，结婚"},priority=50)
@marry.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    如果后面有参数 则求婚
    如果没有参数 则征婚
    有空再写 咕咕咕
    """
