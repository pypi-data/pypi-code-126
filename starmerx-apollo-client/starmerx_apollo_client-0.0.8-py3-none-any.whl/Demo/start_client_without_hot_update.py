# @Time    : 2022/6/23 17:50
# @Author  : chengwenxian@starmerx.com
# @Site    : 
# @Software: PyCharm
# @Project : amazon_project
# TODO:  不带热更新启动客户端
# start_hot_update 实例化客户端时, 此参数设置为False, 则可以启动不带热更新得客户端


from apollo_client import ApolloClient

APOLLO_CONFIG_URL = 'your config server url'
APOLLO_APP_ID = 'your application id'
APOLLO_ACCESS_KEY_SECRET = 'the secret for your application'


a_client = ApolloClient(
    app_id=APOLLO_APP_ID, secret=APOLLO_ACCESS_KEY_SECRET, config_url=APOLLO_CONFIG_URL,
    start_hot_update=False  # 此参数设置为False, 则可以启动不带热更新得客户端
)
