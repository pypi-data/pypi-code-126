from netaddr import IPAddress, IPNetwork

def add2(number):
    return number+2

def square(number):
    return number**2

def is_rfc1918(address:str):
    if not isinstance(address,str):
        raise TypeError

    IP = IPAddress(address)

    if IP in IPNetwork("10.0.0.0/8"):
        return True
    if IP in IPNetwork("172.16.0/12"):
        return True
    if IP in IPNetwork("192.168.0.0/16"):
        return True

    return False
