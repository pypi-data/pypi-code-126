#!/usr/bin/env python
# coding=utf-8

"""
Version: 0.1
Autor: zmf96
Email: zmf96@qq.com
Date: 2022-06-03 19:23:50
LastEditors: zmf96
LastEditTime: 2022-06-03 21:09:20
FilePath: /hotfinger/finger_handle_tools/handle_14.py
Description: 
"""
import json

import bson
import pymysql
from cp_common.log import logger

# # 打开数据库连接
# db = pymysql.connect("177.7.0.13","root","xsC4sdf43aX","15finger")
db = pymysql.connect(
    host="177.7.0.13", user="root", passwd="xsC4sdf43aX", db="15finger"
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()


fingers = {}


def get_app():
    # SQL 查询语句
    sql = "SELECT * FROM api_app;"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # 打印结果
            # logger.info(row)
            get_app_finger(row[1], str(row[0]))
    except:
        logger.info("Error: unable to fetch data")


def get_app_finger(app_name, _id):
    try:
        sql = "select * from api_finger where app_id = %s" % _id
        cursor.execute(sql)
        results = cursor.fetchall()
        tmp = {
            "_id": {"$oid": str(bson.ObjectId())},
            "name": app_name,
            "content": get_content(results),
            "tags": ["14finger"],
        }
        fingers[app_name] = tmp

    except Exception as e:
        logger.info(app_name)
        logger.info(_id)
        logger.info(e)


def get_content(results):
    content = {}
    path_dict = {}
    for item in results:
        path = item[7]
        if not path:
            path = "/"
        if path in path_dict:
            path_dict[path].append(item)
        else:
            path_dict[path] = [item]
    for k, v in path_dict.items():
        ret = get_path(v)
        content[k] = ret
    try:
        return {"/": content["/"]}
    except Exception as e:
        logger.warning(e)
        return None


def get_path(results):
    ret = ""
    for item in results:
        if item[3] == "md5":
            ret = 'body_md5="' + item[2] + '"'
        else:
            _tmp = item[4] + '="' + item[2] + '"'
            if _tmp not in ret:
                if len(ret) > 1:
                    ret += " || "
                ret += _tmp
    return ret


def save2json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def getfinger():
    with open("../data/hotfinger_v5.json", "r") as f:
        hotfinger = json.load(f)
    return hotfinger


def main():
    get_app()
    save2json("./14finger.json", fingers)

    fingers_set = set(fingers)
    hotfinger_set = set()

    hotfinger = getfinger()
    for item in hotfinger:
        hotfinger_set.add(item["name"])

    difffinger = sorted(fingers_set - hotfinger_set)

    logger.info(difffinger)
    finger_v6 = []
    for item in difffinger:
        if fingers[item]["content"]:
            finger_v6.append(fingers[item])

    save2json("./finger_v6.json", finger_v6)


if __name__ == "__main__":
    main()
