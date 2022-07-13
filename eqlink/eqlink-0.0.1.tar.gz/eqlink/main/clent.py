import json
import os
import socket
from sys import exit as sys_exit
from time import sleep as time_sleep


class LinkClient:
    def __init__(self, server_conf, client_conf):
        self.server_conf = server_conf
        self.client_conf = client_conf
        print('连接中心的客户端')

    def client_int(self, data_to_server):
        """
        客户端 socket 初始化
        :return: None
        """

        client = None

        try:
            """
            创建套接字：socket.socket([family[, type[, proto]]])
            family: 套接字家族可以使 AF_UNIX 或者 AF_INET
            type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM
            protocol: 一般不填默认为 0
            """
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("Error creating socket: %s" + str(e))
            sys_exit()

        try:
            """
            服务端的 IP地址 和 端口
            """
            client.connect((self.server_conf['IP'], self.server_conf['PORT']))
            """
            setblocking(flag)
            如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
            """
            # client.setblocking(False)
            print('[连接服务端] [success] IP:' + self.server_conf['IP'])
        except socket.error as e:
            print("connected to server error: %s" + str(e))
            sys_exit()

        while True:
            data_json = json.dumps(data_to_server)
            """
            sendall() 发送心跳数据到服务端
            """
            try:
                client.sendall(bytes(data_json, encoding="utf8"))
                data = client.recv(self.server_conf['BUF_SIZE'])
                print('[Provider注册] [注册中心响应]:', str(data, 'UTF-8'))
            except socket.error:
                print("Send failed!!")
                sys_exit()
            """
            间隔一段时间，进行一次心跳检擦
            """
            print('进程存活，PID:', os.getpid())
            """
            心跳数据设置
            """
            time_sleep(self.client_conf['alive'])
