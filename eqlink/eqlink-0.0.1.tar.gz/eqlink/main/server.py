"""
服务端配置
"""

import json
import socket
import sys
# from _thread import start_new_thread
from threading import Thread
from eqlink.components.protocol import *


class LinkServer:
    def __init__(self, server_conf):
        self.server_conf = server_conf

    def __data_recv__(self, _connect):
        """
        监听客户端请求
        :param _connect: socket 连接
        :return: void
        """
        while True:
            '''处理客户端端数据'''
            try:
                """
                recv(buffer_size) 接收TCP数据，数据以字符串形式返回，buffer_size 指定要接收的最大数据量
                """
                data = _connect.recv(self.server_conf['BUF_SIZE'])
                data = str(data, 'UTF-8')
                if data == '':
                    break
                data_json = json.loads(data)
                print('接收到客户端数据:', data_json)
                response = protocol_analysis(data_json)
                print('返回给客户端数据:', response)
                _connect.sendall(bytes(json.dumps(response).encode('utf-8')))
            except socket.error as e:
                print(str(e))
                break
        '''关闭客户端连接'''
        _connect.close()

    def server_init(self):
        print('初始化一个服务器线程')
        """
            服务端 socket 初始化
            :return: None
            """

        try:
            """
            创建套接字：socket.socket([family[, type[, proto]]])
            family: 套接字家族可以使 AF_UNIX 或者 AF_INET
            type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM
            protocol: 一般不填默认为 0
            """
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print('[注册中心 socket] [初始化异常] ' + str(e))
            sys.exit()

        try:
            """
            bind() 绑定地址(host,port)到套接字， 在AF_INET下，以元组(host,port)的形式表示地址
            """
            self.server_conf['HOST'] = socket.gethostbyname(socket.gethostname())
            server.bind((self.server_conf['HOST'], self.server_conf['PORT']))
            print('[注册中心启动] ' + self.server_conf['HOST'] + ':' + str(self.server_conf['PORT']))
        except socket.error as e:
            print("Bind failed!" + str(e))
            sys.exit()
        print("Socket bind complete")

        """
        listen(backlog) 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5即可
        """
        server.listen(self.server_conf['BACKLOG'])
        print("Socket now listening")

        while True:
            """
            accept() 被动接受TCP客户端连接,(阻塞式)等待连接的到来
            """
            connect, addr = server.accept()
            print("Connected with %s:%s " % (addr[0], str(addr[1])))
            """
            启动线程管理与客户端连接
            """
            # start_new_thread(self.__data_recv__, (connect,))
            Thread(target=self.__data_recv__, args=(connect,)).start()
