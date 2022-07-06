from google.protobuf.json_format import MessageToDict
from sabana import requests as sabana_req


class ProgramError(Exception):
    pass


class Program:
    """
    Program: Holds a series of operations to be executed on a Sabana Instance.
    """

    def __init__(self):
        self.req = sabana_req.execute_request()

    def __del__(self):
        del self.req

    def clear(self):
        self.__del__()
        self.req = sabana_req.execute_request()

    def to_dict(self):
        return MessageToDict(self.req)

    def buffer_alloc(self, name=None, size=None, mmio_name=None, mmio_offset=None):
        self.req.requests.append(
            sabana_req.buffer_alloc(name, size, mmio_name, mmio_offset)
        )

    def buffer_write(self, data, name=None, offset=None):
        self.req.requests.append(sabana_req.buffer_write(name, offset, data))

    def buffer_wait(self, data, name=None, offset=None, timeout=None):
        self.req.requests.append(sabana_req.buffer_wait(name, offset, data, timeout))

    def buffer_read(self, name=None, offset=None, dtype=None, shape=None):
        self.req.requests.append(sabana_req.buffer_read(name, offset, dtype, shape))

    def buffer_dealloc(self, name=None):
        self.req.requests.append(sabana_req.buffer_dealloc(name))

    def mmio_alloc(self, name=None, size=None, base_address=None):
        if size % 4:
            raise ProgramError("Size of MMIO buffer must be a multiple of 4")
        if size >= 0x10000:
            raise ProgramError(f"Size needs less than {0x10000} bytes")
        if size < 0:
            raise ProgramError("Size needs to be a positive number")
        if base_address != 0xA0000000:
            raise ProgramError("Base address must be 0xa0000000")
        self.req.requests.append(sabana_req.mmio_alloc(name, size))

    def mmio_write(self, data, name=None, offset=None):
        if offset % 4:
            raise ProgramError("Offset must be multiple of 4 for MMIO writes")
        self.req.requests.append(sabana_req.mmio_write(name, offset, data))

    def mmio_wait(self, data, name=None, offset=None, timeout=None):
        if offset % 4:
            raise ProgramError("Offset must be multiple of 4 for MMIO writes")
        self.req.requests.append(sabana_req.mmio_wait(name, offset, data, timeout))

    def mmio_read(self, name=None, offset=None, dtype=None, shape=None):
        if offset % 4:
            raise ProgramError("Offset must be multiple of 4 for MMIO writes")
        self.req.requests.append(sabana_req.mmio_read(name, offset, dtype, shape))

    def mmio_dealloc(self, name=None):
        self.req.requests.append(sabana_req.mmio_dealloc(name))
