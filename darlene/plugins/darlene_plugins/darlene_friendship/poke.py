from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Message

def _check(event: PokeNotifyEvent):
    return event.target_id==event.self_id


poke=on_notice(rule=_check)

@poke.handle()
async def _(event: PokeNotifyEvent):
        await poke.finish(Message(f"[CQ:at,qq={event.user_id}]不要再戳了喵!"))