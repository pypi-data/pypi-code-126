# @Author : ZhaoqiWu
# @File : Fddns.py

import re
import os
import json
import time
import requests
import optparse
import configparser
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109 import DeleteDomainRecordRequest

# 可以获取到公网IP的网址（按测试速度排序）
WAN_IP_WEB = ['http://ip.qaros.com',
              'http://www.3322.org/dyndns/getip',
              'http://ident.me',
              'http://icanhazip.com',
              'https://api.ipify.org/',
              'https://api.ip.sb/ip']

BIN = os.path.split(os.path.realpath(__file__))[0] + '/'
global_config = configparser.ConfigParser()


class ORIddns(object):
    def __init__(self, user_id, user_secret, region_id, main_domain_name, list_sub_domain):
        """
        实现对阿里云DNS解析
        :param user_id:
        :param user_secret:
        :param region_id:
        :param main_domain_name:
        :param list_sub_domain:
        """
        self.client = AcsClient(user_id, user_secret, region_id)
        self.main_domain_name = main_domain_name
        self.list_sub_domain = list_sub_domain
        self.run_ddns()

    def run_ddns(self):
        """
        对每一个子域名执行ddns
        :return:
        """
        for sub_domain in self.list_sub_domain:
            self.set_domain_record(self.wan_ip, sub_domain, self.main_domain_name)

    @property
    def wan_ip(self):
        """
        通过特定网址，获取当前公网IP
        :return:
        """
        # return "116.22.149.188"
        for wan_ip_web in WAN_IP_WEB:
            respone = requests.get(wan_ip_web)
            if respone.status_code == 200 and respone.text:
                return respone.text.strip()

    def get_domain_info(self, sub_domain):
        """
        查询域名的记录信息
        :param sub_domain:
        :return:
        """
        request = DescribeSubDomainRecordsRequest.DescribeSubDomainRecordsRequest()
        request.set_accept_format('json')

        # 设置要查询的记录类型为A记录
        request.set_Type("A")

        # 指定查记的域名 格式为 'test.binghe.com'
        request.set_SubDomain(sub_domain)

        response = self.client.do_action_with_exception(request)
        response = str(response, encoding='utf-8')

        # 将获取到的记录转换成json对象并返回
        return json.loads(response)

    def add_domain_record(self, value, rr, domainname):
        """
        给指定域名添加新的解析
        (默认都设置为A记录，通过配置set_Type可设置为其他记录)
        :param value:
        :param rr:
        :param domainname:
        :return:
        """
        request = AddDomainRecordRequest.AddDomainRecordRequest()
        request.set_accept_format('json')

        # request.set_Priority('1')  # MX 记录时的必选参数
        request.set_TTL('600')  # 可选值的范围取决于你的阿里云账户等级，免费版为 600 - 86400 单位为秒
        request.set_Value(value)  # 新增的 ip 地址
        request.set_Type('A')  # 记录类型
        request.set_RR(rr)  # 子域名名称
        request.set_DomainName(domainname)  # 主域名

        # 获取记录信息，返回信息中包含 TotalCount 字段，表示获取到的记录条数 0 表示没有记录
        # 其他数字为多少表示有多少条相同记录，正常有记录的值应该为1，如果值大于1则应该检查是不是重复添加了相同的记录
        response = self.client.do_action_with_exception(request)
        response = str(response, encoding='utf-8')
        relsult = json.loads(response)
        return relsult

    def update_domain_record(self, value, rr, record_id):
        """
        对已有的解析记录进行更新
        :param value:
        :param rr:
        :param record_id:
        :return:
        """
        request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        request.set_accept_format('json')

        # request.set_Priority('1')
        request.set_TTL('600')
        request.set_Value(value)  # 新的ip地址
        request.set_Type('A')
        request.set_RR(rr)
        request.set_RecordId(record_id)  # 更新记录需要指定 record_id ，该字段为记录的唯一标识，可以在获取方法的返回信息中得到该字段的值

        response = self.client.do_action_with_exception(request)
        response = str(response, encoding='utf-8')
        return response

    def del_domain_record(self, subdomain):
        """
        删除已有的解析记录
        :param subdomain:
        :return:
        """
        info = self.get_domain_info(subdomain)
        if info["TotalCount"] == 1:
            request = DeleteDomainRecordRequest.DeleteDomainRecordRequest()
            request.set_accept_format('json')

            record_id = info["DomainRecords"]["Record"][0]["RecordId"]
            # 删除记录需要指定 record_id ，该字段为记录的唯一标识，可以在获取方法的返回信息中得到该字段的值
            request.set_RecordId(record_id)
            result = self.client.do_action_with_exception(request)

    def set_domain_record(self, value, rr, domainname):
        """
        # 有记录则更新，没有记录则新增
        :param value:
        :param rr:
        :param domainname:
        :return:
        """
        info = self.get_domain_info(rr + '.' + domainname)
        if info['TotalCount'] == 0:
            add_result = self.add_domain_record(value, rr, domainname)
        elif info["TotalCount"] == 1:
            record_id = info["DomainRecords"]["Record"][0]["RecordId"]
            cur_ip = self.wan_ip
            old_ip = info["DomainRecords"]["Record"][0]["Value"]
            if cur_ip != old_ip:
                update_result = self.update_domain_record(value, rr, record_id)
        else:
            pass


if __name__ == '__main__':
    # 获取调用参数
    parse = optparse.OptionParser(usage='"%prog"', version="%prog V1.0")
    parse.add_option("--key_id", dest="key_id", type=str, required=True, help="user_id")
    parse.add_option("--secret_id", dest="secret_id", required=True, help="")
    parse.add_option("--region", dest="region", required=True, help="")
    parse.add_option("--domain", dest="domain", required=True, help="")
    parse.add_option("--sub_domain", dest="sub_domain", required=True, help="")
    parse.add_option("--loop", dest="loop", action="store_true", help="")
    parse.add_option("--interval", dest="interval", default='300', help="")
    options, args = parse.parse_args()

    # 获取阿里云子用户的accessKeyId和accessSecret
    aliyun_user_id = options.key_id
    aliyun_user_secret = options.secret_id
    # 设置阿里云地区节点
    aliyun_region_id = options.region
    # 设置阿里云主域名
    domain_name = options.domain
    # 设置阿里云子域名列表
    list_sub_domain_name = re.split(r'[;,|]', options.sub_domain)
    # 执行阿里云DDNS域名解析
    ori_ddns = ORIddns(user_id=aliyun_user_id, user_secret=aliyun_user_secret, region_id=aliyun_region_id,
                       main_domain_name=domain_name, list_sub_domain=list_sub_domain_name)
    # 持续检测
    if options.loop:
        # 记录当前公网IP
        raw_wan_ip = ori_ddns.wan_ip
        # 每隔一段时间将进行一次公网IP检测, 如公网IP发生改变，则进行解析
        swtich = True
        while swtich:
            now_wan_ip = ori_ddns.wan_ip
            if raw_wan_ip != now_wan_ip:
                raw_wan_ip = ori_ddns.wan_ip
                ori_ddns = ORIddns(user_id=aliyun_user_id, user_secret=aliyun_user_secret, region_id=aliyun_region_id,
                                   main_domain_name=domain_name, list_sub_domain=list_sub_domain_name)
            else:
                time.sleep(300)
