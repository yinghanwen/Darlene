from nonebot import on_message
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.log import logger
from random import randint
from yaml import Loader, load, dump
from os import path

config_name = "reply_config.yaml"
default_config = {"qq_list": ["2023491392"], "msg_list": ["你好呀~", "你好!", "贴贴!"]}


if path.exists(config_name) == False:
    with open(config_name, "w", encoding="utf-8") as f:
        f.write(dump(default_config, allow_unicode=True))
        f.close()

with open(config_name, "r", encoding="utf-8") as f:
    config = load(f.read(), Loader=Loader)
    f.close()

def read_config():
    with open(config_name, "r", encoding="utf-8") as f:
        config = load(f.read(), Loader=Loader)
        f.close()
    return config


msg = on_message()
@msg.handle()
async def msg_handle(event: GroupMessageEvent):
    # 读取配置 #
    config = read_config()
    qq_list = config["qq_list"]
    msg_list = config["msg_list"]
    # 读取配置 #
    if event.user_id in qq_list:
        count = len(msg_list)
        num = randint(0,count-1)
        msg.finish(MessageSegment.reply(event.message_id) + msg_list[num])