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



divorce = on_command("divorce", aliases={"离婚","你好，离婚"},priority=50)
@divorce.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    """
    如果未婚 则退出
    如果已婚 则通知对方 问他是否同意离婚
    """

