"""
公共工具，协议分析
"""
from eqlink.components.link_list import LinkList

''' 全局共享：注册中心连接列表 '''
link_list = LinkList()


def protocol_analysis(protocol):
    """
    对协议类型进行分析和处理
    :param protocol: JSON协议数据
    :return: void
    """
    if protocol['type'] == 'provider register':
        ''' Provider注册 '''
        link_list.add_provider(protocol)
        return {'code': '1000', 'message': '服务注册执行完成!'}
    elif protocol['type'] == 'get provider':
        ''' Consumer查询Provider服务列表 '''
        return link_list.provider_list
