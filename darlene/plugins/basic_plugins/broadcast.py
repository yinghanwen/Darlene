from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment, Bot

__plugin_meta__ = PluginMetadata(
    name = "Darlene 广播",
    description = "只有超管能用噢",
    usage = """
    /广播
    """,

    extra = {
        "author": "MRSlouzk",
        "version": "0.0.1"
    }
)

cancel_word=["取消", "取消发送", "cancel", "Cancel"]

bc=on_command("broadcast", aliases={"bc", "广播", "全局广播", "notice"}, permission=SUPERUSER)
@bc.handle()
async def bc_wait(event: MessageEvent, bot: Bot):
    await bc.pause(MessageSegment.reply(event.message_id) + MessageSegment.text("请发送需要广播的消息"))

@bc.handle()
async def bc_send(event: MessageEvent, bot: Bot):
    if event.message.extract_plain_text() in cancel_word:
        await bc.finish(MessageSegment.reply(event.message_id) + MessageSegment.text("已取消发送。"))
    else:
        count=0
        for i in await bot.get_group_list():
            await bot.send_group_msg(group_id=i['group_id'], message=event.message)
            count+=1
        await bc.finish(MessageSegment.reply(event.message_id) + MessageSegment.text(f"成功发送到 {count} 个群。"))