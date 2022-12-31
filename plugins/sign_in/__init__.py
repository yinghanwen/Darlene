from nonebot import on_regex

from nonebot.log import logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent, GROUP

from .data_source import sign_in

PREFIX = "[sign in]"

sign = on_regex(r"^签到$", permission=GROUP, priority=5, block=True)
@sign.handle()
async def _(event: GroupMessageEvent):
    uid = event.user_id
    gid = event.group_id

    logger.opt(f"{PREFIX} {gid}:{uid} 申请签到")

    msg = await sign_in(uid, gid)
    await sign.finish(msg)