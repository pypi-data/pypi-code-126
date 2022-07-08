
import ctypes
import logging
import snap7
import time

from snap7.snap7types import S7DataItem, S7WLByte
from typing import List

from .base import IOTBaseCommon, IOTDriver, IOTSimulateObject

'''
pip install python-snap7==0.10

Note：
    windows:
        snap7.dll is added to the python installation directory or any directory in the system environment

    linux install dll 
        下载压缩包:
            https://sourceforge.net/projects/snap7/files/下载snap7-full-1.4.2.7z
        
        解压
            apt-get install p7zip-full
            7z x snap7-full-1.4.2.7z
        
        编译
            cd snap7-full-1.4.2/build/unix
	        make -f X86_64_linux.mk all
            
        拷贝
            sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/lib/libsnap7.so
            sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/local/lib/libsnap7.so

        sudo ldconfig

        可选
        sudo apt-get install python-pip3

        安装python snap7库
        sudo pip3 install python-snap7
       
地址
    #define daveP 0x80    		/* direct peripheral access */
    #define daveInputs 0x81     S7AreaPE  
    #define daveOutputs 0x82    S7AreaPA
    #define daveFlags 0x83      S7AreaMK
    #define daveDB 0x84	       S7AreaDB /* data blocks */

DB Address：
    V   daveDB      1
    I/E daveInputs  0
    Q   daveOutputs 0
    M/F daveFlags   0
    T   daveTimer200    0
    C/Z daveCounter200  0
    S   daveSysFlags    0
    A   daveAnaOut/daveAnaIn    0
    P   daveP       0
Point：
    DB2,REAL10,VT_R4,192.168.0.2,1,3
    I0.6

'''


'''
    pip install python-snap7==0.10
'''


