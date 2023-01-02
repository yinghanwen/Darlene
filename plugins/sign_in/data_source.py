import json
import random
from datetime import datetime, timedelta

users = {}

async def sign_in(uid, gid):
    try:
        with open(".../data.json", "r", encoding="utf-8") as f:
            users = json.load(f)
    
    except FileNotFoundError:
        pass

    if uid not in users:
        users[gid][uid] = {
            "xp": 0,
            "coins": 0,
            "state":None,
        }

    state = users[gid][uid]["state"]

    if state is not None and datetime.now() - timedelta(days=1) < state:
        return "vive la france您今天签过到了噢~"

    xp = random.randint(1, 10)
    coins = random.randint(1, 10)

    users[gid][uid]["xp"] += xp
    users[gid][uid]["coins"] += coins

    s1 = "您坐上了前往波兰的I号坦克！"
    s2 = "您伞击了法兰西！"
    s3 = "您研究好了闪电战理论！"
    msg = random.choice(s1, s2, s3)
    msg += f"获得了 {xp} 经验值和 {coins} 枚金币！"
    return msg