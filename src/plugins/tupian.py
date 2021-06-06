from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re

yulu = on_keyword({'美女'}, priority=10)


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await mei()

    await yulu.send(Message(msg))


async def mei():
    url = 'https://api.66mz8.com/api/rand.img.php?type=美女&format=json'
    resp = requests.get(url)
    data = resp.json()
    ur = data.get('pic_url')
    tu = f"[CQ:image,file={ur}]"
    return tu
