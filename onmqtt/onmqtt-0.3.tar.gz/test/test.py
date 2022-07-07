# -*- coding: utf-8 -*-
import onmqtt
import time

# 自行替换
product_id=  '533618'# 产品ID
device_id = '966637746' # 设备ID
auth_info = '1' # 鉴权信息

client = onmqtt.onenet_mqtt(product_id,device_id, auth_info)

def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    temp = 67
    print ("CPU的温度值为: %.3f" %temp)
    return temp

while 1:
    temperature = 666
    print('test')
    client.qpublish("temp_cpu", temperature)
    print('test')
    time.sleep(5)