from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from .ark_setting import *
import random as rd, os


random_operator_event = on_keyword(['随机干员'],priority=50)
@random_operator_event.handle()
async def random_operator_handle(bot: Bot, event: Event):
    print('随机干员现在开始运行')
    operator_profile_path = "file:///" + operator_profile_dir +\
        rd.choice(os.listdir(operator_profile_dir))
    print(operator_profile_path)
    message_CQ = Message(f'[CQ:at,qq={event.get_user_id()}]')
    message_img = MessageSegment.image(operator_profile_path),
    msg = message_CQ + message_img
    await random_operator_event.send(
        msg
        )