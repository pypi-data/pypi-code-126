import cv2
from pyzbar import pyzbar
import json
import time


def discern_qrcode(file: str):
    """
    识别图片，并读取二维码，返回二维码内容
    :param file: 需要识别的图片路径
    :return:
    """
    qrcode = cv2.imread(file)
    try:
        data = pyzbar.decode(qrcode)
        return json.loads(data[0].data.decode('utf-8'))
    except:
        return None


if __name__ == '__main__':
    text = discern_qrcode('E:/temp/11.jpg')
    print(text)
