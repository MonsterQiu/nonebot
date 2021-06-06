
from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupDecreaseNoticeEvent,GroupIncreaseNoticeEvent

wel=on_notice()
@wel.handle()
async def _(bot:Bot,event:GroupIncreaseNoticeEvent,state:T_State):
    user= event.get_user_id()
    at_="[CQ:at,qq={}]".format(user)
    msg=at_+'欢迎新进群的小伙伴，\来了就别走了哦'
    msg=Message(msg)
    await wel.finish(message=msg)

@wel.handle()
async def _(bot:Bot,event:GroupDecreaseNoticeEvent,state:T_State):
    user= event.get_user_id()
    at_="[CQ:at,qq={}]".format(user)
    msg=at_+"\n"+'有一位朋友离我们而去了'
    msg = Message(msg)
    await wel.finish(message=msg)


