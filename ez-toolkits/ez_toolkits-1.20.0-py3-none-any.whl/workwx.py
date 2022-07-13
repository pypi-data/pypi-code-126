import json

import requests


class api(object):

    '''
    企业微信开发者中心
    https://developer.work.weixin.qq.com/
    '''

    _work_id, _agent_id, _agent_secret, _access_token = None, None, None, None

    def __init__(self, work_id, agent_id, agent_secret):
        ''' Initiation '''
        self._work_id = work_id
        self._agent_id = agent_id
        self._agent_secret = agent_secret
        _response = self.get_access_token()
        self._access_token = _response

    def get_access_token(self):
        _response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._work_id}&corpsecret={self._agent_secret}')
        if _response.status_code == 200:
            _result = _response.json()
            return _result.get('access_token')
        return None

    def get_agent_list(self):
        _response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/agent/list?access_token={self._access_token}')
        if _response.status_code == 200:
            return _response.json()
        return {'response': _response.text}

    def get_department_list(self, id):
        _response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self._access_token}&id={id}')
        if _response.status_code == 200:
            return _response.json()
        return {'response': _response.text}

    def get_user_list(self, id):
        _response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={self._access_token}&department_id={id}')
        if _response.status_code == 200:
            return _response.json()
        return {'response': _response.text}

    def send_text(self, users, message):
        '''
        https://developer.work.weixin.qq.com/document/path/90235
        '''

        _json_dict = {
            'touser': users,
            'msgtype': 'text',
            'agentid': self._agent_id,
            'text': {'content': message},
            'safe': 0,
            'enable_id_trans': 0,
            'enable_duplicate_check': 0,
            'duplicate_check_interval': 1800
        }

        _json_string = json.dumps(_json_dict)
        _response = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self._access_token}', data=_json_string)
        if _response.status_code == 200:
            return _response.json()
        return {'response': _response.text}
