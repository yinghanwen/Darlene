import aiosqlite
import asyncio

from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.permission import GROUP
from nonebot.plugin import on_command

from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, GroupMessageEvent



apply = on_command("apply", aliases={"申请投票","申请制裁","制裁申请"},permission=GROUP)
@apply.handle()
async def apply_first_recieve(event:GroupMessageEvent, matcher: Matcher,to_kick_id: Message = CommandArg()):
    """
    申请投票 @某人
    """


    plain_text = to_kick_id.extract_plain_text()
    if plain_text:
        matcher.set_arg("to_kick_id", to_kick_id)

    


@apply.got("to_kick_id", prompt="你想公审哪位战犯呢？")
async def handle_to_kick_id(event: GroupMessageEvent,to_kick_id: Message = Arg(), id: str = ArgPlainText("to_kick_id")):
    if to_kick_id not in event.group_id:
        await apply.reject("这位战犯不在群内")
        return

    await applying(to_kick_id)

async def applying(event: GroupMessageEvent,to_kick_id):

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
            await apply.finish("已经有一个战犯被审判了！请稍后再试")
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

        await apply.send(f"针对战犯 {MessageSegment.at(to_kick_id)} 的公审已发起！输入 “/投票 同意” 或者 “/投票 不同意” 参与审判！")
    

async def on_trial(bot: Bot,event: GroupMessageEvent):
    gid = event.group_id

    await asyncio.sleep(3 * 60)
    await apply.send("开始唱票")

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
            await apply.finish(msg)
            bot.set_group_kick(to_kick_id)
        
        elif no > yes:
            msg += "显然，反对票数大于同意票数，取消审判"
            await apply.finish(msg)

        elif no == yes:
            msg += "显然，反对票等于同意票数？？？？？取消审判"
            await apply.finish(msg)


vote = on_command("vote", aliases={"投票"},permission=GROUP)
@vote.handle()
async def vote_first_recieve(event:GroupMessageEvent, matcher: Matcher,attitude: Message = CommandArg()):
    plain_text = attitude.extract_plain_text()
    if plain_text:
        matcher.set_arg("attitude", attitude)

@vote.got("attitude", prompt="您的态度是？（同意/不同意）")
async def handle_vote(attitude: Message =  Arg(), opinion: str = ArgPlainText("attitude")) -> str:
        if opinion in ["同意", "不同意"]:
            if opinion == "同意":
                return "同意"
            elif opinion == "不同意":
                return "不同意"
        
        else:
            await vote.reject("您的输入内容错误！（同意/不同意）")
            return

async def voting(event: GroupMessageEvent):
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
            await vote.finish("找不到对应的战犯~")
            return

        await cur.execute(
            '''SELECT * FROM vote_history WHERE voter_id=?''',
        (voter_id,)
        )

        has_voted = await cur.fetchone()
        if has_voted:
            await vote.finish("您审判过了~")
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

        await vote.finish("您的投票已被记录")


