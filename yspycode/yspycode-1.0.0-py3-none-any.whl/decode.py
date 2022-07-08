def ysdecode(string):
    x = string.replace('I', '0')
    x = x.replace('i', '1')
    return int(x, 2).to_bytes(len(x) // 8, byteorder='big')