import json
import random
import sqlite3

from datetime import datetime, timedelta
from utils.sqlite_utils import *

from nonebot.log import logger

users = {}

async def sign_in(uid, gid):
    try:
        sqlite3.connect(".../data.db")
    
    except FileNotFoundError as e:
        logger.error(e)

    if uid not in users:
        cur.execute(sql_text)
    
    state = f"SELECT {uid} FROM state"

    if state is not None and datetime.now() - timedelta(days=1) < state:
        return "vive la france您今天签过到了噢~"

    xp = random.randint(1, 10)
    coins = random.randint(1, 10)

    

    s1 = "您坐上了前往波兰的I号坦克！"
    s2 = "您伞击了法兰西！"
    s3 = "您研究好了闪电战理论！"
    msg = random.choice(s1, s2, s3)
    msg += f"获得了 {xp} 经验值和 {coins} 枚金币！"
    return msg