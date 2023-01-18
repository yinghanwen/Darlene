from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Event, GroupIncreaseNoticeEvent, MessageSegment

def _rule(event: Event):
    return isinstance(event, GroupIncreaseNoticeEvent)

join=on_notice(rule=_rule)
@join.handle()
async def group_increase_handle(event: GroupIncreaseNoticeEvent):
    await join.finish(MessageSegment.text(f'欢迎新成员 {event.user_id} 加入我们的大家族!'))