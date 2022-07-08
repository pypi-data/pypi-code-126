import logging
import serial
import time
import socket

import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.modbus_rtu as modbus_rtu

from .base import IOTBaseCommon, IOTDriver

'''
    pip install modbus-tk==1.1.2
'''


class IOTModbus(IOTDriver):

    # modbus data type
    class ModbusType:
        E_MODBUS_SIGNED = 0
        E_MODBUS_UNSIGNED = 1
        E_MODBUS_BITE = 2
        E_MODBUS_LONG = 3
        E_MODBUS_LONG_INVERSE = 4
        E_MODBUS_FLOAT = 5
        E_MODBUS_FLOAT_INVERSE = 6
        E_MODBUS_DOUBLE = 7
        E_MODBUS_DOUBLE_INVERSE = 8
        E_MODBUS_STRING = 9
        E_MODBUS_STRING_INVERSE = 10
        E_MODBUS_POWERLINK = 11  # 11 powerLink
        E_MODBUS_HEX = 12

    # modbus read/write unit
    class ModbusReadUnit:

        def __init__(self, address: str, slave_id: int, fun_code: int, start: int, end: int, multi_read: int):
            self.address = address
            self.slave_id = slave_id
            self.start = start
            self.end = end
            self.fun_code = fun_code
            self.multi_read = multi_read

            self.full_flag = False
            self.modbus_point_list = []

        def __str__(self):
            return f"{self.address}_{self.slave_id}_{self.fun_code}"

        def set_full_flag(self):
            self.full_flag = True

        @property
        def get_full_flag(self):
            return self.full_flag

        @property
        def get_modbus_id(self):
            return self.slave_id

        @property
        def get_modbus_address(self):
            return self.address

        @property
        def get_modbus_start(self):
            return self.start

        @property
        def get_modbus_end(self):
            return self.end

        @property
        def get_modbus_fun(self):
            return self.fun_code

        @property
        def get_modbus_multi_read(self):
            return self.multi_read

        def set_modbus_end(self, end):
            self.end = end

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.clients = {}

    def __str__(self):
        return f"IOTModbus({self.kwargs})"

    def _gen_key(self,slave_id: int, fun_code: int, address: int) -> str:
        return f"{slave_id}_{fun_code}_{address}"

    def _combine_read_unit(self, modbus_unit, modbus_read_units: dict):
        read_units = modbus_read_units.get(modbus_unit.__str__())
        if read_units is not None:
            if modbus_unit.get_modbus_start == (read_units[-1].get_modbus_end + 1):
                if read_units[-1].get_modbus_end - read_units[-1].get_modbus_start + 1 >= self.configs.get('multi_read'):  # 超过连读上限
                    read_units[-1].set_full_flag()
                else:
                    read_units[-1].set_modbus_end(modbus_unit.get_modbus_end)
            elif modbus_unit.get_modbus_start == read_units[-1].get_modbus_end:
                read_units[-1].set_modbus_end(modbus_unit.get_modbus_end)
            else:
                modbus_read_units[modbus_unit.__str__()].append(modbus_unit)
        else:
            modbus_read_units[modbus_unit.__str__()] = [modbus_unit]

    def _cread_read_units(self, address, slave_items: dict) -> dict:
        modbus_read_units = {}
        for slave_id, fun_codes in slave_items.items():
            for fun_code, p_address in fun_codes.items():
                p_address.sort()
                for addr in p_address:
                    self._combine_read_unit(self.ModbusReadUnit(address, slave_id, fun_code, addr, addr, self.configs.get('multi_read')), modbus_read_units)
        return modbus_read_units

    def _get_address_info(self, device_address: str) -> dict:
        modbus_info = {}
        if len(device_address) > 0:
            if device_address.find('/dev/tty') == 0:  # linux
                info_list = device_address.split('|')
                if len(info_list) == 1:  # port
                    modbus_info = {'type': 'rtu', 'port': str(info_list[0]), 'baudrate': 9600, 'parity': 'N','bytesize': 8, 'stopbits': 1, 'xonxoff': 0}
                elif len(info_list) == 2:  # port/baudrate
                    modbus_info = {'type': 'rtu', 'port': str(info_list[0]), 'baudrate': int(str(info_list[1])),'parity': 'N', 'bytesize': 8, 'stopbits': 1, 'xonxoff': 0}
                elif len(info_list) == 3:  # port/baudrate/parity
                    modbus_info = {'type': 'rtu', 'port': str(info_list[0]), 'baudrate': int(str(info_list[1])),'parity': str(info_list[2]), 'bytesize': 8, 'stopbits': 1, 'xonxoff': 0}
            else:
                info_list = device_address.split('/')
                if len(info_list) == 1:  # IP or port
                    if IOTBaseCommon.check_ip(info_list[0]) is True:
                        modbus_info = {'type': 'tcp', 'host': str(info_list[0]), 'port': 502}
                    else:
                        modbus_info = {'type': 'rtu', 'port': str(info_list[0])}
                elif len(info_list) == 2:  # IP/port   port/baudrate
                    if IOTBaseCommon.check_ip(info_list[0]) == True:
                        modbus_info = {'type': 'tcp', 'host': str(info_list[0]), 'port': int(str(info_list[1]))}
                    else:
                        modbus_info = {'type': 'rtu', 'port': str(info_list[0]), 'baudrate': int(str(info_list[1])), 'bytesize': 8, 'parity': 'N','stopbits': 1, 'xonxoff': 0}
                elif len(info_list) == 3:  # port/baudrate/parity
                    modbus_info = {'type': 'rtu', 'port': str(info_list[0]), 'baudrate': int(str(info_list[1])),'parity': str(info_list[2]), 'bytesize': 8, 'stopbits': 1, 'xonxoff': 0}
        return modbus_info

    def _get_client(self, address: str):
        client = self.clients.get(address)
        if client is None:
            modbus_info = self._get_address_info(address)
            if 'type' in modbus_info.keys():
                modbus_type = modbus_info['type']
                if modbus_type == 'tcp':
                    client = modbus_tcp.TcpMaster(host=modbus_info['host'], port=modbus_info['port'])
                    client.set_timeout(self.configs.get('time_out', 5))
                    self.clients[address] = client
                else:
                    modbus_com = modbus_info['port']  # com5 或/dev/tty0
                    if modbus_com.find('/dev/tty') == 0:
                        client = modbus_rtu.RtuMaster(serial.Serial(port=modbus_com, baudrate=modbus_info['baudrate'], bytesize=modbus_info['bytesize'], parity=modbus_info['parity'],stopbits=modbus_info['stopbits'], xonxoff=modbus_info['xonxoff']))
                        client.set_timeout(self.configs.get('time_out', 5))
                    else:
                        if modbus_com.starswith('com') is False:
                            modbus_com = f"com{modbus_com}"
                        client = modbus_rtu.RtuMaster(serial.Serial(port=modbus_com, baudrate=modbus_info['baudrate'], bytesize=modbus_info['bytesize'], parity=modbus_info['parity'],stopbits=modbus_info['stopbits'], xonxoff=modbus_info['xonxoff']))

                    client.set_timeout(self.configs.get('time_out', 5))
                    client.set_verbose(True)
                    self.clients[address] = client
        return self.clients.get(address)

    def _release_client(self, address: str):
        try:
            client = self.clients.get(address)
            if client:
                client.close()
                del self.clients[address]
            client = None
        except Exception as e:
            pass

    def _send_read_cmd(self, key: str, results: dict, address: str, slave_id: int, add_start: int, add_end: int, fun_code: int):
        try:
            if self._get_client(address) is not None:
                if fun_code == modbus_tk.defines.READ_HOLDING_REGISTERS or fun_code == modbus_tk.defines.WRITE_MULTIPLE_REGISTERS or fun_code == modbus_tk.defines.READ_WRITE_MULTIPLE_REGISTERS:
                    fun_code = modbus_tk.defines.READ_HOLDING_REGISTERS
                elif fun_code == modbus_tk.defines.WRITE_SINGLE_COIL or fun_code == modbus_tk.defines.WRITE_MULTIPLE_COILS:
                    fun_code = modbus_tk.defines.READ_COILS

                value_list = self._get_client(address).execute(slave_id, fun_code, add_start, add_end - add_start + 1)
                self.logging(content=f"modbus({address}) read ({slave_id}-{fun_code}-[{add_start}-{add_end}]) response {add_end-add_start+1}/{len(value_list)} [{value_list}]")
                if len(value_list) > 0:
                    for index in range(0, len(value_list)):
                        if address not in results.keys():
                            results[address] = {}
                        results[address][self._gen_key(slave_id, fun_code, add_start + index)] = value_list[index]
        except (socket.timeout, ConnectionRefusedError, ConnectionResetError) as e:  # connect
            logging.error(f"modbus({address}) read ({slave_id}-{fun_code}-[{add_start}-{add_end}]) fail({e.__str__()})")
            self._release_client(address)
        except Exception as e:  # other
            logging.error(f"modbus({address}) read ({slave_id}-{fun_code}-[{add_start}-{add_end}]) fail({e.__str__()})")

    def _read_address(self, *args, **kwargs) -> dict:
        (address, slave_items) = args
        results = {}
        read_units = self._cread_read_units(address, slave_items)
        for k, modbus_units in read_units.items():
            for modbus_unit in modbus_units:
                if modbus_unit.get_modbus_id >= 0 and modbus_unit.get_modbus_start >= 0 and modbus_unit.get_modbus_end >= modbus_unit.get_modbus_start and modbus_unit.get_modbus_fun > 0 and modbus_unit.get_modbus_fun < 17:
                    self._send_read_cmd(k, results, modbus_unit.get_modbus_address, modbus_unit.get_modbus_id, modbus_unit.get_modbus_start, modbus_unit.get_modbus_end, modbus_unit.get_modbus_fun)
            time.sleep(self.configs.get('cmd_interval', 0.3))
        return results

    def _read(self, read_items: dict) -> dict:
        if len(read_items) > 0:
            jobs = IOTBaseCommon.SimpleThreadPool(len(read_items))
            for address, slaves in read_items.items():
                jobs.submit_task(self._read_address, address, slaves)
            return jobs.done()
        return {}

    def _get_value(self, results: dict, name: str, address: str, slave_id: int, fun_code: int, start: int, length: int, type: int):
        try:
            values = []
            bit = length
            if type == self.ModbusType.E_MODBUS_BITE:
                length = 1
            for i in range(length):
                value = results.get(address, {}).get(self._gen_key(slave_id, fun_code, start+i))
                if value is not None:
                    values.append(value)
            if len(values) == length:
                if type == self.ModbusType.E_MODBUS_SIGNED:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.INT16)
                elif type == self.ModbusType.E_MODBUS_UNSIGNED:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.UINT16)
                elif type == self.ModbusType.E_MODBUS_BITE:
                    value = IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.UINT16)
                    return value & (1 << bit) and 1 or 0
                elif type == self.ModbusType.E_MODBUS_LONG:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.INT32)
                elif type == self.ModbusType.E_MODBUS_LONG_INVERSE:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.INT32, IOTBaseCommon.DataTransform.DataFormat.BADC)
                elif type == self.ModbusType.E_MODBUS_FLOAT:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.FLOAT)
                elif type == self.ModbusType.E_MODBUS_FLOAT_INVERSE:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.FLOAT, IOTBaseCommon.DataTransform.DataFormat.BADC)
                elif type == self.ModbusType.E_MODBUS_DOUBLE:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.DOUBLE)
                elif type == self.ModbusType.E_MODBUS_DOUBLE_INVERSE:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.DOUBLE, IOTBaseCommon.DataTransform.DataFormat.BADC)
                elif type == self.ModbusType.E_MODBUS_STRING:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.STRING)
                elif type == self.ModbusType.E_MODBUS_STRING_INVERSE:
                    return IOTBaseCommon.DataTransform.convert_values_to_value(values, IOTBaseCommon.DataTransform.TypeFormat.STRING, IOTBaseCommon.DataTransform.DataFormat.BADC)
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
                slave_id = point.get('point_slave_id')
                fun_code = point.get('point_fun_code')
                address = point.get('point_address')
                data_type = point.get('point_data_type')
                data_length = point.get('point_data_length')
                if device_address is not None and slave_id is not None and fun_code is not None and address is not None and data_type is not None and data_length is not None:
                    target_address = device_address
                    if target_address not in read_items.keys():
                        read_items[target_address] = {}
                    if slave_id not in read_items[target_address].keys():
                        read_items[target_address][slave_id] = {}
                    if fun_code not in read_items[target_address][slave_id].keys():
                        read_items[target_address][slave_id][fun_code] = []
                    size = 1 if data_type == self.ModbusType.E_MODBUS_BITE else data_length
                    for i in range(size):
                        p_address = address+i
                        if p_address not in read_items[target_address][slave_id][fun_code]:
                            read_items[target_address][slave_id][fun_code].append(p_address)

        datas = self._read(read_items)

        for name in names:
            point = self.points.get(name)
            if point:
                device_address = point.get('point_device_address')
                slave_id = point.get('point_slave_id')
                fun_code = point.get('point_fun_code')
                address = point.get('point_address')
                data_type = point.get('point_data_type')
                data_length = point.get('point_data_length')
                if device_address is not None and slave_id is not None and fun_code is not None and address is not None and data_type is not None and data_length is not None:
                    results[name] = self._get_value(datas, name, device_address, slave_id, fun_code, address, data_length, data_type)
        return results

    def _convert_value_to_vector(self, type, value):
        if type == self.ModbusType.E_MODBUS_SIGNED:
            value_list = IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.INT16)
            if value_list:
                return value_list[0]
        elif type == self.ModbusType.E_MODBUS_UNSIGNED:
            value_list = IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.UINT16)
            if value_list:
                return value_list[0]
        elif type == self.ModbusType.E_MODBUS_HEX:
            return None
        elif type == self.ModbusType.E_MODBUS_BITE:
            return None
        elif type == self.ModbusType.E_MODBUS_LONG:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.INT32)
        elif type == self.ModbusType.E_MODBUS_LONG_INVERSE:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.INT32, IOTBaseCommon.DataTransform.DataFormat.BADC)
        elif type == self.ModbusType.E_MODBUS_FLOAT:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.FLOAT)
        elif type == self.ModbusType.E_MODBUS_FLOAT_INVERSE:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.FLOAT, IOTBaseCommon.DataTransform.DataFormat.BADC)
        elif type == self.ModbusType.E_MODBUS_DOUBLE:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.DOUBLE)
        elif type == self.ModbusType.E_MODBUS_DOUBLE_INVERSE:
            return IOTBaseCommon.DataTransform.convert_value_to_values(value, IOTBaseCommon.DataTransform.TypeFormat.DOUBLE, IOTBaseCommon.DataTransform.DataFormat.BADC)
        return None

    def _write(self, address: str, slave_id: int, fun_code: int, start: int, type: int, length: int, value):
        result = [False, '']
        try:
            fun_code = modbus_tk.defines.WRITE_SINGLE_REGISTER
            if type == self.ModbusType.E_MODBUS_BITE:
                fun_code = modbus_tk.defines.WRITE_SINGLE_COIL
            else:
                if length <= 1:
                    fun_code = modbus_tk.defines.WRITE_SINGLE_REGISTER
                else:
                    fun_code = modbus_tk.defines.WRITE_MULTIPLE_REGISTERS
            output_value = self._convert_value_to_vector(type, value)
            if output_value is not None and self._get_client(address) is not None:
                value_list = self._get_client(address).execute(slave_id, fun_code, start, output_value=output_value)
                if len(value_list) == 2 and value_list[0] == start:
                    return [True, '']
            raise Exception('set fail')
        except (socket.timeout, ConnectionRefusedError, ConnectionResetError) as e:  # connect
            logging.error(f"modbus({address}) write ({slave_id}-{fun_code}-{start}) fail({e.__str__()})")
            result[1] = e.__str__()
            self._release_client(address)
        except Exception as e:  # other
            logging.error(f"modbus({address}) write ({slave_id}-{fun_code}-{start}) fail({e.__str__()})")
            result[1] = e.__str__()
        return result

    def write(self, **kwargs):
        results = {}
        values = kwargs.get('values', {})
        for name, value in values.items():
            point = self.points.get(name)
            if point:
                device_address = point.get('point_device_address')
                slave_id = point.get('point_slave_id')
                fun_code = point.get('point_fun_code')
                address = point.get('point_address')
                data_type = point.get('point_data_type')
                data_length = point.get('point_data_length')
                if device_address is not None and slave_id is not None and fun_code is not None and address is not None and data_type is not None and data_length is not None:
                    results[name] = self._write(device_address, slave_id, fun_code, address, data_type, data_length, value)
            else:
                results[name] = [False, 'UnExist']
        return results

    def ping(self, **kwargs) -> bool:
        return True

    def simulate(self, **kwargs):
        pass