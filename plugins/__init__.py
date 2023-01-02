import time

from nonebot.params import Arg, CommandArg, Depends
from nonebot.permission import GROUP
from nonebot.plugin import on_command
from nonebot.typing import T_State

from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent


var = {}

apply = on_command("apply", aliases={"申请投票","申请制裁","制裁申请"},permission=GROUP)
@apply.handle()
async def apply_handle_first_recieve(state: T_State,args: Message = CommandArg()):
    """
    申请投票 类型（踢出/禁言） @某人
    """

    plain_text = args.extract_plain_text().strip()
    if plain_text:
        if plain_text != "禁言" or "踢出":
            await apply.reject("踢出类型错误呢！")
            return

        state["type"] = plain_text

@apply.got("type", prompt="你想让他接受哪种制裁呢（踢出/禁言）", parameterless=[Depends("type")])
@apply.got("person", prompt="你想禁言谁呢?", parmeterless=[Depends("person")])
async def _(person: Message = Arg()):
    if person["type"] != "at":
        await apply.send("格式错误！")