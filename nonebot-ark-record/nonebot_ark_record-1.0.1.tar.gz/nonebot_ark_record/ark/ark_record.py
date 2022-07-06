from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from .ark_db import *
from .ark_scrawl import *
print('成功载入ark/ark_record.py')

user_token_event = on_keyword(['方舟抽卡token', '方舟寻访token'],priority=50)
@user_token_event.handle()
async def user_token_handle(bot: Bot, event: Event):
    print('开始设置token')
    qq_id = event.get_user_id()
    user_token = str(event.get_message()).split(' ')[1].strip()
    response = write_token2db(arkgacha_db, qq_id, user_token)
    await user_token_event.finish(\
        Message(\
            f'[CQ:at,qq={event.get_user_id()}] {response}'\
            )
        )


user_analysis_event = on_keyword(['方舟抽卡分析','方舟寻访分析'],priority=50)
@user_analysis_event.handle()
async def user_analysis_handle(bot: Bot, event: Event):
    qq_id = event.get_user_id()    
    print('user_info')
    success, user_info = read_token_from_db(arkgacha_db, qq_id)

    #如果没获取到
    if not success:
        await user_analysis_event.finish(\
            Message(\
                '[CQ:at,qq={}]{}'.format(event.get_user_id(), user_info)\
                )
            )
    else:
        success, max_record_count, pool_name, response_info = parse_message(event.get_message())
        if success:
            success, response_info = user_ark_analyser(arkgacha_db, user_info, max_record_count, pool_name)
        if success:
            image_file_path = "file:///" + response_info
            print(image_file_path)
            message_CQ = Message(f'[CQ:at,qq={event.get_user_id()}]')
            message_img = MessageSegment.image(image_file_path),
            msg = message_CQ + message_img
            await user_analysis_event.send(
                msg
                )
        else:
            await user_analysis_event.finish(\
                Message(\
                    '[CQ:at,qq={}]{}'.format(event.get_user_id(), response_info)\
                    )
                )

ark_help_event = on_keyword(['方舟抽卡帮助','方舟寻访帮助'],priority=50)
@ark_help_event.handle()
async def ark_help_handle(bot: Bot, event: Event):
    example_json = str({"status":0,"msg":"OK","data":{"token":"example123456"}})
    example_token = "example123456"
    example_command1 = "方舟抽卡token example123456"
    example_command2 = "方舟抽卡分析"
    example_command3 = "方舟抽卡分析 100"
    await ark_help_event.finish(\
            Message(\
                f'[CQ:at,qq={event.get_user_id()}]欢迎使用明日方舟抽卡分析工具！请通过以下步骤使用。\
                    \n1、在浏览器中打开官网（不要在QQ中打开） https://ak.hypergryph.com/user/login 登录你的账号。\
                    \n2、在 https://as.hypergryph.com/user/info/v1/token_by_cookie 复制页面中的token（不带引号）。\
                    \n如：页面内容为{example_json}，则复制{example_token}。\
                    \n3、在QQ群/私聊中使用 方舟抽卡token + 你的token（不带加号，带空格），设置token。\
                    \n如使用 {example_command1} 进行设置。\
                    \n4、使用 方舟抽卡分析 + (分析的抽数，可以不加)命令，就可以进行抽卡分析。\
                    \n如使用 {example_command2} 分析当前数据库中所有的抽卡记录； \
                    \n又如使用 {example_command3} 分析最近至多100条抽卡记录。\
                    \n---------------------------------\
                    \n建议间隔一段时间在步骤2的网址中重新获取一次你的token，否则可能无法获取最新的寻访记录。\
                    \n本插件支持增量保存，你的抽卡记录可能会被长时间保存。\
                    \n如担心token泄露，可以私聊设置后再在群内使用分析命令。\
                    \ntoken使用安全，不会泄露除uid、昵称、寻访及充值记录以外的其他账号信息。\
                    \n目前仅支持官服。\
                    '\
                )
            )


def parse_message(message:str):#todo:修改为正则匹配
    """_summary_
    解析抽卡分析的输入参数
    Args:
        message (str): _description_

    Returns:
        _type_: _description_
    """
    if '\n' in str(message):
        return False, "", "", "请不要输入跨行的命令"
    m_lst = str(message).split()

    if len(m_lst) == 1:
        return True, float('inf'), 'all', ""
    if len(m_lst) == 2:
        item = m_lst[1]
        if item.isdigit():
            return True, int(item), 'all', ""
        else:
            return True, float('inf'), item, ""
    if len(m_lst) == 3:
        if "方舟抽卡分析" not in m_lst[0]:
            return False, "", "", "请将 方舟抽卡分析 放在命令开头"
        item1, item2 = m_lst[1:]
        if item1.isdigit() ^  item2.isdigit():#必须一个真一个假
            return False, "", "", "参数不合法"
        if item1.isdigit():
            return True, int(item1), item2, ""
        else:
            return True, int(item2), item1, ""
    if len(m_lst)>=4:
        return False, "", "", "参数过多"