import re , hashlib , requests , uuid , json
from user_agent import generate_user_agent
from .gdo_drow import *

class info_IG:


    def username(sessionid: str) -> str:
        url = "https://www.instagram.com/accounts/edit/?__a=1"
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid=' + sessionid + '; rur=VLL',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'User-Agent': str(generate_user_agent()),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
            'x-requested-with': 'XMLHttpRequest'}
        data = {'__a': '1'}
        res = requests.get(url, data=data, headers=headers).json()
        try:
            username = res['form_data']['username']
            return str(username)

        except:
            return False

    def followers(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            followers = res['graphql']['user']['edge_followed_by']['count']
            return str(followers)

        except:
            return False

    def following(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            following = res['graphql']['user']['edge_follow']['count']
            return str(following)

        except:
            return False

    def posts(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            posts = res['graphql']['user']['edge_owner_to_timeline_media']['count']
            return posts

        except:
            return False

    def id(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            id = res['graphql']['user']['id']
            return str(id)

        except:
            return False

    def name(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            full_name = res['graphql']['user']['full_name']
            return str(full_name)

        except:
            return False

    def date(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': 'csrftoken=' + str(gdo_drow.csrf_token()['csrf_token']) + '; sessionid=' + str(
                secrets.token_hex(8) * 2) + ';',
            'user-agent': str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        d = str(res['logging_page_id']).split('_')[1]
        get = "https://o7aa.pythonanywhere.com/?id=" + str(d)
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'o7aa.pythonanywhere.com',
            'User-Agent': str(generate_user_agent())}
        res = requests.get(get, headers=head).json()
        try:
            return str(res["data"])

        except:
            return False

    def bio(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            bio = str(res['graphql']['user']['biography'])
            return bio

        except:
            return False

    def private(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            private = str(res['graphql']['user']['is_private'])
            return private

        except:
            return False

    def profile(user: str) -> str:
        url = f'https://www.instagram.com/{user}/?__a=1'
        headers = {
            "content-type": "application/json",
            "User-agent": str(generate_user_agent())}
        res = requests.get(url=url, headers=headers).json()
        try:
            photo = str(res['graphql']['user']['profile_pic_url'])
            return photo

        except:
            return False 
    
    
    
    def Server_IG():
        vers = '136.0.0.34.124'
        virs = '208061712'
        de = {
            'one_plus_7': {'app_version': vers ,'android_version': '29' ,'android_release': '10.0' ,'dpi': '420dpi'
                           ,'resolution': '1080x2340' ,'manufacturer': 'OnePlus' ,'device': 'GM1903'
                           ,'model': 'OnePlus7' ,'cpu': 'qcom' ,'version_code': virs},
            'one_plus_3': {'app_version': vers ,'android_version': '28' ,'android_release': '9.0' ,'dpi': '420dpi'
                           ,'resolution': '1080x1920' ,'manufacturer': 'OnePlus' ,'device': 'ONEPLUS A3003'
                           ,'model': 'OnePlus3' ,'cpu': 'qcom' ,'version_code': virs},
            'samsung_galaxy_s7': {'app_version': vers ,'android_version': '26' ,'android_release': '8.0'
                                  ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                  ,'device': 'SM-G930F' ,'model': 'herolte' ,'cpu': 'samsungexynos8890'
                                  ,'version_code': virs},
            'huawei_mate_9_pro': {'app_version': vers ,'android_version': '24' ,'android_release': '7.0'
                                  ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'HUAWEI'
                                  ,'device': 'LON-L29' ,'model': 'HWLON' ,'cpu': 'hi3660' ,'version_code': virs},
            'samsung_galaxy_s9_plus': {'app_version': vers ,'android_version': '28' ,'android_release': '9.0'
                                       ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                       ,'device': 'SM-G965F' ,'model': 'star2qltecs' ,'cpu': 'samsungexynos9810'
                                       ,'version_code': virs},
            'one_plus_3t': {'app_version': vers ,'android_version': '26' ,'android_release': '8.0' ,'dpi': '380dpi'
                            ,'resolution': '1080x1920' ,'manufacturer': 'OnePlus' ,'device': 'ONEPLUS A3010'
                            ,'model': 'OnePlus3T' ,'cpu': 'qcom' ,'version_code': virs},
            'lg_g5': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1' ,'dpi': '640dpi'
                      ,'resolution': '1440x2392' ,'manufacturer': 'LGE/lge' ,'device': 'RS988' ,'model': 'h1'
                      ,'cpu': 'h1' ,'version_code': virs},
            'zte_axon_7': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1' ,'dpi': '640dpi'
                           ,'resolution': '1440x2560' ,'manufacturer': 'ZTE' ,'device': 'ZTE A2017U'
                           ,'model': 'ailsa_ii' ,'cpu': 'qcom' ,'version_code': virs},
            'samsung_galaxy_s7_edge': {'app_version': vers ,'android_version': '23' ,'android_release': '6.0.1'
                                       ,'dpi': '640dpi' ,'resolution': '1440x2560' ,'manufacturer': 'samsung'
                                       ,'device': 'SM-G935' ,'model': 'hero2lte' ,'cpu': 'samsungexynos8890'
                                       ,'version_code': virs} ,}
        davic = random.choice(list(de.keys()))
        versions = de[davic]['app_version']
        androids = de[davic]['android_version']
        endroids = de[davic]['android_release']
        phonas = de[davic]['dpi']
        phones = de[davic]['resolution']
        manufa = de[davic]['manufacturer']
        devicees = de[davic]['device']
        modelas = de[davic]['model']
        apicup = de[davic]['cpu']
        versiones = de[davic]['version_code']
        massage = 'Instagram {} Android ({}/{}; {}; {}; {}; {}; {}; {}; en_US; {})'.format(str(versions) ,str(androids)
                                                                                           ,str(endroids) ,str(phonas)
                                                                                           ,str(phones) ,str(manufa)
                                                                                           ,str(devicees) ,str(modelas)
                                                                                           ,str(apicup) ,str(versiones))
        return massage


# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------

class session_IG:

    def login_sessionid(session: str) -> str:
        url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        headers = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTBw==',
            'User-Agent': str(info_IG.Server_IG()),
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Accept': '*/*'}
        cookies = {"sessionid": str(session)}
        res = requests.get(url, headers=headers, cookies=cookies).json()
        if str('message') in res:
            return {'status': 'error', 'login': 'error_session'}

        else:
            return {'status': 'Success', 'login': 'true', 'session': str(session)}

    def login_user_pass(username: str, password: str) -> str:

        header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}
        with requests.Session() as m:
            ur = "https://www.instagram.com/"
            data = m.get(ur, headers=header).content
            token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            "Host": "www.instagram.com",
            "X-CSRFToken": token,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "User-Agent": str(info_IG.Server_IG()), }
        data = {
            "username": str(username),
            "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999),
                                                                    str(password)),
            "optIntoOneTap": False,
            "queryParams": {},
            "stopDeletionNonce": "",
            "trustedDeviceRecords": {}}

        with requests.Session() as r:
            url = "https://www.instagram.com/accounts/login/ajax/"
            response = r.post(url, data=data, headers=headers)
            login = json.loads(response.content)

        if ("userId") in str(login):
            userid = login['userId']
            session = str(r.cookies['sessionid'])
            message = {
                'status': 'Success', 'login': 'true',
                'userid': str(userid),
                'sessionid': str(session)}
            return message

        elif ("checkpoint_url") in str(login):
            return {'status': 'error', 'login': 'checkpoint'}

        elif ("Please wait") in str(login):
            return {'status': 'error', 'login': 'blocked'}

        else:
            return {'status': 'error', 'login': 'error.username_or_password'}

    def follow(user: str, session: str) -> str:
        toke = gdo_drow.csrf_token()['csrf_token']
        url = "https://www.instagram.com/web/friendships/" + str(info_IG.id(user)) + "/follow/"
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YfHAnwALAAFCLfUn6sJVurIEyEfr; ig_did=DF84157E-69D8-46D5-B090-33F4741C808C; ig_nrcb=1; csrftoken=hbqh3XgJPV7Rbvr7dgcKiHQnUtX887Pv; ds_user_id=53352662133; sessionid=' + str(
                session) + '; rur="CLN\05453352662133\0541684424578:01f726c10813bcb9113b0f4dcf1be24a5278c0fed11c90001622f46b9b5fdf7010e66eda"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/' + str(user) + '/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '198387',
            'x-csrftoken': str(toke),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3ftyvn6nRl6sa3ptTW-Vz0nWdjaRGWCLkc_dmTa7Pg4Ag3',
            'x-instagram-ajax': '808d16d2325b',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, headers=headers).text
        if str('{"result":"following","status":"ok"}') in res:
            message = {'status': 'Success', 'following': 'true', 'userneme': str(user)}
            return message

        elif str("message") in res:
            return {'status': 'checkpoint', 'following': 'false', 'username': str(user)}
        else:
            return {'status': 'error', 'following': 'false', 'username': str(user)}

    def like(id: str, session: str) -> str:
        url = f'https://www.instagram.com/web/likes/{id}/like/'
        toke = gdo_drow.csrf_token()['csrf_token']
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YfHAnwALAAFCLfUn6sJVurIEyEfr; ig_did=DF84157E-69D8-46D5-B090-33F4741C808C; ig_nrcb=1; shbid="19368\05452914264168\0541682536774:01f7c91f0322a7914c4967e12bcfa34c11317752f470517e402d83ba56c43dd701276cd8"; shbts="1651000774\05452914264168\0541682536774:01f704008a362d517796cf36108b67ea9ace8dbfcadcd2a319c9f940d90aa3647ebd9dbe"; csrftoken=hbqh3XgJPV7Rbvr7dgcKiHQnUtX887Pv; ds_user_id=53352662133;; sessionid=' + str(
                session) + '; rur="CLN\05452914264168\0541682560907:01f70b26a7341573483af51f1be279a94d451a4ebb66ffdf3419bec3f98f6850794bf7f7"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/' + str(id),
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '198387',
            'x-csrftoken': str(toke),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1uQ-iX4kPv3S7OgVlHqdoy-l9MiEpOXeiyxpZdbvWKxKgA',
            'x-instagram-ajax': '20e2a5e214f4',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, headers=headers).text
        if ('status: "ok"') in res:
            return {'status': 'Success', 'like': 'true'}

        elif str("message") in res:
            return {'status': 'checkpoint', 'like': 'false'}

        else:
            return {'status': 'error', 'like': 'false'}

    def comment(id: str, session: str, text: str) -> str:
        url = f"https://www.instagram.com/web/comments/{id}/add/"
        toke = gdo_drow.csrf_token()['csrf_token']
        data = {
            "comment_text": str(text),
            "replied_to_comment_id": "", }
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-length': '37',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={session}; rur=RVA',
            'origin': 'https://www.instagram.com',
            "referer": "https://www.instagram.com/p/Ce8f0HljKad/comments/",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-csrftoken': str(toke),
            'x-ig-app-id': "1217981644879628",
            'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',
            'x-instagram-ajax': '0edc1000e5e7',
            'x-requested-with': 'XMLHttpRequest', }
        res = requests.post(url, data=data, headers=headers).text
        if ('status: "ok"') in res:
            return {'status': 'Success', 'comment': 'true'}

        elif str("message") in res:
            return {'status': 'checkpoint', 'comment': 'false'}

        else:
            return {'status': 'error', 'comment': 'false'}




class login_IG:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        md = hashlib.md5()
        md.update(username.encode('utf-8') + password.encode('utf-8'))
        self.device_id = self.tsn(md.hexdigest())
        self.uuid = self.Tsne(True)
        self.se = requests.Session()

    def tsn(self, sed):
        volatile_ = "12345"
        md = hashlib.md5()
        md.update(sed.encode('utf-8') + volatile_.encode('utf-8'))
        return 'android-' + md.hexdigest()[:16]

    def Tsne(self, type):
        uuid_ = str(uuid.uuid4())
        if (type):
            return uuid_
        else:
            return uuid_.replace('-', '')

    def instagram(self):
        self.url = "https://i.instagram.com/api/v1/accounts/login/"
        token = self.se.get("https://www.instagram.com/", headers={"user-agent": str(generate_user_agent())}).text
        crftoken = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
        self.se.headers.update({
            'Connection': 'close',
            'Accept': '*/*',
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie2': '$Version=1',
            'Accept-Language': 'en-US',
            'User-Agent': str(info_IG.Server_IG())})
        self.data = json.dumps({
            'phone_id': self.Tsne(True),
            '_csrftoken': crftoken,
            'username': self.username,
            'guid': self.uuid,
            'device_id': self.device_id,
            'password': self.password,
            'login_attempt_count': '0'})
        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(self.Tsne(False),urllib.request.quote(self.data))
        resp = self.se.post(self.url, self.payload)
        res = json.loads(resp.text)
        cookie = resp.cookies.get_dict()
        if ("logged_in_user") in str(resp.text):
            cookies = ";".join([v + "=" + cookie[v] for v in cookie])
            sessionid = str(self.se.cookies['sessionid'])
            userid = str(res['logged_in_user']['pk'])

            date = requests.get(f"https://o7aa.pythonanywhere.com/?id={userid}").json()['data']
            massage = {
                'status': 'Success',
                'userid': str(userid),
                'sessionid': str(sessionid),
                'cookies': str(cookies)}
            return massage

        elif ('challenge_required') in str(res):
            return {'status': 'Checkpoint'}

        else:
            return {'status': 'error'}


# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------