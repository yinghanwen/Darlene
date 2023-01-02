import aiosqlite
import random

from nonebot import on_regex
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent, GROUP



PREFIX = "[sign in]"

sign = on_regex(r"^签到$", permission=GROUP, priority=5, block=True)
@sign.handle()
async def _(event: GroupMessageEvent):
    uid = event.user_id
    gid = event.group_id
    logger.opt(f"{PREFIX} {gid}:{uid} 申请签到")

    async with aiosqlite.connect("vote.db") as db:
        cur = await db.cursor()
        cur.execute('SELECT xp, coins FROM users WHERE uid=?', (uid,))
        user = cur.fetchone()

        if user is None:
            cur.execute('INSERT INTO users (uid) VALUES (?)', (uid,))
            xp = 0
            coins = 0

        else:
            xp, coins = user
        
        xp += random.randint(10,20)
        coins += random.randint(20,100)

        cur.execute('UPDATE users SET xp=?, coins=?, WHERE uid=?', (xp, coins, uid))
        await db.commit()
    
