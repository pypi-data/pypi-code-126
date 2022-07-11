# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 下午3:54
# @Author  : kyq
# @Software: PyCharm

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


import logging
import os
import sys
from bson.objectid import ObjectId

if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest

doc = {
    "_id": ObjectId("626b7eaa2186ff440d8c924b"),
    "title": "我们的婚姻",
    "programId": "620d2f2992c103091db1ede1",
    "doubanId": "35423605",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("61515e75a75eb73ca717cfd7"),
            "actorName": "沈严",
            "sex": 0,
            "doubanId": "1321171"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d44e"),
            "actorName": "刘海波",
            "sex": 0,
            "doubanId": "1322934"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6184f0277d060a0ac383fc14"),
            "actorName": "白百何",
            "sex": 1,
            "doubanId": "1275542"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e037"),
            "actorName": "佟大为",
            "sex": 0,
            "doubanId": "1009179"
        },
        {
            "_id": ObjectId("6135e0b1aab95f5ecdf5e3c7"),
            "actorName": "蒋欣",
            "sex": 1,
            "doubanId": "1314821"
        },
        {
            "_id": ObjectId("6135e150aab95f5ecdf5e956"),
            "actorName": "高叶",
            "sex": 1,
            "doubanId": "1322964"
        },
        {
            "_id": ObjectId("6135df8aaab95f5ecdf5df4f"),
            "actorName": "王骁",
            "sex": 0,
            "doubanId": "1314222"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d460"),
            "actorName": "是安",
            "sex": 0,
            "doubanId": "1319541"
        },
        {
            "_id": ObjectId("620d2f2892c103091db1edd5"),
            "actorName": "张哲华",
            "sex": 0,
            "doubanId": "1414494"
        },
        {
            "_id": ObjectId("6184f4d97d060a0ac384179a"),
            "actorName": "曹曦文",
            "sex": 1,
            "doubanId": "1274603"
        },
        {
            "_id": ObjectId("6133303baab95f5ecdf5c404"),
            "actorName": "张晨光",
            "sex": 0,
            "doubanId": "1275270"
        },
        {
            "_id": ObjectId("6133303baab95f5ecdf5c3fe"),
            "actorName": "邬君梅",
            "sex": 1,
            "doubanId": "1004773"
        },
        {
            "_id": ObjectId("6135e0b5aab95f5ecdf5e469"),
            "actorName": "佟悦",
            "sex": 0,
            "doubanId": "1313861"
        },
        {
            "_id": ObjectId("6135df3caab95f5ecdf5dd4a"),
            "actorName": "郑合惠子",
            "sex": 1,
            "doubanId": "1349498"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e031"),
            "actorName": "郝平",
            "sex": 0,
            "doubanId": "1313559"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9c4"),
            "actorName": "田小洁",
            "sex": 0,
            "doubanId": "1314851"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d91a"),
            "actorName": "杨新鸣",
            "sex": 0,
            "doubanId": "1275510"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd88"),
            "actorName": "谭凯",
            "sex": 0,
            "doubanId": "1275687"
        },
        {
            "_id": ObjectId("619f3a2ae10e4d121d655d89"),
            "actorName": "赵达",
            "sex": 0,
            "doubanId": "1322795"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.grpah.ActorRelationGraph"
}

doc1 = {
    "_id": ObjectId("626b6467bc76fd5d550b2479"),
    "title": "突围",
    "programId": "6173280eff99840c246de494",
    "doubanId": "27015861",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("61515e75a75eb73ca717cfd7"),
            "actorName": "沈严",
            "sex": 0,
            "doubanId": "1321171"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d44e"),
            "actorName": "刘海波",
            "sex": 0,
            "doubanId": "1322934"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da58"),
            "actorName": "靳东",
            "sex": 0,
            "doubanId": "1314123"
        },
        {
            "_id": ObjectId("6135de7eaab95f5ecdf5d5ca"),
            "actorName": "闫妮",
            "sex": 1,
            "doubanId": "1274496"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e307"),
            "actorName": "黄志忠",
            "sex": 0,
            "doubanId": "1255860"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da68"),
            "actorName": "陈晓",
            "sex": 0,
            "doubanId": "1325412"
        },
        {
            "_id": ObjectId("6135e0b5aab95f5ecdf5e437"),
            "actorName": "秦岚",
            "sex": 1,
            "doubanId": "1274294"
        },
        {
            "_id": ObjectId("6135e0ddaab95f5ecdf5e605"),
            "actorName": "耿乐",
            "sex": 0,
            "doubanId": "1274576"
        },
        {
            "_id": ObjectId("6135dddaaab95f5ecdf5d312"),
            "actorName": "田雷",
            "sex": 0,
            "doubanId": "1366396"
        },
        {
            "_id": ObjectId("6135de44aab95f5ecdf5d4aa"),
            "actorName": "黄品沅",
            "sex": 0,
            "doubanId": "1326050"
        },
        {
            "_id": ObjectId("6135dec9aab95f5ecdf5d874"),
            "actorName": "潘之琳",
            "sex": 1,
            "doubanId": "1275632"
        },
        {
            "_id": ObjectId("6135ddd2aab95f5ecdf5d2e6"),
            "actorName": "奚美娟",
            "sex": 1,
            "doubanId": "1001714"
        },
        {
            "_id": ObjectId("6173280eff99840c246de466"),
            "actorName": "王景春",
            "sex": 0,
            "doubanId": "1275934"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d91e"),
            "actorName": "高鑫",
            "sex": 0,
            "doubanId": "1274776"
        },
        {
            "_id": ObjectId("6173280eff99840c246de46a"),
            "actorName": "韩童生",
            "sex": 0,
            "doubanId": "1274722"
        },
        {
            "_id": ObjectId("6173280eff99840c246de46c"),
            "actorName": "高明",
            "sex": 0,
            "doubanId": "1009107"
        },
        {
            "_id": ObjectId("6133302faab95f5ecdf5c3bc"),
            "actorName": "侯明昊",
            "sex": 0,
            "doubanId": "1359141"
        },
        {
            "_id": ObjectId("6136befdaab95f5ecdf5ef88"),
            "actorName": "张萌",
            "sex": 1,
            "doubanId": "1275422"
        },
        {
            "_id": ObjectId("6173280eff99840c246de472"),
            "actorName": "陈瑾",
            "sex": 1,
            "doubanId": "1309215"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e031"),
            "actorName": "郝平",
            "sex": 0,
            "doubanId": "1313559"
        },
        {
            "_id": ObjectId("6137d3c503ce86576611751f"),
            "actorName": "冯嘉怡",
            "sex": 0,
            "doubanId": "1317068"
        },
        {
            "_id": ObjectId("6135e140aab95f5ecdf5e8b2"),
            "actorName": "李洪涛",
            "sex": 0,
            "doubanId": "1317230"
        },
        {
            "_id": ObjectId("6135d968aab95f5ecdf5cb36"),
            "actorName": "涂松岩",
            "sex": 0,
            "doubanId": "1276048"
        },
        {
            "_id": ObjectId("6135ddf2aab95f5ecdf5d360"),
            "actorName": "代露娃",
            "sex": 1,
            "doubanId": "1404001"
        },
        {
            "_id": ObjectId("6135dd23aab95f5ecdf5d03a"),
            "actorName": "秦焰",
            "sex": 0,
            "doubanId": "1318605"
        },
        {
            "_id": ObjectId("6135db5baab95f5ecdf5cb82"),
            "actorName": "丁勇岱",
            "sex": 0,
            "doubanId": "1314975"
        },
        {
            "_id": ObjectId("6135ded2aab95f5ecdf5d898"),
            "actorName": "王阳",
            "sex": 0,
            "doubanId": "1323174"
        },
        {
            "_id": ObjectId("6173280eff99840c246de484"),
            "actorName": "句号",
            "sex": 0,
            "doubanId": "1287953"
        },
        {
            "_id": ObjectId("6135dcb6aab95f5ecdf5cde8"),
            "actorName": "来喜",
            "sex": 0,
            "doubanId": "1321645"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d460"),
            "actorName": "是安",
            "sex": 0,
            "doubanId": "1319541"
        },
        {
            "_id": ObjectId("6173280eff99840c246de48a"),
            "actorName": "荣飞",
            "sex": 0,
            "doubanId": "1449563"
        },
        {
            "_id": ObjectId("6135dcdbaab95f5ecdf5cf56"),
            "actorName": "韦奕波",
            "sex": 0,
            "doubanId": "1422829"
        },
        {
            "_id": ObjectId("6135d964aab95f5ecdf5cafe"),
            "actorName": "周璞",
            "sex": 0,
            "doubanId": "1343475"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bae"),
            "actorName": "何琳",
            "sex": 1,
            "doubanId": "1044222"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bb0"),
            "actorName": "宫晓瑄",
            "sex": 1,
            "doubanId": "1275543"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bb2"),
            "actorName": "冯鹏",
            "sex": 0,
            "doubanId": "1319036"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bb4"),
            "actorName": "王嘉绮",
            "sex": 1,
            "doubanId": "1409360"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd5c"),
            "actorName": "李强",
            "sex": 0,
            "doubanId": "1274810"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bb8"),
            "actorName": "任东霖",
            "sex": 0,
            "doubanId": "1021981"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bba"),
            "actorName": "王欧蕾",
            "sex": 1,
            "doubanId": "1394249"
        },
        {
            "_id": ObjectId("6135e0b5aab95f5ecdf5e469"),
            "actorName": "佟悦",
            "sex": 0,
            "doubanId": "1313861"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bbe"),
            "actorName": "唐旭",
            "sex": 0,
            "doubanId": "1334343"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bc0"),
            "actorName": "李彦达",
            "sex": 0,
            "doubanId": "1463552"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bc2"),
            "actorName": "刘鑫凯",
            "sex": 0,
            "doubanId": "1463553"
        },
        {
            "_id": ObjectId("61418cce9b773c05a61bf030"),
            "actorName": "邹元清",
            "sex": 1,
            "doubanId": "1375319"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bc6"),
            "actorName": "郭洺宇",
            "sex": 0,
            "doubanId": "1376398"
        },
        {
            "_id": ObjectId("6135e020aab95f5ecdf5e12b"),
            "actorName": "高蓓蓓",
            "sex": 1,
            "doubanId": "1315396"
        },
        {
            "_id": ObjectId("6135deb6aab95f5ecdf5d768"),
            "actorName": "张皓然",
            "sex": 0,
            "doubanId": "1331394"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bcc"),
            "actorName": "翟万臣",
            "sex": 0,
            "doubanId": "1318266"
        },
        {
            "_id": ObjectId("6135e07aaab95f5ecdf5e35b"),
            "actorName": "徐绍瑛",
            "sex": 0,
            "doubanId": "1423003"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bd0"),
            "actorName": "李文玲",
            "sex": 1,
            "doubanId": "1323213"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd5e"),
            "actorName": "陈逸恒",
            "sex": 0,
            "doubanId": "1318303"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bd4"),
            "actorName": "杨小冬",
            "sex": 0,
            "doubanId": "1412369"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bd6"),
            "actorName": "于越",
            "sex": 1,
            "doubanId": "1319038"
        },
        {
            "_id": ObjectId("6173280eff99840c246de490"),
            "actorName": "孟祥亮",
            "sex": 0,
            "doubanId": "1430720"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bda"),
            "actorName": "曹凯",
            "sex": 0,
            "doubanId": "1440437"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbba"),
            "actorName": "赫雷",
            "sex": 0,
            "doubanId": "1400410"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da98"),
            "actorName": "刘天佐",
            "sex": 0,
            "doubanId": "1318324"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd88"),
            "actorName": "谭凯",
            "sex": 0,
            "doubanId": "1275687"
        },
        {
            "_id": ObjectId("6135df13aab95f5ecdf5dc82"),
            "actorName": "海一天",
            "sex": 0,
            "doubanId": "1313672"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0be4"),
            "actorName": "王丽涵",
            "sex": 1,
            "doubanId": "1325769"
        },
        {
            "_id": ObjectId("6135de58aab95f5ecdf5d53e"),
            "actorName": "夏侯镔",
            "sex": 0,
            "doubanId": "1323758"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0be8"),
            "actorName": "赵科",
            "sex": 0,
            "doubanId": "1365836"
        },
        {
            "_id": ObjectId("6135e0b5aab95f5ecdf5e46f"),
            "actorName": "徐晟",
            "sex": 0,
            "doubanId": "1376613"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bec"),
            "actorName": "陈旺林",
            "sex": 0,
            "doubanId": "1325172"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd4c"),
            "actorName": "郭广平",
            "sex": 0,
            "doubanId": "1318073"
        },
        {
            "_id": ObjectId("617f0462ff99840c246e0bf0"),
            "actorName": "赵立新",
            "sex": 0,
            "doubanId": "1312817"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.grpah.ActorRelationGraph"
}

