from nonebot import require
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent

from darlene.utils.json_utils import JsonUtils
from darlene.conf.schedule import SCHEDULE_PATH

from .data_source import get_wake_up_msg, get_lunch_msg, get_dinner_msg, get_sleep_msg

json_path = SCHEDULE_PATH / "schedule.json"

timing = require("nonebot_plugin_apscheduler").scheduler


group_list = JsonUtils.read_json(json_path)["group_list"]

@timing.scheduled_job("cron", hour='08', minute = '00' , second = '00' ,id="wake_up")
async def _(event: GroupMessageEvent, bot: Bot):
    if event.group_id in group_list:
        await bot.send_group_msg(
            group_id=event.group_id,
            message=get_wake_up_msg()
        )

    else:
        pass


@timing.scheduled_job("cron", hour='11', minute = '45' , second = '00' ,id="lunch")
async def _(event: GroupMessageEvent, bot: Bot):
    if event.group_id in group_list:
        await bot.send_group_msg(
            group_id=event.group_id,
            message=get_lunch_msg()
        )
    
    else:
        pass

@timing.scheduled_job("cron", hour='19', minute = '00' , second = '00' ,id="dinner")
async def _(event: GroupMessageEvent, bot: Bot):
    if event.group_id in group_list:
        await bot.send_group_msg(
            group_id=event.group_id,
            message=get_dinner_msg()
        )
    
    else:
        pass

@timing.scheduled_job("cron", hour='22', minute = '00' , second = '00' ,id="go_to_sleep")
async def _(event: GroupMessageEvent, bot: Bot):
    if event.group_id in group_list:
        await bot.send_group_msg(
            group_id=event.group_id,
            message=get_sleep_msg()
        )
    
    else:
        pass