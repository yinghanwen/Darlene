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
        users[uid] = {
            "xp": 0,
            "coins": 0,
            "state":None,
        }

    state = users[uid]["state"]

    if state is not None and datetime.now() - timedelta(days=1) < state:
        return "您今天签过到了噢~"

    xp = random.randint(1, 10)
    coins = random.randint(1, 10)

    users[uid]["xp"] += xp
    users[uid]["coins"] += coins

    msg = f"您获得了 {xp} 经验值和 {coins} 枚金币！"
    return msg