doc2 = {
    "_id": ObjectId("6275eaba8024fe13f66583fc"),
    "title": "功勋",
    "programId": "61515e75a75eb73ca717d019",
    "doubanId": "34951103",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("61515e75a75eb73ca717cfd5"),
            "actorName": "郑晓龙",
            "sex": 0,
            "doubanId": "1303060"
        },
        {
            "_id": ObjectId("6135e0e2aab95f5ecdf5e647"),
            "actorName": "毛卫宁",
            "sex": 0,
            "doubanId": "1318245"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717cfd7"),
            "actorName": "沈严",
            "sex": 0,
            "doubanId": "1321171"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717cfdf"),
            "actorName": "康洪雷",
            "sex": 0,
            "doubanId": "1314924"
        },
        {
            "_id": ObjectId("6135dcf2aab95f5ecdf5cfac"),
            "actorName": "杨阳",
            "sex": 1,
            "doubanId": "1319424"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717cfd9"),
            "actorName": "林楠",
            "sex": 0,
            "doubanId": "1357492"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717cfdb"),
            "actorName": "杨文军",
            "sex": 0,
            "doubanId": "1318406"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e301"),
            "actorName": "阎建钢",
            "sex": 0,
            "doubanId": "1318150"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("61332ffbaab95f5ecdf5c1a2"),
            "actorName": "王雷",
            "sex": 0,
            "doubanId": "1275487"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e045"),
            "actorName": "雷佳音",
            "sex": 0,
            "doubanId": "1312940"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9b2"),
            "actorName": "郭涛",
            "sex": 0,
            "doubanId": "1274274"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d988"),
            "actorName": "黄晓明",
            "doubanId": "1041404"
        },
        {
            "_id": ObjectId("6135e0b1aab95f5ecdf5e3c7"),
            "actorName": "蒋欣",
            "sex": 1,
            "doubanId": "1314821"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e037"),
            "actorName": "佟大为",
            "sex": 0,
            "doubanId": "1009179"
        },
        {
            "_id": ObjectId("614ac7aaa75eb73ca717b25a"),
            "actorName": "周迅",
            "doubanId": "1027798"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e307"),
            "actorName": "黄志忠",
            "sex": 0,
            "doubanId": "1255860"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8ae"),
            "actorName": "邵汶",
            "sex": 0,
            "doubanId": "1330994"
        },
        {
            "_id": ObjectId("61332ffbaab95f5ecdf5c1ca"),
            "actorName": "郝荣光",
            "sex": 0,
            "doubanId": "1379970"
        },
        {
            "_id": ObjectId("6135e0e2aab95f5ecdf5e6ed"),
            "actorName": "鲁诺",
            "sex": 0,
            "doubanId": "1321098"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db9a"),
            "actorName": "孙锡堃",
            "sex": 0,
            "doubanId": "1328092"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717cff7"),
            "actorName": "倪妮",
            "sex": 1,
            "doubanId": "1315861"
        },
        {
            "_id": ObjectId("6135e020aab95f5ecdf5e10f"),
            "actorName": "杨烁",
            "sex": 0,
            "doubanId": "1275708"
        },
        {
            "_id": ObjectId("6135df8aaab95f5ecdf5df4f"),
            "actorName": "王骁",
            "sex": 0,
            "doubanId": "1314222"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d460"),
            "actorName": "是安",
            "sex": 0,
            "doubanId": "1319541"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9c4"),
            "actorName": "田小洁",
            "sex": 0,
            "doubanId": "1314851"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8c0"),
            "actorName": "柯宇",
            "sex": 1,
            "doubanId": "1402124"
        },
        {
            "_id": ObjectId("6135e020aab95f5ecdf5e11b"),
            "actorName": "李添诺",
            "sex": 0,
            "doubanId": "1334556"
        },
        {
            "_id": ObjectId("6135dde0aab95f5ecdf5d32e"),
            "actorName": "尤勇智",
            "sex": 0,
            "doubanId": "1301518"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db86"),
            "actorName": "胡可",
            "sex": 1,
            "doubanId": "1274939"
        },
        {
            "_id": ObjectId("6135dde0aab95f5ecdf5d334"),
            "actorName": "李野萍",
            "sex": 1,
            "doubanId": "1321933"
        },
        {
            "_id": ObjectId("6135dec8aab95f5ecdf5d844"),
            "actorName": "白凡",
            "sex": 0,
            "doubanId": "1317979"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9c6"),
            "actorName": "刚毅",
            "sex": 0,
            "doubanId": "1317991"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8ce"),
            "actorName": "马佳玛尧",
            "sex": 0,
            "doubanId": "1417784"
        },
        {
            "_id": ObjectId("6135dee1aab95f5ecdf5d94c"),
            "actorName": "孙茜",
            "sex": 1,
            "doubanId": "1318082"
        },
        {
            "_id": ObjectId("6135db5baab95f5ecdf5cb82"),
            "actorName": "丁勇岱",
            "sex": 0,
            "doubanId": "1314975"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8d4"),
            "actorName": "娄乃鸣",
            "sex": 1,
            "doubanId": "1316665"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8d6"),
            "actorName": "迟蓬",
            "doubanId": "1314926"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8d8"),
            "actorName": "罗京民",
            "sex": 0,
            "doubanId": "1313471"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8da"),
            "actorName": "刘小蕙",
            "sex": 1,
            "doubanId": "1325376"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8dc"),
            "actorName": "德姬",
            "doubanId": "1327727"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d005"),
            "actorName": "陈好",
            "sex": 1,
            "doubanId": "1037748"
        },
        {
            "_id": ObjectId("6136c024aab95f5ecdf5f926"),
            "actorName": "章贺",
            "sex": 0,
            "doubanId": "1320522"
        },
        {
            "_id": ObjectId("6135de50aab95f5ecdf5d4ce"),
            "actorName": "黄小蕾",
            "sex": 1,
            "doubanId": "1316146"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d00b"),
            "actorName": "王洛勇",
            "sex": 0,
            "doubanId": "1274819"
        },
        {
            "_id": ObjectId("6135ded2aab95f5ecdf5d8a8"),
            "actorName": "宿宇杰",
            "sex": 0,
            "doubanId": "1355787"
        },
        {
            "_id": ObjectId("61613001a75eb73ca7180e1f"),
            "actorName": "管云鹏",
            "sex": 0,
            "doubanId": "1365814"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d011"),
            "actorName": "陈震",
            "sex": 0,
            "doubanId": "1374512"
        },
        {
            "_id": ObjectId("61613001a75eb73ca7180e23"),
            "actorName": "夷永定",
            "sex": 0,
            "doubanId": "1462622"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db3e"),
            "actorName": "王鑫",
            "sex": 0,
            "doubanId": "1335594"
        },
        {
            "_id": ObjectId("6136bf5eaab95f5ecdf5f3e0"),
            "actorName": "张凯丽",
            "sex": 1,
            "doubanId": "1030951"
        },
        {
            "_id": ObjectId("61333004aab95f5ecdf5c1f2"),
            "actorName": "倪萍",
            "sex": 1,
            "doubanId": "1305386"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8e8"),
            "actorName": "孟阿赛",
            "sex": 0,
            "doubanId": "1351562"
        },
        {
            "_id": ObjectId("61613001a75eb73ca7180e2d"),
            "actorName": "张洪杰",
            "sex": 0,
            "doubanId": "1315645"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daea"),
            "actorName": "左小青",
            "sex": 1,
            "doubanId": "1274978"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e325"),
            "actorName": "迟帅",
            "sex": 0,
            "doubanId": "1274879"
        },
        {
            "_id": ObjectId("6135e0adaab95f5ecdf5e393"),
            "actorName": "李光洁",
            "sex": 0,
            "doubanId": "1275178"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e039"),
            "actorName": "陈赫",
            "sex": 0,
            "doubanId": "1313841"
        },
        {
            "_id": ObjectId("61613001a75eb73ca7180e37"),
            "actorName": "王菁华",
            "sex": 1,
            "doubanId": "1322293"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd84"),
            "actorName": "邢岷山",
            "doubanId": "1317860"
        },
        {
            "_id": ObjectId("6135e0ddaab95f5ecdf5e5ef"),
            "actorName": "刘宇宁",
            "sex": 0,
            "doubanId": "1401585"
        },
        {
            "_id": ObjectId("61613001a75eb73ca7180e3d"),
            "actorName": "菅纫姿",
            "sex": 1,
            "doubanId": "1328420"
        },
        {
            "_id": ObjectId("6135e150aab95f5ecdf5e94e"),
            "actorName": "孙俪",
            "doubanId": "1004856"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d45a"),
            "actorName": "刘奕君",
            "sex": 0,
            "doubanId": "1322731"
        },
        {
            "_id": ObjectId("6135e0b1aab95f5ecdf5e3e9"),
            "actorName": "王自健",
            "doubanId": "1326390"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd4a"),
            "actorName": "王亚楠",
            "sex": 0,
            "doubanId": "1275110"
        },
        {
            "_id": ObjectId("6135e0e2aab95f5ecdf5e64f"),
            "actorName": "朱刚日尧",
            "sex": 0,
            "doubanId": "1314181"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d003"),
            "actorName": "张颂文",
            "sex": 0,
            "doubanId": "1314329"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5da2c"),
            "actorName": "陈宝国",
            "sex": 0,
            "doubanId": "1274584"
        },
        {
            "_id": ObjectId("6135ddd2aab95f5ecdf5d2e6"),
            "actorName": "奚美娟",
            "sex": 1,
            "doubanId": "1001714"
        },
        {
            "_id": ObjectId("6135d964aab95f5ecdf5cac4"),
            "actorName": "于荣光",
            "sex": 0,
            "doubanId": "1274556"
        },
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef18"),
            "actorName": "董洁",
            "sex": 1,
            "doubanId": "1001074"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e305"),
            "actorName": "任重",
            "sex": 0,
            "doubanId": "1315001"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbae"),
            "actorName": "蒋梦婕",
            "sex": 1,
            "doubanId": "1276049"
        },
        {
            "_id": ObjectId("6135e05baab95f5ecdf5e29d"),
            "actorName": "柴隽哲",
            "sex": 0,
            "doubanId": "1453838"
        },
        {
            "_id": ObjectId("6135e05baab95f5ecdf5e2b1"),
            "actorName": "威力斯",
            "sex": 0,
            "doubanId": "1381291"
        },
        {
            "_id": ObjectId("6135def1aab95f5ecdf5dc66"),
            "actorName": "李祉默",
            "sex": 1,
            "doubanId": "1450062"
        },
        {
            "_id": ObjectId("614f8e42a75eb73ca717c689"),
            "actorName": "李依蒙",
            "sex": 1,
            "doubanId": "1461745"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d015"),
            "actorName": "赵爱诚",
            "sex": 1,
            "doubanId": "1460979"
        },
        {
            "_id": ObjectId("61515e75a75eb73ca717d013"),
            "actorName": "王文强",
            "sex": 0,
            "doubanId": "1448458"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.grpah.ActorRelationGraph"
}


