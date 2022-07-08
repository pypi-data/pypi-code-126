import random
import time
from robertcommondriver.system.iot.iot_plc_s7 import IOTPlcS7


def logging_print(**kwargs):
    print(kwargs)


def test_simulate():
    dict_config = {'multi_read': 20, 'cmd_interval': 0.3, 'send_timeout': 15, 'rec_timeout': 3500}
    dict_point = {}
    dict_point['plc1'] = {'point_writable': True, 'point_name': 'plc1', 'device_address': '192.168.1.88/0/1', 'address': 'DB3,REAL4', 'scale': '1'}
    dict_point['plc2'] = {'point_writable': True, 'point_name': 'plc2', 'device_address': '192.168.1.88/0/1', 'address': 'DB3,REAL8', 'scale': '1'}
    dict_point['plc3'] = {'point_writable': True, 'point_name': 'plc3', 'device_address': '192.168.1.88/0/1', 'address': 'DB2,INT2', 'scale': '1'}
    dict_point['plc4'] = {'point_writable': True, 'point_name': 'plc4', 'device_address': '192.168.1.88/0/1', 'address': 'DB1,BOOL0.0', 'scale': '1'}
    dict_point['plc5'] = {'point_writable': True, 'point_name': 'plc5', 'device_address': '192.168.1.88/0/1', 'address': 'I2', 'scale': '1'}
    dict_point['plc6'] = {'point_writable': True, 'point_name': 'plc6', 'device_address': '192.168.1.88/0/1', 'address': 'M2870.0', 'scale': '1'}

    client = IOTPlcS7(configs = dict_config, points= dict_point)
    client.logging(call_logging=logging_print)
    while True:
        try:
            for name, point in dict_point.items():
                point['present_value'] = f"{random.randint(1, 100)}"
            client.simulate(points=dict_point)
        except Exception as e:
            print(e.__str__())
        time.sleep(4)


test_simulate()