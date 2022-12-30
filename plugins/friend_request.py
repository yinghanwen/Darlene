import random
import string

from nonebot.log import logger
from nonebot.matcher import Matcher

from nonebot.params import CommandArg, ArgStr
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command, on_request
from nonebot.rule import to_me
from nonebot.typing import T_State

from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.event import FriendRequestEvent, GroupMessageEvent

"""
This plugin code is purely theoretical
May include many bugs
still in developing
"""

VERTIFY_CODE: dict[str, str] = {}
PREFIX = "[Friend Request]"

async def parase_user_id(state: T_State, Args: Message = CommandArg()):
    if uid := Args.extract_plain_text().strip():
        state.update({'user_id':uid})

send_code = on_command("send_code", aliases={"好友验证"}, permission=SUPERUSER, priority=6, block=True)
send_code.handle()
async def handle_user_vertify_code(user_id: str = ArgStr('user_id')):
    user_id = user_id.strip()
    if not user_id.isdigit():
        logger.warning("qq num is not int")
        await send_code.reject(f"{PREFIX} QQ号不是纯数字")

