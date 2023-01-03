import aiosqlite
import asyncio
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment

from . import handle_vote

async def on_trial(bot: Bot,event: GroupMessageEvent):
    gid = event.group_id

    await asyncio.sleep(3 * 60)
    await bot.send_group_msg(group_id=gid,message="开始唱票")

    async with aiosqlite.connect("vote.db") as db:

        cur = await db.cursor()

        to_kick_id = cur.execute(
            '''SELECT to_kick_id FROM WHERE gid=?''', (gid,)
        )

        yes = cur.execute(
            '''SELECT yes_votes FROM WHERE gid=?''', (gid,)
        )

        no = cur.execute(
            '''SELECT no_votes FROM WHERE gid=?''', (gid,)
        ) 

        msg = f"有 {yes} 人投了同意票，{no} 人投了反对票\n"
        
        if yes > no:
            msg += "显然，同意大于反对，实施制裁"
            await bot.send_group_msg(group_id=gid, message=msg)
            bot.set_group_kick(to_kick_id)
        
        elif no > yes:
            msg += "显然，反对票数大于同意票数，取消审判"
            await bot.send_group_msg(group_id=gid, message=msg)

        elif no == yes:
            msg += "显然，反对票等于同意票数？？？？？取消审判"
            await bot.send_group_msg(group_id=gid, message=msg)


async def applying(bot:Bot, event: GroupMessageEvent, to_kick_id):

    group_id = event.group_id
    initiator_id = event.user_id

    async with aiosqlite.connect("vote.db") as db:
        cur = await db.cursor()
        
        await cur.execute(
             '''CREATE TABLE IF NOT EXISTS votes (
                id INTEGER PRIMARY KEY,
                group_id INTEGER NOT NULL,
                initiator_id INTEGER NOT NULL,
                to_kick_id INTEGER NOT NULL,
                yes INTEGER NOT NULL,
                no INTEGER NOT NULL
            )'''
        )

        #检查本群是否有正在进行的投票
        await cur.execute(
            '''SELECT * FROM votes WHERE group_id=?''',
            (group_id,)
        ) 

        ongoing_vote = await cur.fetchone()
        if ongoing_vote:
            await bot.send_group_msg(group_id=group_id, message="已经有一个战犯被审判了！请稍后再试")
            return

        #如果没有正在进行的投票，那么新建一个投票
        await cur.execute(
            '''INSERT INTO votes (group_id, initiator_id, to_kick_id, yes_votes, no_votes)
            VALUES (?, ?, ?, 0, 0)''',
            (group_id, initiator_id, to_kick_id)
        )

        await db.commit()

        await cur.execute(
            '''SELECT id FROM votes WHERE group_id=? AND initiator_id=? AND to_kick_id=?''',
            (group_id, initiator_id, to_kick_id)
        )

        await bot.send_group_msg(group_id=group_id, msg=f"针对战犯 {MessageSegment.at(to_kick_id)} 的公审已发起！输入 “/投票 同意” 或者 “/投票 不同意” 参与审判！")

async def voting(bot:Bot, event: GroupMessageEvent):
    group_id = event.group_id
    voter_id = event.user_id

    async with aiosqlite.connect('vote.db') as db:
        cur = await db.cursor()

        await cur.execute(
            '''SELECT * FROM votes WHERE id=? AND group_id=?''',
        (voter_id, group_id)
        )

        vote_check = await cur.fetchone()
        if not vote_check:
            await bot.send_group_msg(group_id=group_id, message="找不到对应的战犯~")
            return

        await cur.execute(
            '''SELECT * FROM vote_history WHERE voter_id=?''',
        (voter_id,)
        )

        has_voted = await cur.fetchone()
        if has_voted:
            await bot.send_group_msg(group_id=group_id, message="您审判过了~")
            return
        
        if handle_vote() is "同意":
            await cur.execute(
                 '''UPDATE votes SET yes_votes=yes_votes+1 WHERE id=?''',
                (voter_id,)
            )

        else:
            await cur.execute(
                 '''UPDATE votes SET no_votes=no_votes+1 WHERE id=?''',
                (voter_id,)
            )
        
        await db.commit()

        await cur.execute(
             '''INSERT INTO vote_history (voter_id) VALUES (?)''',
            (voter_id,)
        )

        await db.commit()

        await bot.send_group_msg(group_id=group_id, message="您的投票已被记录")