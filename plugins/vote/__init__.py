from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.permission import GROUP
from nonebot.plugin import on_command

from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent
from .data_source import applying


apply = on_command("apply", aliases={"申请投票","申请制裁","制裁申请"},permission=GROUP)
@apply.handle()
async def apply_first_recieve(event:GroupMessageEvent, matcher: Matcher,to_kick_id: Message = CommandArg()):
    """
    申请投票 @某人
    """


    plain_text = to_kick_id.extract_plain_text()
    if plain_text:
        matcher.set_arg("to_kick_id", to_kick_id)

    


@apply.got("to_kick_id", prompt="你想公审哪位战犯呢？")
async def handle_to_kick_id(event: GroupMessageEvent,to_kick_id: Message = Arg(), id: str = ArgPlainText("to_kick_id")):
    if to_kick_id not in event.group_id:
        await apply.reject("这位战犯不在群内")
        return

    await applying(to_kick_id)






vote = on_command("vote", aliases={"投票"},permission=GROUP)
@vote.handle()
async def vote_first_recieve(event:GroupMessageEvent, matcher: Matcher,attitude: Message = CommandArg()):
    plain_text = attitude.extract_plain_text()
    if plain_text:
        matcher.set_arg("attitude", attitude)

@vote.got("attitude", prompt="您的态度是？（同意/不同意）")
async def handle_vote(attitude: Message =  Arg(), opinion: str = ArgPlainText("attitude")) -> str:
        if opinion in ["同意", "不同意"]:
            if opinion == "同意":
                return "同意"
            elif opinion == "不同意":
                return "不同意"
        
        else:
            await vote.reject("您的输入内容错误！（同意/不同意）")
            return




