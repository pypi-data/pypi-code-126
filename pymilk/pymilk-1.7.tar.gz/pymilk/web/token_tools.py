from time import time as nowTimestamp
from math import ceil
from json import loads as json_loads
from json import dumps as json_dumps
from random import random as randomR
from ..localtool import get_md5


class token_tools:
    checkState = {
        0: '',
        1: 'token错误',
        2: '客户端时间过慢',
        3: '客户端时间过快',
        4: '重复的请求',
    }

    def __init__(self, token, maxTimeDis=0, batchDis=0):
        self.token = token
        self.maxTimeDis = maxTimeDis  # 客户端与服务端的时间差不能超过这个值, 否则拒绝访问
        self.batchDis = batchDis  # 相同的请求包间隔秒数须大于这个值, 否则拒绝访问. 用于防止攻击者抓包后反复请求
        if batchDis > 0:
            self.startTime = nowTimestamp()
            self.batchHistory = {}

    def _getBathHisNum(self, t):
        return ceil((t - self.startTime) / self.batchDis)

    def resAddToken(self, content):
        contentJson = json_dumps({
            'content': content,
            'resBatch': str(randomR()) + str(randomR()),
            'timestamp': nowTimestamp()
        })
        return json_dumps({
            'contentJson': contentJson,
            'hash': get_md5(contentJson + self.token)
        })  # return gcontentJson
    
    def bodyParseToken(self, body):
        serverTtime = nowTimestamp()
        gbody = json_loads(body)
        sbodyJson = gbody['sbodyJson']
        hash = gbody['hash']
        sbody = json_loads(sbodyJson)
        body = sbody['body']
        reqBatch = sbody['reqBatch']
        timestamp = sbody['timestamp']
        server_hash = get_md5(sbodyJson + self.token)
        if hash != server_hash: return 1, self.checkState[1], body
        if self.maxTimeDis > 0:
            if timestamp < serverTtime - self.maxTimeDis: return 2, self.checkState[2], body
            if timestamp > serverTtime + self.maxTimeDis: return 3, self.checkState[3], body
        if self.batchDis > 0:
            hisNum = self._getBathHisNum(serverTtime)
            for k in list(self.batchHistory):
                if k < hisNum - 1:
                    self.batchHistory.pop(k, None)
            part = self.batchHistory.setdefault(hisNum, {})
            if reqBatch in part:
                return 4, self.checkState[4], body
            else:
                part[reqBatch] = serverTtime
            partL = self.batchHistory.get(hisNum-1)
            if partL:
                t = partL.get(reqBatch)
                if t and serverTtime <= t + self.batchDis:
                    return 4, self.checkState[4], body
        return 0, self.checkState[0], body


class PyTokenTools:
    ''' 给Python客户端用的 '''

    def __init__(self, token):
        self.token = token
    
    def bodyAddToken(self, body):
        sbodyJson = json_dumps({
            'body': body,
            'reqBatch': str(randomR()) + str(randomR()),
            'timestamp': nowTimestamp()
        })
        return json_dumps({
            'sbodyJson': sbodyJson,
            'hash': get_md5(sbodyJson + self.token)
        })  # return gbodyJson
