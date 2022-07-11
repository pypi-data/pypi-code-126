import time

from steel_seal import SteelSeal


def test_signature():
    token = SteelSeal.generate_token()
    data = "Hello, World"
    seal_ins = SteelSeal(token)

    sig_info = seal_ins.signature(data)

    print(sig_info)
    print("进行第一次签名验证：{status}".format(status="合法" if seal_ins.verify(data, sig_info) else "非法"))

    time.sleep(4)

    print("模拟重放：{status}".format(status="合法" if seal_ins.verify(data, sig_info) else "非法"))
