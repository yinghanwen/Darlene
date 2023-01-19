import re
import ujson as json

from nonebot import on_request
from nonebot.adapters.onebot.v11 import Bot, GroupRequestEvent

from darlene.utils.darlene_logger import logger

notice=on_request(priority=1)

group_to_use=[] 
approve_message_1=[""] 

@notice.handle()
async def _(bot: Bot,event: GroupRequestEvent):
    if(event.group_id in group_to_use):
        raw = json.loads(event.json())
        gid = str(event.group_id)
        flag = raw['flag']
        sub_type = raw['sub_type']
        if sub_type == 'add':
            comment = raw['comment']
            word = re.findall(re.compile('答案：(.*)'), comment)[0]
            uid = event.user_id
            if(str(word) in approve_message_1):
                logger.info(f'同意{uid}加入群 {gid},验证消息为 “{word}”') #控制台日志输出加群信息!logger类的使用参见																		2.5章(未做)
                await bot.set_group_add_request(
                    flag=flag,
                    sub_type=sub_type,
                    approve=True,
                    reason=" ",
                )
            else:
                await notice.finish("有人要加群!但答案不对呀!")
    await notice.finish()