class IOTPlcS7(IOTDriver):

    class S7BlockUnit:

        def __init__(self, area, db: int, start: int, end: int):
            self.area = area
            self.db = db
            self.start = start
            self.end = end
            self.length = end - start
            self.buffers = None

        def __str__(self):
            return f"{self.area}_{self.db}"

        @property
        def get_area(self):
            return self.area

        @property
        def get_db(self):
            return self.db

        @property
        def get_start(self):
            return self.start

        @property
        def get_end(self):
            return self.end

        def set_end(self, end):
            self.end = end

        @property
        def get_buffers(self):
            return self.buffers

        def buffer(self):
            self.length = self.end - self.start
            self.buffers = ctypes.create_string_buffer(self.length)

        def update(self, server, start: int, addr: int, type, value):
            index = start - self.start
            if server and index >= 0 and index < self.length:
                if type == IOTBaseCommon.DataTransform.TypeFormat.BOOL:
                    server.lock_area(self.area, self.db)
                    snap7.util.set_bool(self.buffers, index, addr, int(float(value)))
                    server.unlock_area(self.area, self.db)
                elif type == IOTBaseCommon.DataTransform.TypeFormat.INT16:
                    server.lock_area(self.area, self.db)
                    snap7.util.set_int(self.buffers, index, int(float(value)))
                    server.unlock_area(self.area, self.db)
                elif type == IOTBaseCommon.DataTransform.TypeFormat.INT32:
                    server.lock_area(self.area, self.db)
                    snap7.util.set_dword(self.buffers, index, int(float(value)))
                    server.unlock_area(self.area, self.db)
                elif type == IOTBaseCommon.DataTransform.TypeFormat.FLOAT:
                    server.lock_area(self.area, self.db)
                    snap7.util.set_real(self.buffers, index, float(value))
                    server.unlock_area(self.area, self.db)

    class S7ReadUnit:

        def __init__(self, address: str, area, db: int, start: int, length: int, type):
            self.address = address
            self.area = area
            self.db = db
            self.start = start
            self.length = length
            self.type = type

        def __str__(self):
            return f"{self.address}_{self.area}_{self.db}_{self.start}_{self.length}"

        @property
        def get_area(self):
            return self.area

        @property
        def get_db(self):
            return self.db

        @property
        def get_start(self):
            return self.start

        @property
        def get_amount(self):
            return self.length

        def get_item(self):
            item = S7DataItem()
            item.Area = ctypes.c_int32(self.area)
            item.WordLen = ctypes.c_int32(S7WLByte)
            item.Result = ctypes.c_int32(0)
            item.DBNumber = ctypes.c_int32(self.db)
            item.Start = ctypes.c_int32(self.start)
            item.Amount = ctypes.c_int32(self.length)  # reading a REAL, 4 bytes
            buffer = ctypes.create_string_buffer(item.Amount)
            item.pData = ctypes.cast(ctypes.pointer(buffer), ctypes.POINTER(ctypes.c_uint8))
            return item

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.clients = {}
        self.server = None
        self.plc_objects = {}

    def __str__(self):
        return f"IOTPlcS7({self.kwargs})"

    def exit(self):
        super().exit()

        if self.server:
            self.server.stop()
            self.server.destroy()
        self.server = None

        for client in self.clients.keys():
            if client:
                client.disconnect()
                client.destroy()
        self.clients = {}

    def _gen_key(self, area, db: int, start: int, length: int) -> str:
        return f"{area}_{db}_{start}_{length}"

    def _cread_read_units(self, address, s7_items: list) -> dict:
        read_units = {}
        for s7_item in s7_items:
            area, db, start, length, addr, type = self._get_s7_item(s7_item)
            unit = self.S7ReadUnit(address, area, db, start, length, type)
            if unit.__str__() not in read_units[address].keys():
                read_units[unit.__str__()] = unit.get_item()
        return read_units

    def _get_address_info(self, device_address: str) -> dict:
        # ip/port/rack/slot
        info_list = device_address.split('/')
        return {'host': info_list[0] if len(info_list) > 0 else '', 'port': int(float(info_list[1])) if len(info_list) > 1 else 102, 'rack': int(float(info_list[2])) if len(info_list) > 2 else 0, 'slot': int(float(info_list[3])) if len(info_list) > 3 else 1, 'type': '' if len(info_list) > 2 else 'plc200'}

    def _release_client(self, address: str):
        try:
            client = self.clients.get(address)
            if client:
                client.disconnect()
                client.destroy()
                del self.clients[address]
            client = None
        except Exception as e:
            pass

    def _get_client(self, address: str):
        client = self.clients.get(address)
        if client is not None and client.get_connected() is False:
            self._release_client(address)

        if client is None:
            info = self._get_address_info(address)
            if 'type' in info.keys():
                client = snap7.client.Client()
                if client:
                    if self.configs.get('send_timeout', 15) > 0:
                        client.set_param(snap7.snap7types.SendTimeout, self.configs.get('send_timeout'))
                    if self.configs.get('rec_timeout', 3500) > 0:
                        client.set_param(snap7.snap7types.RecvTimeout, self.configs.get('rec_timeout'))

                if info['type'] == 'plc200':
                    client.connect200(info['host'], info['port'])
                else:
                    client.connect(info['host'], info['rack'], info['slot'], info['port'])
                self.clients[address] = client
        return self.clients.get(address)

    def _parse_result(self, address: str, s7_item, results: dict):
        s7_key = self._gen_key(s7_item.Area, s7_item.DBNumber, s7_item.Start, s7_item.Amount)
        value = ctypes.string_at(s7_item.pData, s7_item.Amount)
        if address not in results.keys():
            results[address] = {}
        results[address][s7_key] = value

    def _send_read_cmd(self, address: str, results: dict, s7_item_list: list):
        try:
            if self._get_client(address) is not None and len(s7_item_list) > 0:
                s7_item_byref = (S7DataItem * len(s7_item_list))()
                for index in range(0, len(s7_item_list)):
                    s7_item_byref[index] = s7_item_list[index]
                result, s7_data_items = self._get_client(address).read_multi_vars(s7_item_byref)
                for s7_item in s7_data_items:
                    if s7_item.Result:
                        raise Exception(str(s7_item.Result))
                    else:
                        self._parse_result(address, s7_item, results)
        except Exception as e:
            logging.error(f"plc({address}) read fail({e.__str__()})")

    def _read_address(self, *args, **kwargs) -> dict:
        (address, s7_items) = args
        results = {}
        read_units = self._cread_read_units(address, s7_items)

        units = IOTBaseCommon.chunk_list(list(read_units.values()), self.configs.get('multi_read'))
        for unit in units:
            self._send_read_cmd(address, results, unit)
            time.sleep(self.configs.get('cmd_interval', 0.3))
        return results

    def _read(self, read_items: dict):
        if len(read_items) > 0:
            jobs = IOTBaseCommon.SimpleThreadPool(len(read_items))
            for address, s7_items in read_items.items():
                jobs.submit_task(self._read_address, address, s7_items)
            return jobs.done()
        return {}

    def _get_s7_item(self, address: str):
        # DB2,REAL10,VT_R4 I0.6
        # define daveP 0x80    		/* direct peripheral access */
        # define daveInputs 0x81     S7AreaPE
        # define daveOutputs 0x82    S7AreaPA
        # define daveFlags 0x83      S7AreaMK
        # define daveDB 0x84	       S7AreaDB /* data blocks */

        area = 0x84
        db = 0
        start = 0
        length = 1
        type = IOTBaseCommon.DataTransform.TypeFormat.BOOL
        addr = 0

        if address[0] == 'V':
            area = 0x84
        elif address[0] in ['I', 'E']:
            area = 0x81
        elif address[0] == 'Q':
            area = 0x82
        elif address[0] in ['M', 'F']:
            area = 0x83
        else:
            area = 0x84

        if address[:2] == 'DB':
            infos = address.split(',')
            if len(infos) == 2:
                db = int(infos[0][2:])
                if infos[1].startswith('INT'):
                    type = IOTBaseCommon.DataTransform.TypeFormat.INT16
                    length = 2
                    start = int(float(infos[1][3:]))
                    addr = start
                elif infos[1].startswith('DINT'):
                    type = IOTBaseCommon.DataTransform.TypeFormat.INT32
                    length = 2
                    start = int(float(infos[1][4:]))
                    addr = start
                elif infos[1].startswith('REAL'):
                    type = IOTBaseCommon.DataTransform.TypeFormat.FLOAT
                    length = 2
                    start = int(float(infos[1][4:]))
                    addr = start
                elif infos[1].startswith('BOOL'):
                    type = IOTBaseCommon.DataTransform.TypeFormat.BOOL
                    length = 4
                    pos = address.find('.')
                    if pos >= 4:
                        start = int(float(address[4:pos]))
                        addr = int(float(address[pos+1:]))
        else:
            if area == 'V':
                db = 1
            else:
                db = 0
            if address[2] == 'B':
                if address.find('.') > 0:
                    type = IOTBaseCommon.DataTransform.TypeFormat.BOOL
                else:
                    type = IOTBaseCommon.DataTransform.TypeFormat.BYTE
                length = 1
            elif address[2] == 'W':
                type = IOTBaseCommon.DataTransform.TypeFormat.INT16
                length = 2
            elif address[2] == 'D':
                type = IOTBaseCommon.DataTransform.TypeFormat.INT32
                length = 4

            info = address[1:]
            if address[2] in ['D', 'B', 'W']:
                info = info[1:]
            pos = info.find('.')
            if pos > 0:
                start = int(float(info[:pos]))
                addr = int(float(info[pos+1:]))
            else:
                start = int(float(info))
                addr = start
        return area, db, start, length, addr, type

    def _get_value(self, results: dict, name: str, device_address: str, address: str):
        try:
            area, db, start, length, addr, type = self._get_s7_item(address)
            s7_key = self._gen_key(area, db, start, length)
            _value = results.get(device_address, {}).get(s7_key)
            if _value is not None:
                value = IOTBaseCommon.DataTransform.convert_bytes_to_values(_value, type, 0)
                if type == IOTBaseCommon.DataTransform.TypeFormat.BOOL:
                    return value[addr]
                return value
        except Exception as e:
            logging.error(f"get value({name}) fail({e.__str__()})")
        return None

    def read(self, **kwargs):
        results = {}
        names = kwargs.get('names', list(self.points.keys()))
        read_items = {}
        for name in names:
            point = self.points.get(name)
            if point:
                device_address = point.get('point_device_address')
                address = point.get('point_address')
                if device_address is not None and address is not None:
                    if device_address not in read_items.keys():
                        read_items[device_address] = []
                    if address not in read_items[device_address]:
                        read_items[device_address].append(address)

        datas = self._read(read_items)

        for name in names:
            point = self.points.get(name)
            if point:
                device_address = point.get('point_device_address')
                address = point.get('point_address')
                if device_address is not None and address is not None:
                    value = self._get_value(datas, name, device_address, address)
                    if value is not None:
                        results[name] = value
        return results

    def _conver_set_data_value(self, value, type):
        return bytearray(IOTBaseCommon.DataTransform.convert_values_to_bytes(value, type))

    def _write(self, device_address: str, address: str, value):
        result = [False, '']
        try:
            area, db, start, length, addr, type = self._get_s7_item(address)
            if self._get_client(address) is not None:
                reading = self._conver_set_data_value(value, type)
                result[0] = self._get_client(address).write_area(area, db, start, reading)
            raise Exception('set fail')
        except Exception as e:  # other
            logging.error(f"plc({device_address}) write({address}) fail({e.__str__()})")
            result[1] = e.__str__()
        return result

    def write(self, **kwargs):
        results = {}
        values = kwargs.get('values', {})
        for name, value in values.items():
            point = self.points.get(name)
            if point:
                device_address = point.get('point_device_address')
                address = point.get('point_address')
                if device_address is not None and address is not None:
                    results[name] = self._write(device_address, address, value)
            else:
                results[name] = [False, 'UnExist']
        return results

    def ping(self, **kwargs) -> bool:
        return True

    def _get_server(self):
        if self.server is None:
            server = snap7.server.Server()
            server.start()
            self.server = server
        return self.server

    def simulate(self, **kwargs):
        points = kwargs.get('points', {})
        objects = []
        for name, point in points.items():
            # objects.append(SimulateObject(object_type=point.get('point_type'), instance_number=point.get('point_address'), present_value=point.get('presentValue')))
            objects.append(IOTSimulateObject(**point))

        if len(objects) > 0 and self._get_server():
            self._create_objects(objects)

            self.refresh_objects(objects)

    # 合并生成地址块单元
    def _combine_unit(self, block_unit, block_units: dict):
        units = block_units.get(block_unit.__str__())
        if units is not None:
            if block_unit.get_start == (units[-1].get_end + 1):
                units[-1].set_end(block_unit.get_end)
            elif block_unit.get_start == units[-1].get_modbus_end:
                units[-1].set_modbus_end(block_unit.get_modbus_end)
            else:
                block_units[block_unit.__str__()].append(block_unit)
        else:
            block_units[block_unit.__str__()] = [block_unit]

    def _create_objects(self, objects: List[IOTSimulateObject]):
        if self._get_server() is not None:
            address = []
            for object in objects:
                area, db, start, length, addr, type = self._get_s7_item(object.get('point_address'))
                if [area, db, start, length] not in address:
                    for i in range(length):
                        key = f"{area}_{db}_{start + i}"
                        if key not in self.plc_objects.keys():
                            address.append([area, db, start, length])
            address.sort(key=lambda t: (t[0], t[1], t[2]))

            block_units = {}
            # 生成Block连续地址快
            for address in address:
                self._combine_unit(self.S7BlockUnit(address[0], address[1], address[2], address[2]+address[3]), block_units)

            for k, units in block_units.items():
                for unit in units:
                    for i in range(unit.get_start, unit.get_end):
                        self.plc_objects[f"{k}_{i}"] = unit
                    unit.buffer()
                    self._get_server().register_area(unit.get_area, unit.get_db, unit.get_buffers)

    def refresh_objects(self, objects: List[IOTSimulateObject]):
        for object in objects:
            point_address = object.get('point_address')
            present_value = object.get('present_value')
            if point_address is not None and present_value is not None:
                area, db, start, length, addr, type = self._get_s7_item(point_address)
                plc_object = self.plc_objects.get(f"{area}_{db}_{start}")
                if plc_object:
                    plc_object.update(self._get_server(), start, addr, type, present_value)

    def scan(self, **kwargs):
        pass