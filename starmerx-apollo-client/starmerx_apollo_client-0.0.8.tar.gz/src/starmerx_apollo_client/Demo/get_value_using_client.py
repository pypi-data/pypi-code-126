# @Time    : 2022/6/23 17:52
# @Author  : chengwenxian@starmerx.com
# @Site    : 
# @Software: PyCharm
# @Project : amazon_project
# TODO: 通过客户端获取参数

from apollo_client import ApolloClient

APOLLO_CONFIG_URL = 'your config server url'
APOLLO_APP_ID = 'your application id'
APOLLO_ACCESS_KEY_SECRET = 'the secret for your application'


a_client = ApolloClient(app_id=APOLLO_APP_ID, secret=APOLLO_ACCESS_KEY_SECRET, config_url=APOLLO_CONFIG_URL)

# 获取数据目前只提供了三种格式, 后续有需要可以自行扩展或提交问题, 统一进行添加
# 1. 获取普通文本
a_client.get_value('key_name', default_val='default_value')

# 2. 获取Json格式数据, 如果获取失败, 返回默认值
a_client.get_json('key_name', default_val='default_val')

# 3. 获取是否是DEBUG, 只有对应字段设置为: 'on', True, 1, '1'时, 改函数返回True
a_client.get_debug('key_name', default_val='default_val')

