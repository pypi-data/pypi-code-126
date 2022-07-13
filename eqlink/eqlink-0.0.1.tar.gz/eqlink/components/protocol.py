"""
公共工具
"""
from eqlink.components.link_list import LinkList

link_list = LinkList()


def protocol_analysis(protocol):
    """
    对协议类型进行分析和处理
    :param protocol: 协议 JSON 内容
    :return: void
    """
    if protocol['type'] == 'provider register':
        print('协议类型', 'provider register')
        link_list.add_provider(protocol)
        print(link_list.provider_list)
        return {'code': '1000'}
    elif protocol['type'] == 'get provider':
        print('协议类型', 'get provider')
        return link_list.provider_list
