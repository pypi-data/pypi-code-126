import json
import socket
from sys import exit as sys_exit


class LinkRegister:
    def __init__(self, server_conf):
        """
        对象初始化
        :param server_conf: 注册中心配置
        """
        self.server_conf = server_conf

    def register_int(self, send_data):
        """
        服务提供者注册
        :return: None
        """
        register = None
        try:
            register = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("[Socket创建] [ERROR]: " + str(e))
            sys_exit()
        try:
            register.connect((self.server_conf['IP'], self.server_conf['PORT']))
            # register.setblocking(False) # 设置非阻塞模式
            print('[连接注册中心] [SUCCESS] IP:' + self.server_conf['IP'])
        except socket.gaierror as e:
            print("[连接注册中心] [ERROR]: " + str(e))
            sys_exit()
        '''发送信息到注册中心'''
        try:
            register.sendall(bytes(json.dumps(send_data), encoding="utf8"))
            print("[Provider注册] [注册信息发送]:", json.dumps(send_data))
            data = register.recv(self.server_conf['BUF_SIZE'])
            print('[Provider注册] [注册中心响应]:', str(data, 'UTF-8'))
        except socket.error as e:
            print("[Provider注册] [Error]: " + str(e))
            sys_exit()
        """
        关闭注册连接
        """
        register.close()
