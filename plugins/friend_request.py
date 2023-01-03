import random
import string

from nonebot.log import logger

from nonebot.params import CommandArg, ArgStr
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command, on_request
from nonebot.typing import T_State

from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11.event import FriendRequestEvent, MessageEvent

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
async def _(user_id: str = ArgStr('user_id')):
    user_id = user_id.strip()
    if not user_id.isdigit():
        logger.warning("qq num is not int")
        await send_code.reject(f"{PREFIX} QQ号不是纯数字")

@on_request("friend")
async def _(bot: Bot, event: FriendRequestEvent):
    request_user_id = event.user_id
    request_message = event.comment
    code = ''.join(random.choices(string.digits, k=6))
    VERTIFY_CODE[request_user_id] = code
    await bot.set_friend_add_request(flag=event.flag, approve=False, remark=code)
    await bot.send_private_msg(user_id=request_user_id, message=f"{PREFIX} 您的验证码是 {code}")

verify = on_command("verify", aliases={"验证"}, permission=SUPERUSER, priority=4, block=True)
@verify.handle()
async def _(bot: Bot, event: MessageEvent, Args: Message = CommandArg()):
    request_user_id = event.user_id
    request_message = event.message
    if request_user_id in VERTIFY_CODE:
        code = VERTIFY_CODE.get(request_user_id)
        if code in request_message:
            await bot.set_friend_add_request(flag=event.flag, approve=True)
            await bot.send_private_msg(user_id=request_user_id, message=f"{PREFIX} 验证成功")
            del VERTIFY_CODE[request_user_id]
        else:
            await bot.send_private_msg(user_id=request_user_id, message=f"{PREFIX} 验证码错误")
    else:
        await bot.send_private_msg(user_id=request_user_id, message=f"{PREFIX} 您没有收到验证码或者验证码已过期")