doc3 = {
    "_id": ObjectId("6275ef0f8838d13eedd53cb0"),
    "title": "冰雪之名",
    "programId": "61eedc746bdd9c0991a2088b",
    "doubanId": "35370815",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("6135dc78aab95f5ecdf5cc70"),
            "actorName": "白涛",
            "sex": 0,
            "doubanId": "1387783"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6133302faab95f5ecdf5c3ba"),
            "actorName": "欧豪",
            "sex": 0,
            "doubanId": "1337644"
        },
        {
            "_id": ObjectId("6135dc97aab95f5ecdf5ccb4"),
            "actorName": "梁洁",
            "sex": 1,
            "doubanId": "1374407"
        },
        {
            "_id": ObjectId("6135e0b1aab95f5ecdf5e3c7"),
            "actorName": "蒋欣",
            "sex": 1,
            "doubanId": "1314821"
        },
        {
            "_id": ObjectId("6135dd86aab95f5ecdf5d110"),
            "actorName": "陈若轩",
            "sex": 0,
            "doubanId": "1348101"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da74"),
            "actorName": "彭小苒",
            "sex": 1,
            "doubanId": "1344792"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9f8"),
            "actorName": "伊丽媛",
            "sex": 1,
            "doubanId": "1426577"
        },
        {
            "_id": ObjectId("6184f7917d060a0ac384245a"),
            "actorName": "张峻鸣",
            "sex": 0,
            "doubanId": "1356938"
        },
        {
            "_id": ObjectId("61eedc746bdd9c0991a20885"),
            "actorName": "刘显达",
            "sex": 0,
            "doubanId": "1362214"
        },
        {
            "_id": ObjectId("61450210a75eb73ca7178f04"),
            "actorName": "蔡子伦",
            "sex": 0,
            "doubanId": "1328046"
        },
        {
            "_id": ObjectId("6135e033aab95f5ecdf5e209"),
            "actorName": "万籽麟",
            "sex": 1,
            "doubanId": "1428425"
        },
        {
            "_id": ObjectId("6135dc78aab95f5ecdf5cc7e"),
            "actorName": "刘卫华",
            "sex": 0,
            "doubanId": "1316359"
        },
        {
            "_id": ObjectId("6135e0b1aab95f5ecdf5e3e7"),
            "actorName": "周德华",
            "sex": 0,
            "doubanId": "1318117"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.grpah.ActorRelationGraph"
}


