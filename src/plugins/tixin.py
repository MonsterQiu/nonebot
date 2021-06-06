from nonebot import require
import nonebot

# from nonebot_plugin_apscheduler import scheduler
scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour=7, end_date='2024-12-13 14:00:10', id='sleep_sched')
async def dy_sched():
    bot = nonebot.get_bots()['机器人qq号']
    return await bot.call_api('send_group_msg', **{
        'message': '宝贝该钉钉打卡了:\n别忘记了哦',
        'group_id': '你自己的qq号'
    })
