"""
用于存储服务消费者和提供者列表
"""


class LinkList:
    def __init__(self):
        self.provider_list = {}
        self.consumer_list = {}

    def add_provider(self, provider):
        """
        将服务提供者加入到本地
        :param provider: 服务提供者信息
        :return: void
        """
        service_name = provider['service_name']
        if service_name in self.provider_list:
            '''服务已注册，不更新provider ip 和 port 列表'''
            if 'remote' in self.provider_list[service_name]:
                if provider['remote'] not in self.provider_list[service_name]['remote']:
                    self.provider_list[service_name]['remote'].append(provider['remote'])
                '''调整服务的方法列表'''
                self.provider_list[service_name]['func'] = list(set(
                    self.provider_list[service_name]['func'] + provider['func']))
        else:
            '''首次进行服务注册'''
            self.provider_list[service_name] = {
                'remote': [provider['remote']],
                'func': provider['func']
            }
