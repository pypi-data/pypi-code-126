import json
import requests

url = 'https://open.ucpaas.com/ol/sms/sendsms'

sid = 'bb9ac7f6232f4ef961046409ec3bc3b5'
token = '7acc7c8de3d1e7d7e144fa88fd3f0677'
appid = '593404d07d6146aa9b4ba79f929240be'  # 签名：湖南品禾
product_template_id = '609168'  # 您定制的产品{1}已到，请登录会员后台查看。
verification_code_template_id = '604381'  # 您的验证码为{1}，一分钟内输入有效。


def send_product_sms(mobile: str, content: str) -> dict:
    """
    发送短信
    :param mobile: 接收短信的号码
    :param content: 参数内容
    :return:
    """
    response = requests.post(
        url=url,
        data=json.dumps({
            'sid': sid,
            'token': token,
            'appid': appid,
            'templateid': product_template_id,
            'mobile': mobile,
            'param': content
        }),
        headers={
            'Content-Type': 'application/json'
        },
        timeout=5
    )

    resp = json.loads(response.content.decode('utf8'))

    return resp


def send_verification_code_sms(mobile: str, verification_code: str) -> dict:
    """
    发送验证码短信
    :param mobile: 接收短信的号码
    :param verification_code: 验证码内容
    :return:
    """
    response = requests.post(
        url=url,
        data=json.dumps({
            'sid': sid,
            'token': token,
            'appid': appid,
            'templateid': verification_code_template_id,
            'mobile': mobile,
            'param': verification_code
        }),
        headers={
            'Content-Type': 'application/json'
        },
        timeout=5
    )

    resp = json.loads(response.content.decode('utf8'))

    return resp
