from nonebot import on_command, on_keyword
# from nonebot.adapters import Bot,Event
# from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent

test = on_keyword({'我帅不帅', '谁最帅'})


@test.handle()
async def h_r(bot: Bot, event: GroupMessageEvent, state: T_State):
    id_ = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(id_)
    msg = at_ + '你最帅，帅的一批'
    msg = Message(msg)
    await test.finish(msg)