doc5 = {
    "_id": ObjectId("627c801cffaa56759c79947f"),
    "title": "日日妈妈声2",
    "programId": "62794a28db465d619844083e",
    "doubanId": "35891956",
    "type": 0,
    "cast": [
        {
            "_id": ObjectId("62794a28db465d6198440838"),
            "actorName": "余安安",
            "sex": 1,
            "doubanId": "1301560"
        },
        {
            "_id": ObjectId("62794a28db465d619844083a"),
            "actorName": "陈凯琳",
            "sex": 1,
            "doubanId": "1342251"
        },
        {
            "_id": ObjectId("62794a28db465d619844083c"),
            "actorName": "罗敏庄",
            "doubanId": "1017475"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}


doc6 = {
    "_id": ObjectId("627dec018101946a52dced24"),
    "title": "且试天下",
    "programId": "619da4cd2bc7fc52ae3de924",
    "doubanId": "26339609",
    "type":0,
    "director": [
        {
            "_id": ObjectId("6135dfcdaab95f5ecdf5dfb1"),
            "actorName": "尹涛",
            "sex":0,
            "doubanId": "1371155"
        },
        {
            "_id": ObjectId("618cdbe97d060a0ac384db4a"),
            "actorName": "于永刚",
            "doubanId": "1398227"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135df3caab95f5ecdf5dd42"),
            "actorName": "杨洋",
            "sex":0,
            "doubanId": "1276051"
        },
        {
            "_id": ObjectId("6135dfd2aab95f5ecdf5e04d"),
            "actorName": "赵露思",
            "sex":1,
            "doubanId": "1385770"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d1f8"),
            "actorName": "宣璐",
            "sex":1,
            "doubanId": "1323763"
        },
        {
            "_id": ObjectId("6135dfcdaab95f5ecdf5dfbf"),
            "actorName": "赖艺",
            "sex":0,
            "doubanId": "1351258"
        },
        {
            "_id": ObjectId("6184f0ef7d060a0ac384021e"),
            "actorName": "贺开朗",
            "sex":0,
            "doubanId": "1445208"
        },
        {
            "_id": ObjectId("6135e12caab95f5ecdf5e7fb"),
            "actorName": "张丰毅",
            "sex":0,
            "doubanId": "1050265"
        },
        {
            "_id": ObjectId("6136bf06aab95f5ecdf5f05e"),
            "actorName": "李若彤",
            "sex":1,
            "doubanId": "1023476"
        },
        {
            "_id": ObjectId("6135d964aab95f5ecdf5cacc"),
            "actorName": "张天阳",
            "sex":0,
            "doubanId": "1339958"
        },
        {
            "_id": ObjectId("6135de6baab95f5ecdf5d5a6"),
            "actorName": "刘芮麟",
            "sex":0,
            "doubanId": "1339588"
        },
        {
            "_id": ObjectId("619da4cd2bc7fc52ae3de920"),
            "actorName": "邢韵嘉",
            "sex":1,
            "doubanId": "1462486"
        },
        {
            "_id": ObjectId("619da4cd2bc7fc52ae3de922"),
            "actorName": "李乾锋",
            "sex":0,
            "doubanId": "1375394"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc7 = {
    "_id": ObjectId("627debb38101946a52dced21"),
    "title": "特战荣耀",
    "programId": "619d95d02bc7fc52ae3de7fb",
    "doubanId": "30284118",
    "type":0,
    "writer": [
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d90e"),
            "actorName": "徐纪周",
            "sex":0,
            "doubanId": "1317195"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135df3caab95f5ecdf5dd42"),
            "actorName": "杨洋",
            "sex":0,
            "doubanId": "1276051"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cb90"),
            "actorName": "李一桐",
            "sex":1,
            "doubanId": "1354284"
        },
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef2a"),
            "actorName": "蒋璐霞",
            "sex":1,
            "doubanId": "1313597"
        },
        {
            "_id": ObjectId("615b6b92a75eb73ca717f8e8"),
            "actorName": "孟阿赛",
            "sex":0,
            "doubanId": "1351562"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d91e"),
            "actorName": "高鑫",
            "sex":0,
            "doubanId": "1274776"
        },
        {
            "_id": ObjectId("613924f803ce86576611767c"),
            "actorName": "蒋龙",
            "sex":0,
            "doubanId": "1359404"
        },
        {
            "_id": ObjectId("619d95d02bc7fc52ae3de7ef"),
            "actorName": "柳文欢",
            "sex":0,
            "doubanId": "1406672"
        },
        {
            "_id": ObjectId("6135de7eaab95f5ecdf5d5dc"),
            "actorName": "刘硕",
            "sex":0,
            "doubanId": "1366545"
        },
        {
            "_id": ObjectId("619d95d02bc7fc52ae3de7f3"),
            "actorName": "杨彤",
            "sex":0,
            "doubanId": "1356618"
        },
        {
            "_id": ObjectId("619d95d02bc7fc52ae3de7f5"),
            "actorName": "赵震宇",
            "sex":0,
            "doubanId": "1373322"
        },
        {
            "_id": ObjectId("619d95d02bc7fc52ae3de7f7"),
            "actorName": "陈慧康",
            "sex":0,
            "doubanId": "1429538"
        },
        {
            "_id": ObjectId("619d95d02bc7fc52ae3de7f9"),
            "actorName": "杰古",
            "sex":0,
            "doubanId": "1442704"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}


doc8= {
    "_id": ObjectId("627df0e38101946a52dced78"),
    "title": "传家",
    "programId": "61eedc7d6bdd9c0991a208c4",
    "doubanId": "30464581",
    "type":0,
    "director": [
        {
            "_id": ObjectId("619d93f22bc7fc52ae3de78a"),
            "actorName": "王威",
            "sex":0,
            "doubanId": "1440107"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135e0b5aab95f5ecdf5e437"),
            "actorName": "秦岚",
            "sex":1,
            "doubanId": "1274294"
        },
        {
            "_id": ObjectId("6133301caab95f5ecdf5c2c8"),
            "actorName": "韩庚",
            "doubanId": "1275667"
        },
        {
            "_id": ObjectId("6135e141aab95f5ecdf5e8e0"),
            "actorName": "吴谨言",
            "sex":1,
            "doubanId": "1337020"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9a0"),
            "actorName": "聂远",
            "sex":0,
            "doubanId": "1275718"
        },
        {
            "_id": ObjectId("61333025aab95f5ecdf5c35c"),
            "actorName": "刘钧",
            "sex":0,
            "doubanId": "1314921"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cba6"),
            "actorName": "苗圃",
            "sex":1,
            "doubanId": "1033846"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cba0"),
            "actorName": "张楠",
            "sex":1,
            "doubanId": "1375486"
        },
        {
            "_id": ObjectId("6135de7eaab95f5ecdf5d5ce"),
            "actorName": "张逸杰",
            "sex":0,
            "doubanId": "1341220"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cb9a"),
            "actorName": "何奉天",
            "sex":0,
            "doubanId": "1363930"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d20a"),
            "actorName": "郑凯",
            "sex":0,
            "doubanId": "1316093"
        },
        {
            "_id": ObjectId("6135dc78aab95f5ecdf5cc7c"),
            "actorName": "郑国霖",
            "sex":0,
            "doubanId": "1275878"
        },
        {
            "_id": ObjectId("618ae6d77d060a0ac384d6c5"),
            "actorName": "张译兮",
            "doubanId": "1399232"
        },
        {
            "_id": ObjectId("6135de8baab95f5ecdf5d612"),
            "actorName": "方安娜",
            "doubanId": "1313869"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d1f2"),
            "actorName": "汪汐潮",
            "sex":0,
            "doubanId": "1326518"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbbc"),
            "actorName": "何佳怡",
            "sex":1,
            "doubanId": "1318149"
        },
        {
            "_id": ObjectId("6135def1aab95f5ecdf5dc60"),
            "actorName": "王可如",
            "sex":1,
            "doubanId": "1366845"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208ad"),
            "actorName": "刘璐",
            "doubanId": "1376836"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbb4"),
            "actorName": "郑龙",
            "doubanId": "1393225"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208b0"),
            "actorName": "常铖",
            "sex":0,
            "doubanId": "1423589"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208b2"),
            "actorName": "张婕婕",
            "doubanId": "1414699"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208b4"),
            "actorName": "刘益嫣",
            "sex":1,
            "doubanId": "1454255"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208b6"),
            "actorName": "安安",
            "sex":1,
            "doubanId": "1399975"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208b8"),
            "actorName": "韩伯维",
            "sex":0,
            "doubanId": "1402524"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208ba"),
            "actorName": "美浓轮泰史",
            "sex":0,
            "doubanId": "1354011"
        },
        {
            "_id": ObjectId("61e14cfaf1b8d17f6261955b"),
            "actorName": "卢勇",
            "sex":0,
            "doubanId": "1355552"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbbe"),
            "actorName": "沈保平",
            "sex":0,
            "doubanId": "1319363"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbe6"),
            "actorName": "许榕真",
            "sex":1,
            "doubanId": "1316750"
        },
        {
            "_id": ObjectId("6135e0cbaab95f5ecdf5e51f"),
            "actorName": "邓莎",
            "sex":1,
            "doubanId": "1313740"
        },
        {
            "_id": ObjectId("61eedc7d6bdd9c0991a208c0"),
            "actorName": "汪以时",
            "sex":0,
            "doubanId": "1426270"
        },
        {
            "_id": ObjectId("6135e0adaab95f5ecdf5e3a5"),
            "actorName": "姜瑞霖",
            "sex":0,
            "doubanId": "1448203"
        },
        {
            "_id": ObjectId("6133303faab95f5ecdf5c452"),
            "actorName": "齐尔洛",
            "sex":0,
            "doubanId": "1452417"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc9 = {
    "_id": ObjectId("627dec548101946a52dced26"),
    "title": "尚食",
    "programId": "619d93f22bc7fc52ae3de79b",
    "doubanId": "30463682",
    "type":0,
    "director": [
        {
            "_id": ObjectId("619d93f22bc7fc52ae3de78a"),
            "actorName": "王威",
            "sex":0,
            "doubanId": "1440107"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cb92"),
            "actorName": "许凯",
            "sex":0,
            "doubanId": "1383033"
        },
        {
            "_id": ObjectId("6135e141aab95f5ecdf5e8e0"),
            "actorName": "吴谨言",
            "sex":1,
            "doubanId": "1337020"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cba2"),
            "actorName": "何瑞贤",
            "sex":1,
            "doubanId": "1359523"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cba0"),
            "actorName": "张楠",
            "sex":1,
            "doubanId": "1375486"
        },
        {
            "_id": ObjectId("6167c827a75eb73ca71825e6"),
            "actorName": "王楚然",
            "sex":1,
            "doubanId": "1375836"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d216"),
            "actorName": "张芷溪",
            "sex":1,
            "doubanId": "1323727"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cb9e"),
            "actorName": "王一哲",
            "doubanId": "1397908"
        },
        {
            "_id": ObjectId("6135d964aab95f5ecdf5cac4"),
            "actorName": "于荣光",
            "sex":0,
            "doubanId": "1274556"
        },
        {
            "_id": ObjectId("6135e065aab95f5ecdf5e31f"),
            "actorName": "洪剑涛",
            "sex":0,
            "doubanId": "1274654"
        },
        {
            "_id": ObjectId("6133303faab95f5ecdf5c448"),
            "actorName": "刘敏",
            "sex":1,
            "doubanId": "1275658"
        },
        {
            "_id": ObjectId("6135df76aab95f5ecdf5df11"),
            "actorName": "练练",
            "sex":1,
            "doubanId": "1315828"
        },
        {
            "_id": ObjectId("6135ddccaab95f5ecdf5d2a0"),
            "actorName": "姚童",
            "sex":1,
            "doubanId": "1429767"
        },
        {
            "_id": ObjectId("6136bfc2aab95f5ecdf5f67e"),
            "actorName": "王艳",
            "sex":1,
            "doubanId": "1274509"
        },
        {
            "_id": ObjectId("6135dcdbaab95f5ecdf5cf62"),
            "actorName": "韩帅",
            "sex":0,
            "doubanId": "1349794"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc10 = {
    "_id": ObjectId("6286082412552b533c798d87"),
    "title": "新围棋少年",
    "programId": "625d0e00db465d619843ff3f",
    "doubanId": "26980013",
    "type": 0,
    "writer": [
        {
            "_id": ObjectId("6286081b12552b533c798d85"),
            "actorName": "孙晓松",
            "sex": 0,
            "doubanId": "1342906"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc11 = {
    "_id": ObjectId("628de679cdac022bf6581858"),
    "title": "野生厨房 第二季",
    "programId": "6184f9637d060a0ac38424da",
    "doubanId": "34891743",
    "type": 1,
    "director": [
        {
            "_id": ObjectId("628b691299681c6979a93597"),
            "actorName": "黄磊",
            "doubanId": "1446838"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db66"),
            "actorName": "汪涵",
            "sex": 0,
            "doubanId": "1312937"
        },
        {
            "_id": ObjectId("6136bff7aab95f5ecdf5f7e4"),
            "actorName": "林依轮",
            "doubanId": "1313324"
        },
        {
            "_id": ObjectId("6135e150aab95f5ecdf5e97e"),
            "actorName": "姜妍",
            "sex": 1,
            "doubanId": "1318859"
        },
        {
            "_id": ObjectId("6136bf0baab95f5ecdf5f0f4"),
            "actorName": "汪苏泷",
            "doubanId": "1374972"
        },
        {
            "_id": ObjectId("6184f9637d060a0ac38424d8"),
            "actorName": "柳任",
            "sex": 0,
            "doubanId": "1426497"
        }
    ],
    "producer": [
        {
            "_id": ObjectId("6136bff9aab95f5ecdf5f7ec"),
            "actorName": "俞杭英",
            "doubanId": "1403998"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc12 = {
    "_id": ObjectId("62903c927eaba44f313b7967"),
    "title": "司藤",
    "programId": "6135dd04aab95f5ecdf5cfee",
    "doubanId": "27605542",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfc4"),
            "actorName": "李木戈",
            "sex": 0,
            "doubanId": "1324156"
        }
    ],
    "assistantDirector": [
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfec"),
            "actorName": "郭淼鑫",
            "sex": 0,
            "doubanId": "1412010"
        }
    ],
    "writer": [
        {
            "_id": ObjectId("628df0f899681c6979a9c8fd"),
            "actorName": "李旻",
            "doubanId": "1448790"
        },
        {
            "_id": ObjectId("628df0f899681c6979a9c8ff"),
            "actorName": "汪洪",
            "sex": 1,
            "doubanId": "1448791"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfc6"),
            "actorName": "景甜",
            "sex": 1,
            "doubanId": "1275432"
        },
        {
            "_id": ObjectId("6135d968aab95f5ecdf5cb2a"),
            "actorName": "张彬彬",
            "sex": 0,
            "doubanId": "1349994"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfca"),
            "actorName": "李沐宸",
            "sex": 1,
            "doubanId": "1369029"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfcc"),
            "actorName": "张亦驰",
            "sex": 0,
            "doubanId": "1356221"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfce"),
            "actorName": "吴俊余",
            "sex": 0,
            "doubanId": "1315986"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfd0"),
            "actorName": "金泽灏",
            "doubanId": "1341898"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd8e"),
            "actorName": "邵峰",
            "sex": 0,
            "doubanId": "1315418"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfd4"),
            "actorName": "潘一祎",
            "sex": 1,
            "doubanId": "1429894"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfd6"),
            "actorName": "李依晓",
            "sex": 1,
            "doubanId": "1314761"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfd8"),
            "actorName": "袁成杰",
            "doubanId": "1315027"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfda"),
            "actorName": "陈芷琰",
            "sex": 1,
            "doubanId": "1435181"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfc4"),
            "actorName": "李木戈",
            "sex": 0,
            "doubanId": "1324156"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfde"),
            "actorName": "张定涵",
            "sex": 1,
            "doubanId": "1318242"
        },
        {
            "_id": ObjectId("62603dc6db465d619844006b"),
            "actorName": "吕行",
            "doubanId": "1313870"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfe2"),
            "actorName": "石蕊",
            "sex": 1,
            "doubanId": "1382096"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfe4"),
            "actorName": "郭赫轩",
            "sex": 0,
            "doubanId": "1410498"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfe6"),
            "actorName": "于觐源",
            "sex": 0,
            "doubanId": "1449406"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfe8"),
            "actorName": "贺颖怡",
            "sex": 1,
            "doubanId": "1447655"
        },
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfea"),
            "actorName": "师悦玲",
            "sex": 1,
            "doubanId": "1428160"
        }
    ],
    "producer": [
        {
            "_id": ObjectId("628c501e99681c6979a94751"),
            "actorName": "戴玮",
            "sex": 0,
            "doubanId": "1381892"
        },
        {
            "_id": ObjectId("628b49d999681c6979a9218b"),
            "actorName": "谢颖",
            "sex": 1,
            "doubanId": "1424487"
        },
        {
            "_id": ObjectId("6186497e7d060a0ac38475ea"),
            "actorName": "贾士凯",
            "sex": 0,
            "doubanId": "1368561"
        },
        {
            "_id": ObjectId("628dcab099681c6979a9acaa"),
            "actorName": "吴倩",
            "sex": 1,
            "doubanId": "1450657"
        },
        {
            "_id": ObjectId("628b4c7799681c6979a9243b"),
            "actorName": "闫丹丹",
            "sex": 1,
            "doubanId": "1446513"
        },
        {
            "_id": ObjectId("628dcc2f99681c6979a9adfe"),
            "actorName": "伍星焰",
            "sex": 1,
            "doubanId": "1456234"
        }
    ],
    "cameraDepartment": [
        {
            "_id": ObjectId("628df0f899681c6979a9c907"),
            "actorName": "赵振刚",
            "sex": 0,
            "doubanId": "1412009"
        }
    ],
    "artDepartment": [
        {
            "_id": ObjectId("628df0f899681c6979a9c909"),
            "actorName": "武明",
            "sex": 0,
            "doubanId": "1379290"
        }
    ],
    "otherCrew": [
        {
            "_id": ObjectId("628df0f899681c6979a9c90f"),
            "actorName": "吴永超",
            "sex": 0,
            "doubanId": "1394013"
        }
    ],
    "actionOrStunts": [
        {
            "_id": ObjectId("628df0f899681c6979a9c90d"),
            "actorName": "王鑫峰",
            "sex": 0,
            "doubanId": "1411291"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc13 = {
    "_id": ObjectId("62a7e6497baf4b2ae4869cdd"),
    "title": "说英雄谁是英雄",
    "programId": "6281faeadb465d6198440a6a",
    "doubanId": "35192154",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("6135dd04aab95f5ecdf5cfc4"),
            "actorName": "李木戈",
            "sex": 0,
            "doubanId": "1324156"
        }
    ],
    "writer": [
        {
            "_id": ObjectId("628b479c99681c6979a92007"),
            "actorName": "霜城",
            "sex": 0,
            "doubanId": "1466571"
        },
        {
            "_id": ObjectId("6296d4a4d915283ce8f170cf"),
            "actorName": "温瑞安",
            "sex": 0,
            "doubanId": "1321279"
        },
        {
            "_id": ObjectId("6296d4a4d915283ce8f170d1"),
            "actorName": "虞筱霏",
            "sex": 1,
            "doubanId": "1472456"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135dedeaab95f5ecdf5d92a"),
            "actorName": "曾舜晞",
            "sex": 0,
            "doubanId": "1356395"
        },
        {
            "_id": ObjectId("6133300eaab95f5ecdf5c236"),
            "actorName": "杨超越",
            "doubanId": "1392263"
        },
        {
            "_id": ObjectId("6135e0ddaab95f5ecdf5e5ef"),
            "actorName": "刘宇宁",
            "sex": 0,
            "doubanId": "1401585"
        },
        {
            "_id": ObjectId("61863f367d060a0ac38459a9"),
            "actorName": "陈楚河",
            "sex": 0,
            "doubanId": "1275675"
        },
        {
            "_id": ObjectId("6135dec9aab95f5ecdf5d870"),
            "actorName": "孟子义",
            "doubanId": "1361032"
        },
        {
            "_id": ObjectId("617a4afcff99840c246dfdc0"),
            "actorName": "孙祖君",
            "sex": 0,
            "doubanId": "1356585"
        },
        {
            "_id": ObjectId("61a150a1e10e4d121d655f92"),
            "actorName": "罗嘉良",
            "sex": 0,
            "doubanId": "1038521"
        },
        {
            "_id": ObjectId("6281faeadb465d6198440a68"),
            "actorName": "钱门超",
            "sex": 0,
            "doubanId": "1454671"
        },
        {
            "_id": ObjectId("628cc92199681c6979a98501"),
            "actorName": "张骏杰",
            "sex": 0,
            "doubanId": "1468488"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}

doc14 = {
    "_id": ObjectId("69c64ddf2d2d883d85837b1c"),
    "title": "理想照耀中国",
    "programId": "6135def0aab95f5ecdf5dc0e",
    "doubanId": "35209733",
    "type": 0,
    "director": [
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da34"),
            "actorName": "傅东育",
            "sex": 0,
            "doubanId": "1318143"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da36"),
            "actorName": "郭廷波",
            "sex": 0,
            "doubanId": "1344422"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da38"),
            "actorName": "韩可一",
            "sex": 0,
            "doubanId": "1341437"
        },
        {
            "_id": ObjectId("6135deb7aab95f5ecdf5d7a0"),
            "actorName": "洪泠",
            "sex": 1,
            "doubanId": "1350308"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da3c"),
            "actorName": "焦永亮",
            "doubanId": "1435917"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da3e"),
            "actorName": "金晔",
            "sex": 0,
            "doubanId": "1386413"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da40"),
            "actorName": "毛溦",
            "doubanId": "1454016"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da42"),
            "actorName": "曲江涛",
            "sex": 0,
            "doubanId": "1319081"
        },
        {
            "_id": ObjectId("628de91a99681c6979a9c121"),
            "actorName": "王硕",
            "sex": 0,
            "doubanId": "1406604"
        },
        {
            "_id": ObjectId("6135de26aab95f5ecdf5d42c"),
            "actorName": "王为",
            "sex": 0,
            "doubanId": "1351728"
        },
        {
            "_id": ObjectId("628de91a99681c6979a9c124"),
            "actorName": "王元",
            "doubanId": "1454017"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da4a"),
            "actorName": "姚铂",
            "sex": 0,
            "doubanId": "1453622"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da4c"),
            "actorName": "赵小鸥",
            "sex": 0,
            "doubanId": "1275612"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da4e"),
            "actorName": "赵小溪",
            "sex": 0,
            "doubanId": "1323628"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da50"),
            "actorName": "郑世龙",
            "doubanId": "1401386"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da52"),
            "actorName": "周涤非",
            "sex": 0,
            "doubanId": "1362979"
        }
    ],
    "writer": [
        {
            "_id": ObjectId("628b662799681c6979a93388"),
            "actorName": "梁振华",
            "sex": 0,
            "doubanId": "1336986"
        },
        {
            "_id": ObjectId("628de91c99681c6979a9c20f"),
            "actorName": "陈萱",
            "doubanId": "1405133"
        },
        {
            "_id": ObjectId("628c567199681c6979a94cba"),
            "actorName": "初征",
            "sex": 1,
            "doubanId": "1386717"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da38"),
            "actorName": "韩可一",
            "sex": 0,
            "doubanId": "1341437"
        },
        {
            "_id": ObjectId("628de91c99681c6979a9c213"),
            "actorName": "何庆平",
            "doubanId": "1435068"
        },
        {
            "_id": ObjectId("628b662799681c6979a9338a"),
            "actorName": "胡雅婷",
            "sex": 1,
            "doubanId": "1426467"
        },
        {
            "_id": ObjectId("628de51099681c6979a9bec8"),
            "actorName": "姜大乔",
            "sex": 0,
            "doubanId": "1401107"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c217"),
            "actorName": "李花",
            "sex": 0,
            "doubanId": "1439280"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c219"),
            "actorName": "李正虎",
            "sex": 0,
            "doubanId": "1335139"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c21b"),
            "actorName": "刘沈",
            "doubanId": "1345969"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c21d"),
            "actorName": "刘丹",
            "doubanId": "1375273"
        },
        {
            "_id": ObjectId("628dcad599681c6979a9acc2"),
            "actorName": "秦文",
            "sex": 1,
            "doubanId": "1439303"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da42"),
            "actorName": "曲江涛",
            "sex": 0,
            "doubanId": "1319081"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c221"),
            "actorName": "苏蓬",
            "sex": 0,
            "doubanId": "1386775"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c223"),
            "actorName": "王海峰",
            "doubanId": "1337719"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c225"),
            "actorName": "王琬晴",
            "doubanId": "1454019"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c227"),
            "actorName": "潇雅",
            "sex": 1,
            "doubanId": "1337718"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c229"),
            "actorName": "余思",
            "sex": 1,
            "doubanId": "1377919"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c22b"),
            "actorName": "张显",
            "sex": 0,
            "doubanId": "1380465"
        },
        {
            "_id": ObjectId("628b662799681c6979a9338c"),
            "actorName": "张贝思",
            "doubanId": "1454018"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da52"),
            "actorName": "周涤非",
            "sex": 0,
            "doubanId": "1362979"
        }
    ],
    "cast": [
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da54"),
            "actorName": "王凯",
            "sex": 0,
            "doubanId": "1314544"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd36"),
            "actorName": "王劲松",
            "sex": 0,
            "doubanId": "1313468"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da58"),
            "actorName": "靳东",
            "sex": 0,
            "doubanId": "1314123"
        },
        {
            "_id": ObjectId("6135de29aab95f5ecdf5d45a"),
            "actorName": "刘奕君",
            "sex": 0,
            "doubanId": "1322731"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da5c"),
            "actorName": "赵丽颖",
            "sex": 1,
            "doubanId": "1275620"
        },
        {
            "_id": ObjectId("6133301caab95f5ecdf5c2c4"),
            "actorName": "王一博",
            "sex": 0,
            "doubanId": "1354130"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da60"),
            "actorName": "王俊凯",
            "sex": 0,
            "doubanId": "1339594"
        },
        {
            "_id": ObjectId("6133303faab95f5ecdf5c44c"),
            "actorName": "侯勇",
            "sex": 0,
            "doubanId": "1274228"
        },
        {
            "_id": ObjectId("6135d966aab95f5ecdf5cb1e"),
            "actorName": "杨童舒",
            "sex": 1,
            "doubanId": "1315220"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cb90"),
            "actorName": "李一桐",
            "sex": 1,
            "doubanId": "1354284"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da68"),
            "actorName": "陈晓",
            "sex": 0,
            "doubanId": "1325412"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da6a"),
            "actorName": "邓伦",
            "sex": 0,
            "doubanId": "1333341"
        },
        {
            "_id": ObjectId("6133302faab95f5ecdf5c3bc"),
            "actorName": "侯明昊",
            "sex": 0,
            "doubanId": "1359141"
        },
        {
            "_id": ObjectId("6135ddc6aab95f5ecdf5d25c"),
            "actorName": "张雪迎",
            "sex": 1,
            "doubanId": "1326897"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd70"),
            "actorName": "林永健",
            "sex": 0,
            "doubanId": "1274650"
        },
        {
            "_id": ObjectId("6135dee1aab95f5ecdf5d958"),
            "actorName": "严屹宽",
            "sex": 0,
            "doubanId": "1313653"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da74"),
            "actorName": "彭小苒",
            "sex": 1,
            "doubanId": "1344792"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da76"),
            "actorName": "陈恒",
            "sex": 1,
            "doubanId": "1364999"
        },
        {
            "_id": ObjectId("6135de89aab95f5ecdf5d5ec"),
            "actorName": "成毅",
            "sex": 0,
            "doubanId": "1323398"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da7a"),
            "actorName": "陆毅",
            "doubanId": "1014781"
        },
        {
            "_id": ObjectId("6135dda3aab95f5ecdf5d196"),
            "actorName": "袁冰妍",
            "sex": 1,
            "doubanId": "1342901"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da7e"),
            "actorName": "张婧仪",
            "doubanId": "1407562"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da80"),
            "actorName": "董璇",
            "sex": 1,
            "doubanId": "1276104"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da82"),
            "actorName": "张嘉倪",
            "sex": 1,
            "doubanId": "1314636"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da84"),
            "actorName": "王圣迪",
            "sex": 1,
            "doubanId": "1407876"
        },
        {
            "_id": ObjectId("6135de4faab95f5ecdf5d4c2"),
            "actorName": "杨了",
            "sex": 1,
            "doubanId": "1351248"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da88"),
            "actorName": "李锐",
            "sex": 0,
            "doubanId": "1317204"
        },
        {
            "_id": ObjectId("6135de44aab95f5ecdf5d4aa"),
            "actorName": "黄品沅",
            "sex": 0,
            "doubanId": "1326050"
        },
        {
            "_id": ObjectId("628de02e99681c6979a9ba89"),
            "actorName": "张晶晶",
            "sex": 1,
            "doubanId": "1355296"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da8e"),
            "actorName": "索朗旺姆",
            "doubanId": "1400147"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da90"),
            "actorName": "普布次仁",
            "doubanId": "1425075"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da92"),
            "actorName": "宁心",
            "sex": 1,
            "doubanId": "1386777"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da94"),
            "actorName": "章煜奇",
            "sex": 0,
            "doubanId": "1408074"
        },
        {
            "_id": ObjectId("61332ffbaab95f5ecdf5c1c0"),
            "actorName": "李梦男",
            "sex": 0,
            "doubanId": "1321589"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da98"),
            "actorName": "刘天佐",
            "sex": 0,
            "doubanId": "1318324"
        },
        {
            "_id": ObjectId("6135d968aab95f5ecdf5cb38"),
            "actorName": "刘宥畅",
            "sex": 0,
            "doubanId": "1425863"
        },
        {
            "_id": ObjectId("6133303baab95f5ecdf5c3fc"),
            "actorName": "牛骏峰",
            "doubanId": "1322716"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5da9e"),
            "actorName": "赵珞然",
            "doubanId": "1395279"
        },
        {
            "_id": ObjectId("6135dcdbaab95f5ecdf5cee8"),
            "actorName": "谭松韵",
            "doubanId": "1318061"
        },
        {
            "_id": ObjectId("628c9b6e99681c6979a968d3"),
            "actorName": "平安",
            "sex": 0,
            "doubanId": "1361751"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daa4"),
            "actorName": "于晓光",
            "sex": 0,
            "doubanId": "1321977"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daa6"),
            "actorName": "邵杰睿",
            "doubanId": "1409830"
        },
        {
            "_id": ObjectId("6135dcbeaab95f5ecdf5ce3a"),
            "actorName": "王若麟",
            "sex": 0,
            "doubanId": "1348350"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daaa"),
            "actorName": "张欢",
            "sex": 0,
            "doubanId": "1403358"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daac"),
            "actorName": "黄星羱",
            "sex": 0,
            "doubanId": "1375258"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daae"),
            "actorName": "晋松",
            "sex": 0,
            "doubanId": "1315699"
        },
        {
            "_id": ObjectId("6135dec8aab95f5ecdf5d852"),
            "actorName": "贺刚",
            "sex": 0,
            "doubanId": "1313048"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dab2"),
            "actorName": "李浩轩",
            "sex": 0,
            "doubanId": "1317325"
        },
        {
            "_id": ObjectId("6135dd90aab95f5ecdf5d152"),
            "actorName": "代旭",
            "sex": 0,
            "doubanId": "1321741"
        },
        {
            "_id": ObjectId("6135ddaeaab95f5ecdf5d22e"),
            "actorName": "王佳宇",
            "sex": 1,
            "doubanId": "1361608"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dab8"),
            "actorName": "田昊",
            "sex": 0,
            "doubanId": "1335215"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daba"),
            "actorName": "周澄奥",
            "sex": 0,
            "doubanId": "1384090"
        },
        {
            "_id": ObjectId("6135dcdbaab95f5ecdf5cf5a"),
            "actorName": "杨猛",
            "sex": 0,
            "doubanId": "1328363"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dabe"),
            "actorName": "石凯",
            "sex": 0,
            "doubanId": "1415590"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dac0"),
            "actorName": "陈昱彤",
            "sex": 1,
            "doubanId": "1444805"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dac2"),
            "actorName": "李兰迪",
            "sex": 1,
            "doubanId": "1330228"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dac4"),
            "actorName": "于月仙",
            "sex": 1,
            "doubanId": "1314006"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dac6"),
            "actorName": "房子斌",
            "sex": 0,
            "doubanId": "1316392"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dac8"),
            "actorName": "叶晞月",
            "sex": 1,
            "doubanId": "1429491"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5d9b2"),
            "actorName": "郭涛",
            "sex": 0,
            "doubanId": "1274274"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dacc"),
            "actorName": "黄健翔",
            "sex": 0,
            "doubanId": "1316405"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dace"),
            "actorName": "赵雷棋",
            "sex": 0,
            "doubanId": "1337573"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dad0"),
            "actorName": "刘頔",
            "sex": 0,
            "doubanId": "1343944"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dad2"),
            "actorName": "徐多多",
            "sex": 1,
            "doubanId": "1429626"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd74"),
            "actorName": "陈都灵",
            "sex": 1,
            "doubanId": "1342249"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dad6"),
            "actorName": "乔振宇",
            "doubanId": "1275683"
        },
        {
            "_id": ObjectId("6135de67aab95f5ecdf5d580"),
            "actorName": "张隽溢",
            "sex": 0,
            "doubanId": "1321110"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dada"),
            "actorName": "荣梓杉",
            "sex": 0,
            "doubanId": "1352321"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dadc"),
            "actorName": "林昕宜",
            "doubanId": "1406835"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dade"),
            "actorName": "吴彦姝",
            "sex": 1,
            "doubanId": "1338004"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dae0"),
            "actorName": "崔可法",
            "sex": 0,
            "doubanId": "1318263"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dae2"),
            "actorName": "张世会",
            "doubanId": "1336229"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dae4"),
            "actorName": "啜妮",
            "sex": 1,
            "doubanId": "1323760"
        },
        {
            "_id": ObjectId("61332ff4aab95f5ecdf5c150"),
            "actorName": "曹磊",
            "sex": 0,
            "doubanId": "1318195"
        },
        {
            "_id": ObjectId("6135db5baab95f5ecdf5cb84"),
            "actorName": "娜仁花",
            "sex": 1,
            "doubanId": "1292855"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daea"),
            "actorName": "左小青",
            "sex": 1,
            "doubanId": "1274978"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daec"),
            "actorName": "刘妍",
            "sex": 1,
            "doubanId": "1439708"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daee"),
            "actorName": "杨颖",
            "sex": 1,
            "doubanId": "1033011"
        },
        {
            "_id": ObjectId("6135de8caab95f5ecdf5d62e"),
            "actorName": "印小天",
            "sex": 0,
            "doubanId": "1274888"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d210"),
            "actorName": "黄杨钿甜",
            "sex": 1,
            "doubanId": "1383019"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daf4"),
            "actorName": "岳跃利",
            "doubanId": "1313611"
        },
        {
            "_id": ObjectId("6135dd86aab95f5ecdf5d110"),
            "actorName": "陈若轩",
            "sex": 0,
            "doubanId": "1348101"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5daf8"),
            "actorName": "孔琳",
            "sex": 1,
            "doubanId": "1015186"
        },
        {
            "_id": ObjectId("628b6d8899681c6979a9387a"),
            "actorName": "李威",
            "sex": 0,
            "doubanId": "1317893"
        },
        {
            "_id": ObjectId("61332fecaab95f5ecdf5c0f2"),
            "actorName": "陈思宇",
            "doubanId": "1364252"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dafe"),
            "actorName": "节冰",
            "sex": 0,
            "doubanId": "1365737"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db00"),
            "actorName": "张欣媚",
            "sex": 1,
            "doubanId": "1374118"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db02"),
            "actorName": "千喆",
            "sex": 0,
            "doubanId": "1399086"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db04"),
            "actorName": "斯力更",
            "sex": 0,
            "doubanId": "1336640"
        },
        {
            "_id": ObjectId("628de91b99681c6979a9c184"),
            "actorName": "李昂",
            "sex": 0,
            "doubanId": "1337228"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db08"),
            "actorName": "战菁一",
            "sex": 1,
            "doubanId": "1318521"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db0a"),
            "actorName": "罗予彤",
            "sex": 1,
            "doubanId": "1409430"
        },
        {
            "_id": ObjectId("61c12f1e9fb9b74f97640caf"),
            "actorName": "林鹏",
            "sex": 0,
            "doubanId": "1349188"
        },
        {
            "_id": ObjectId("6135dc78aab95f5ecdf5cc8a"),
            "actorName": "侯祥玲",
            "doubanId": "1318604"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db10"),
            "actorName": "薛闻君",
            "doubanId": "1362997"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d924"),
            "actorName": "仉上明珠",
            "sex": 1,
            "doubanId": "1428515"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db14"),
            "actorName": "经超",
            "doubanId": "1348538"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db16"),
            "actorName": "盛一伦",
            "sex": 0,
            "doubanId": "1330841"
        },
        {
            "_id": ObjectId("6135dc65aab95f5ecdf5cc28"),
            "actorName": "赵昭仪",
            "sex": 1,
            "doubanId": "1419860"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db1a"),
            "actorName": "舒耀瑄",
            "sex": 0,
            "doubanId": "1314212"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db1c"),
            "actorName": "赵恒煊",
            "sex": 0,
            "doubanId": "1275891"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db1e"),
            "actorName": "吴磊",
            "sex": 0,
            "doubanId": "1276150"
        },
        {
            "_id": ObjectId("6133301caab95f5ecdf5c2c6"),
            "actorName": "张艺兴",
            "doubanId": "1338949"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db22"),
            "actorName": "王鸥",
            "sex": 1,
            "doubanId": "1275508"
        },
        {
            "_id": ObjectId("62545f9bdb465d619843fcc1"),
            "actorName": "李菁",
            "sex": 0,
            "doubanId": "1313907"
        },
        {
            "_id": ObjectId("6135dc65aab95f5ecdf5cc10"),
            "actorName": "尹铸胜",
            "sex": 0,
            "doubanId": "1313561"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db28"),
            "actorName": "陶红",
            "sex": 1,
            "doubanId": "1187908"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db2a"),
            "actorName": "余承恩",
            "sex": 0,
            "doubanId": "1414465"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db2c"),
            "actorName": "何蓝逗",
            "sex": 1,
            "doubanId": "1376538"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db2e"),
            "actorName": "赵轩",
            "sex": 0,
            "doubanId": "1440336"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db30"),
            "actorName": "柯颖",
            "sex": 1,
            "doubanId": "1445060"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db32"),
            "actorName": "郭晓东",
            "sex": 0,
            "doubanId": "1274230"
        },
        {
            "_id": ObjectId("61333025aab95f5ecdf5c35c"),
            "actorName": "刘钧",
            "sex": 0,
            "doubanId": "1314921"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db36"),
            "actorName": "周中和",
            "sex": 0,
            "doubanId": "1343200"
        },
        {
            "_id": ObjectId("6135ddd2aab95f5ecdf5d2ec"),
            "actorName": "汪晴",
            "sex": 1,
            "doubanId": "1435222"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db3a"),
            "actorName": "白泽泽",
            "sex": 0,
            "doubanId": "1441799"
        },
        {
            "_id": ObjectId("6135dda3aab95f5ecdf5d198"),
            "actorName": "佟梦实",
            "sex": 0,
            "doubanId": "1352897"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db3e"),
            "actorName": "王鑫",
            "sex": 0,
            "doubanId": "1335594"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db40"),
            "actorName": "孙浩涪",
            "sex": 0,
            "doubanId": "1327985"
        },
        {
            "_id": ObjectId("61332ff8aab95f5ecdf5c196"),
            "actorName": "许晓诺",
            "doubanId": "1353236"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db44"),
            "actorName": "王鹏翔",
            "sex": 0,
            "doubanId": "1363592"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db46"),
            "actorName": "冯绍峰",
            "sex": 0,
            "doubanId": "1275721"
        },
        {
            "_id": ObjectId("6135ddc9aab95f5ecdf5d274"),
            "actorName": "张慧雯",
            "doubanId": "1339318"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db4a"),
            "actorName": "岳旸",
            "sex": 0,
            "doubanId": "1327329"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db4c"),
            "actorName": "吴恙",
            "sex": 1,
            "doubanId": "1327810"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db4e"),
            "actorName": "王建新",
            "sex": 0,
            "doubanId": "1315700"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db50"),
            "actorName": "郭昊伦",
            "sex": 0,
            "doubanId": "1318247"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db52"),
            "actorName": "赵千紫",
            "sex": 1,
            "doubanId": "1348963"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db54"),
            "actorName": "冯青",
            "sex": 1,
            "doubanId": "1368652"
        },
        {
            "_id": ObjectId("628dda9599681c6979a9b837"),
            "actorName": "邱林",
            "sex": 1,
            "doubanId": "1351452"
        },
        {
            "_id": ObjectId("6135dd8eaab95f5ecdf5d130"),
            "actorName": "肖燃",
            "doubanId": "1418598"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db5a"),
            "actorName": "任程伟",
            "sex": 0,
            "doubanId": "1313893"
        },
        {
            "_id": ObjectId("61332ff4aab95f5ecdf5c14c"),
            "actorName": "刘芸",
            "sex": 1,
            "doubanId": "1276152"
        },
        {
            "_id": ObjectId("6135dc7baab95f5ecdf5cca0"),
            "actorName": "陈子由",
            "doubanId": "1379701"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db60"),
            "actorName": "雨婷儿",
            "sex": 1,
            "doubanId": "1350930"
        },
        {
            "_id": ObjectId("6135dd14aab95f5ecdf5d00c"),
            "actorName": "冉旭",
            "doubanId": "1328841"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db64"),
            "actorName": "厉梦帆",
            "sex": 1,
            "doubanId": "1402949"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db66"),
            "actorName": "汪涵",
            "sex": 0,
            "doubanId": "1312937"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db68"),
            "actorName": "杨采钰",
            "sex": 1,
            "doubanId": "1320350"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db6a"),
            "actorName": "扈耀之",
            "sex": 0,
            "doubanId": "1318140"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db6c"),
            "actorName": "王莎莎",
            "sex": 1,
            "doubanId": "1274647"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db6e"),
            "actorName": "乔鸣麟",
            "sex": 0,
            "doubanId": "1362844"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db70"),
            "actorName": "方向",
            "sex": 0,
            "doubanId": "1437755"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db72"),
            "actorName": "周钦霖",
            "doubanId": "1328868"
        },
        {
            "_id": ObjectId("6135ded2aab95f5ecdf5d8a6"),
            "actorName": "陈伟栋",
            "sex": 0,
            "doubanId": "1351456"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db76"),
            "actorName": "王迅",
            "sex": 0,
            "doubanId": "1317139"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db78"),
            "actorName": "杨皓宇",
            "sex": 0,
            "doubanId": "1318482"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db7a"),
            "actorName": "黄烁文",
            "sex": 0,
            "doubanId": "1394476"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db7c"),
            "actorName": "张屹杨",
            "sex": 0,
            "doubanId": "1447667"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db7e"),
            "actorName": "刘威",
            "sex": 0,
            "doubanId": "1313885"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db80"),
            "actorName": "施京明",
            "sex": 0,
            "doubanId": "1275418"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db82"),
            "actorName": "吴施乐",
            "sex": 1,
            "doubanId": "1416295"
        },
        {
            "_id": ObjectId("628de91c99681c6979a9c1c4"),
            "actorName": "朱峰",
            "sex": 0,
            "doubanId": "1364596"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db86"),
            "actorName": "胡可",
            "sex": 1,
            "doubanId": "1274939"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db88"),
            "actorName": "傅迦",
            "sex": 0,
            "doubanId": "1318706"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db8a"),
            "actorName": "张玟芊",
            "sex": 1,
            "doubanId": "1330227"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db8c"),
            "actorName": "张曦文",
            "sex": 1,
            "doubanId": "1321313"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db8e"),
            "actorName": "冯棉",
            "sex": 1,
            "doubanId": "1386800"
        },
        {
            "_id": ObjectId("6135de01aab95f5ecdf5d3e8"),
            "actorName": "丁子迪",
            "sex": 1,
            "doubanId": "1365828"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db92"),
            "actorName": "杨晓丹",
            "sex": 1,
            "doubanId": "1357298"
        },
        {
            "_id": ObjectId("6135de44aab95f5ecdf5d4ae"),
            "actorName": "余骁睿",
            "sex": 0,
            "doubanId": "1442284"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db96"),
            "actorName": "孙坚",
            "sex": 0,
            "doubanId": "1313285"
        },
        {
            "_id": ObjectId("6135dee1aab95f5ecdf5d94e"),
            "actorName": "林江国",
            "sex": 0,
            "doubanId": "1316735"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db9a"),
            "actorName": "孙锡堃",
            "sex": 0,
            "doubanId": "1328092"
        },
        {
            "_id": ObjectId("61332ff7aab95f5ecdf5c190"),
            "actorName": "赵子麒",
            "sex": 0,
            "doubanId": "1406093"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5db9e"),
            "actorName": "葛铮",
            "sex": 0,
            "doubanId": "1359090"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dba0"),
            "actorName": "王冠淇",
            "sex": 0,
            "doubanId": "1387972"
        },
        {
            "_id": ObjectId("61333022aab95f5ecdf5c2f6"),
            "actorName": "张云龙",
            "sex": 0,
            "doubanId": "1326059"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dba4"),
            "actorName": "刘帅良",
            "sex": 0,
            "doubanId": "1337891"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dba6"),
            "actorName": "周波",
            "sex": 0,
            "doubanId": "1319320"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dba8"),
            "actorName": "董向荣",
            "sex": 0,
            "doubanId": "1355497"
        },
        {
            "_id": ObjectId("628de91c99681c6979a9c1d8"),
            "actorName": "王博",
            "sex": 0,
            "doubanId": "1446489"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbac"),
            "actorName": "于湉",
            "sex": 0,
            "doubanId": "1340458"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbae"),
            "actorName": "卢勉达",
            "sex": 0,
            "doubanId": "1429586"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbb0"),
            "actorName": "祖峰",
            "sex": 0,
            "doubanId": "1313650"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbb2"),
            "actorName": "袁姗姗",
            "doubanId": "1316067"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbb4"),
            "actorName": "公磊",
            "sex": 0,
            "doubanId": "1322905"
        },
        {
            "_id": ObjectId("6135dc65aab95f5ecdf5cc22"),
            "actorName": "郑伟",
            "sex": 0,
            "doubanId": "1325438"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cdb4"),
            "actorName": "张喜前",
            "sex": 0,
            "doubanId": "1322765"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbba"),
            "actorName": "尼玛颂宋",
            "sex": 1,
            "doubanId": "1329143"
        },
        {
            "_id": ObjectId("6135dcdbaab95f5ecdf5cf0c"),
            "actorName": "马少骅",
            "sex": 0,
            "doubanId": "1274966"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbbe"),
            "actorName": "江一燕",
            "sex": 1,
            "doubanId": "1274286"
        },
        {
            "_id": ObjectId("6135dee8aab95f5ecdf5da06"),
            "actorName": "曹骏",
            "sex": 0,
            "doubanId": "1275884"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbc2"),
            "actorName": "维妮",
            "sex": 1,
            "doubanId": "1329519"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbc4"),
            "actorName": "葛晓凤",
            "sex": 1,
            "doubanId": "1325612"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d914"),
            "actorName": "吴倩",
            "sex": 1,
            "doubanId": "1334223"
        },
        {
            "_id": ObjectId("6135dee1aab95f5ecdf5d95c"),
            "actorName": "张宁江",
            "sex": 0,
            "doubanId": "1321998"
        },
        {
            "_id": ObjectId("6135dc78aab95f5ecdf5cc78"),
            "actorName": "牟星",
            "sex": 1,
            "doubanId": "1336748"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbcc"),
            "actorName": "李莎旻子",
            "sex": 1,
            "doubanId": "1350846"
        },
        {
            "_id": ObjectId("6135de1caab95f5ecdf5d40c"),
            "actorName": "苏梦迪",
            "doubanId": "1456570"
        },
        {
            "_id": ObjectId("6135dec8aab95f5ecdf5d840"),
            "actorName": "廖京生",
            "sex": 0,
            "doubanId": "1314453"
        },
        {
            "_id": ObjectId("6135ddacaab95f5ecdf5d1f0"),
            "actorName": "常铖",
            "sex": 0,
            "doubanId": "1314524"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbd4"),
            "actorName": "李沐然",
            "sex": 1,
            "doubanId": "1447663"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbd6"),
            "actorName": "果靖霖",
            "sex": 0,
            "doubanId": "1274914"
        },
        {
            "_id": ObjectId("6135dc69aab95f5ecdf5cc32"),
            "actorName": "万鹏",
            "sex": 1,
            "doubanId": "1403999"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbda"),
            "actorName": "张陆",
            "sex": 0,
            "doubanId": "1318034"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbdc"),
            "actorName": "马苏",
            "sex": 1,
            "doubanId": "1275459"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbde"),
            "actorName": "冯国强",
            "sex": 0,
            "doubanId": "1325166"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbe0"),
            "actorName": "张亚坤",
            "sex": 0,
            "doubanId": "1318430"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbe2"),
            "actorName": "井柏然",
            "sex": 0,
            "doubanId": "1274628"
        },
        {
            "_id": ObjectId("6135ddaeaab95f5ecdf5d224"),
            "actorName": "李乃文",
            "sex": 0,
            "doubanId": "1274530"
        },
        {
            "_id": ObjectId("6135de58aab95f5ecdf5d532"),
            "actorName": "张志坚",
            "sex": 0,
            "doubanId": "1313469"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbe8"),
            "actorName": "徐佳",
            "doubanId": "1313651"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbea"),
            "actorName": "李亭哲",
            "sex": 0,
            "doubanId": "1325611"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbec"),
            "actorName": "陆思恒",
            "doubanId": "1414629"
        },
        {
            "_id": ObjectId("6135ddd2aab95f5ecdf5d2dc"),
            "actorName": "秦俊杰",
            "sex": 0,
            "doubanId": "1316921"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbae"),
            "actorName": "蒋梦婕",
            "sex": 1,
            "doubanId": "1276049"
        },
        {
            "_id": ObjectId("6135deddaab95f5ecdf5d918"),
            "actorName": "李建义",
            "sex": 0,
            "doubanId": "1323026"
        },
        {
            "_id": ObjectId("6135de44aab95f5ecdf5d4ac"),
            "actorName": "由立平",
            "sex": 0,
            "doubanId": "1318573"
        },
        {
            "_id": ObjectId("6135d964aab95f5ecdf5cad8"),
            "actorName": "黄奕",
            "sex": 1,
            "doubanId": "1051051"
        },
        {
            "_id": ObjectId("6135dca6aab95f5ecdf5cd4a"),
            "actorName": "王亚楠",
            "sex": 0,
            "doubanId": "1275110"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbfa"),
            "actorName": "鄂靖文",
            "sex": 1,
            "doubanId": "1362292"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbfc"),
            "actorName": "衣云鹤",
            "sex": 0,
            "doubanId": "1350228"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dbfe"),
            "actorName": "张优",
            "sex": 0,
            "doubanId": "1348506"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dc00"),
            "actorName": "赵奂然",
            "sex": 0,
            "doubanId": "1407515"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dc02"),
            "actorName": "何家辉",
            "sex": 0,
            "doubanId": "1416942"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dc04"),
            "actorName": "梦秦",
            "sex": 1,
            "doubanId": "1363939"
        },
        {
            "_id": ObjectId("628de91c99681c6979a9c207"),
            "actorName": "王川",
            "sex": 0,
            "doubanId": "1451474"
        },
        {
            "_id": ObjectId("6135de4faab95f5ecdf5d4c6"),
            "actorName": "周俞辰",
            "sex": 0,
            "doubanId": "1456194"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dc0a"),
            "actorName": "赵煊",
            "doubanId": "1325184"
        },
        {
            "_id": ObjectId("614f8e42a75eb73ca717c689"),
            "actorName": "李依蒙",
            "sex": 1,
            "doubanId": "1461745"
        },
        {
            "_id": ObjectId("619da4cd2bc7fc52ae3de920"),
            "actorName": "邢韵嘉",
            "sex": 1,
            "doubanId": "1462486"
        },
        {
            "_id": ObjectId("6135deefaab95f5ecdf5dc0c"),
            "actorName": "刘雯熙",
            "sex": 1,
            "doubanId": "1459720"
        }
    ],
    "producer": [
        {
            "_id": ObjectId("6135def1aab95f5ecdf5dc5c"),
            "actorName": "龚宇",
            "doubanId": "1406734"
        }
    ],
    "musicDepartment": [
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef06"),
            "actorName": "那英",
            "sex": 1,
            "doubanId": "1040056"
        },
        {
            "_id": ObjectId("6184f4147d060a0ac3841112"),
            "actorName": "韩磊",
            "sex": 0,
            "doubanId": "1337425"
        },
        {
            "_id": ObjectId("61333018aab95f5ecdf5c2ba"),
            "actorName": "王源",
            "sex": 0,
            "doubanId": "1339808"
        },
        {
            "_id": ObjectId("6136bf05aab95f5ecdf5efe4"),
            "actorName": "周深",
            "doubanId": "1366895"
        },
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef5a"),
            "actorName": "郁可唯",
            "sex": 1,
            "doubanId": "1274942"
        },
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef24"),
            "actorName": "周笔畅",
            "doubanId": "1274425"
        },
        {
            "_id": ObjectId("6184efdd7d060a0ac383faa8"),
            "actorName": "王铮亮",
            "sex": 0,
            "doubanId": "1322493"
        },
        {
            "_id": ObjectId("618643b97d060a0ac3846f49"),
            "actorName": "魏巡",
            "sex": 0,
            "doubanId": "1414393"
        },
        {
            "_id": ObjectId("61333031aab95f5ecdf5c3e2"),
            "actorName": "郎朗",
            "sex": 0,
            "doubanId": "1224366"
        },
        {
            "_id": ObjectId("6136bf05aab95f5ecdf5efe6"),
            "actorName": "黄明昊",
            "doubanId": "1390368"
        },
        {
            "_id": ObjectId("6135df48aab95f5ecdf5ddae"),
            "actorName": "赖美云",
            "sex": 1,
            "doubanId": "1392264"
        },
        {
            "_id": ObjectId("6136bedeaab95f5ecdf5edc4"),
            "actorName": "蔡徐坤",
            "sex": 0,
            "doubanId": "1389078"
        },
        {
            "_id": ObjectId("6133302baab95f5ecdf5c3a0"),
            "actorName": "佟丽娅",
            "sex": 1,
            "doubanId": "1275756"
        },
        {
            "_id": ObjectId("6136bff1aab95f5ecdf5f7a2"),
            "actorName": "符龙飞",
            "sex": 0,
            "doubanId": "1368302"
        },
        {
            "_id": ObjectId("6136bff1aab95f5ecdf5f7a0"),
            "actorName": "段奥娟",
            "doubanId": "1392309"
        },
        {
            "_id": ObjectId("6136bf0baab95f5ecdf5f0f4"),
            "actorName": "汪苏泷",
            "doubanId": "1374972"
        },
        {
            "_id": ObjectId("618643bd7d060a0ac3846f75"),
            "actorName": "许鹤缤",
            "sex": 0,
            "doubanId": "1343966"
        },
        {
            "_id": ObjectId("6184ea2b7d060a0ac383e39d"),
            "actorName": "伍嘉成",
            "sex": 0,
            "doubanId": "1357678"
        },
        {
            "_id": ObjectId("6136bf94aab95f5ecdf5f57c"),
            "actorName": "阿云嘎",
            "sex": 0,
            "doubanId": "1365029"
        },
        {
            "_id": ObjectId("628de91d99681c6979a9c243"),
            "actorName": "宿雨涵",
            "sex": 1,
            "doubanId": "1369662"
        },
        {
            "_id": ObjectId("6135e0e2aab95f5ecdf5e671"),
            "actorName": "蔡程昱",
            "sex": 0,
            "doubanId": "1408048"
        },
        {
            "_id": ObjectId("6184f0f57d060a0ac384028e"),
            "actorName": "黄英",
            "sex": 1,
            "doubanId": "1320891"
        },
        {
            "_id": ObjectId("6184f3ac7d060a0ac3840dc0"),
            "actorName": "赵雷",
            "doubanId": "1368013"
        },
        {
            "_id": ObjectId("6184f0f67d060a0ac38402cc"),
            "actorName": "陈明",
            "sex": 1,
            "doubanId": "1314039"
        },
        {
            "_id": ObjectId("6136bef7aab95f5ecdf5ef0c"),
            "actorName": "李慧珍",
            "sex": 1,
            "doubanId": "1370010"
        },
        {
            "_id": ObjectId("6136bf0baab95f5ecdf5f12e"),
            "actorName": "李宇春",
            "doubanId": "1274227"
        },
        {
            "_id": ObjectId("6184f0f67d060a0ac38402b6"),
            "actorName": "孙楠",
            "sex": 0,
            "doubanId": "1326575"
        },
        {
            "_id": ObjectId("6135dde0aab95f5ecdf5d320"),
            "actorName": "孙浩",
            "sex": 0,
            "doubanId": "1316965"
        },
        {
            "_id": ObjectId("6186497f7d060a0ac384763a"),
            "actorName": "左立",
            "sex": 0,
            "doubanId": "1340461"
        },
        {
            "_id": ObjectId("6135ddd2aab95f5ecdf5d2dc"),
            "actorName": "秦俊杰",
            "sex": 0,
            "doubanId": "1316921"
        },
        {
            "_id": ObjectId("6135db5eaab95f5ecdf5cbae"),
            "actorName": "蒋梦婕",
            "sex": 1,
            "doubanId": "1276049"
        }
    ],
    "otherCrew": [
        {
            "_id": ObjectId("628de91d99681c6979a9c250"),
            "actorName": "李缘",
            "sex": 1,
            "doubanId": "1422208"
        }
    ],
    "_class": "com.mediaplus.mgcserver.commons.service.entity.ActorRelationGraph"
}