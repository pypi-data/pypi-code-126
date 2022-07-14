import base64
import uuid
import oss2
auth = oss2.Auth('LTAI5tFU8HsxU531eP34p5qA', 'xIAzsYLc5gb7g9TFLCymQ8orWqKB3O')
bucket = oss2.Bucket(auth, 'oss-cn-shenzhen.aliyuncs.com', 'dobot-image')


def upload_oss(img_base64):
    datas = base64.b64decode(img_base64)
    new_pic = f"expire/{str(uuid.uuid4())}.txt"
    # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
    bucket.put_object(new_pic, datas)


def ToBase64(file):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        return base64_data


res = ToBase64('D:/gitttt/dobotedu/test/0.png')
res2 = upload_oss(res)
print(res2)