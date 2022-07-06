import requests as req, time
import json
from collections import defaultdict as ddict
from .ark_drawer import ArkImage
from .ark_db import *
from .ark_setting import *
from .ark_utils import *
from math import ceil

def check_pool_name(pool_name):
    """_summary_
    检查卡池名称是否正确
    """
    if pool_name not in tot_pool_info.keys():  
        error_info = "错误的卡池名称！现有卡池名称如下:\n"
        pool_name_string = '\n'.join(tot_pool_info[:-1])
        return False, error_info + pool_name_string
    return True, ""
  
def url_scrawler(token:str):
    """_summary_
    爬取官网抽卡记录
    Args:
        token (str): _description_

    Returns:
        _type_: _description_
    """
    base_url = "https://ak.hypergryph.com/user/api/inquiry/gacha?page=PAGE_NUMBER&token="+token
    draw_info_list = []
    try:
        for i in range(1,11):
            page_url = base_url.replace('PAGE_NUMBER', str(i))
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            print(page_url)
            res_page = req.get(page_url, headers=headers)
            page_data = json.loads(res_page.text)['data']['list']
            if not page_data:
                break
            draw_info_list.extend(page_data)
        return True, "", draw_info_list
    except Exception as e:
        print(e)
        return False, "获取官网寻访信息失败", []



def user_ark_analyser(db:sq.Connection, user_info:str, max_read_count = float('inf'), pool_name = "all"):
    """_summary_
    抽卡分析主函数
    Args:
        db (pm.Connection): _description_
        user_info (str): _description_
        max_read_count (_type_, optional): _description_. Defaults to float('inf').

    Returns:
        _type_: _description_
    """
    user_id = user_info[0]
    user_name = user_info[1]
    token = user_info[2]
    #检查卡池名称 取消单卡池分析功能
    # pool_name_right, return_info = check_pool_name(pool_name)
    # if not pool_name_right: return False, return_info
    # print("完成检查")
    # 获取官网寻访记录
    scrawl_success, return_info, record_info_list = url_scrawler(token)
    if not scrawl_success: return False, return_info
    print("完成抓取")
    # 写数据库
    if not record_info_list: return False, "你最近没有抽卡，海猫在呼唤你！"
    write_success, return_info = url_db_writer(db, record_info_list, user_id)
    if not write_success:return False, return_info
    print("完成写入")
    # 读数据库
    db_reader = ArkDBReader(db, user_id, user_name, max_read_count, pool_name, tot_pool_info)
    db_reader.query_all()
    query_info = db_reader.query_result
    # 生成图片
    aig = ArkImage(query_info, user_id, db_reader.get_img_wh())
    aig.text_title(user_name, pool_name, db_reader.max_record_count)
    aig.draw_pie('star')
    aig.draw_histo('pool')
    aig.text_distribution('star')
    aig.text_distribution('shuiwei')

    aig.draw_char_query('star6char')        
    aig.draw_char_query('newchar')      
    aig_success, aig_save_path_desc = aig.save()  
    return aig_success, aig_save_path_desc

