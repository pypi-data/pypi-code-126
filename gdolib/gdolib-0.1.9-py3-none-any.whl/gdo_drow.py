import os , uuid , requests , instaloader , random , re , json

class gdo_drow:

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


    def get_users_following(username: str, password: str ,name: str) -> str:
        s = instaloader.Instaloader()
        try:
            s.login(username ,password)
            profile = instaloader.Profile.from_username(s.context, name)
            follow_list = []
            for follow in profile.get_followees():
                user = str(follow)
                users = user.split('Profile ')[1].split('(')[0]
                follow_list.append(users)

            return follow_list

        except:
            return {'status' :'error' ,'login' :'error'}



    def get_users_followers(username :str ,password: str, name: str) -> str:
        s = instaloader.Instaloader()
        try:
            s.login(username ,password)
            profile = instaloader.Profile.from_username(s.context, name)
            follow_list = []
            for follow in profile.get_followers():
                user = str(follow)
                users = user.split('Profile ')[1].split('(')[0]
                follow_list.append(users)

            return follow_list

        except:
            return {'status' :'error' ,'login' :'error'}


    def get_ids_following(username: str ,password: str, name: str) -> str:
        L = instaloader.Instaloader()
        try:
            L.login(username ,password)
            profile = instaloader.Profile.from_username(L.context, name)
            follow_list = []
            for follow in profile.get_followees():
                user = str(follow)
                id = user.split('(')[1].split(')')[0]
                follow_list.append(id)

            return follow_list

        except:
            return {'status' :'error' ,'login' :'error'}



    def get_ids_followers(username: str ,password: str, name: str) -> str:
        L = instaloader.Instaloader()
        try:
            L.login(username ,password)
            profile = instaloader.Profile.from_username(L.context, name)
            follow_list = []
            for follow in profile.get_followers():
                user = str(follow)
                id = user.split('(')[1].split(')')[0]
                follow_list.append(id)

            return follow_list

        except:
            return {'status' :'error' ,'login' :'error'}

    def reset(email: str) -> str:
        url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
        headers = {
            "Content-Length": "317",
            "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
            "Host": "i.instagram.com",
            "Connection": "Keep-Alive",
            "User-Agent": str(os.system('ua')),
            "Cookie": f"mid={uuid.uuid4()}",
            "Cookie2": "$Version\u003d1",
            "Accept-Language": "ar-EG, en-US",
            "X-IG-Connection-Type": "MOBILE(LTE)",
            "X-IG-Capabilities": "AQ\u003d\u003d",
            "Accept-Encoding": "gzip"}
        data = {
            "ig_sig_key_version" :"4",
            "user_email" :str(email),
            "device_id" :str(uuid.uuid4()),
            "guid" :str(uuid.uuid4()) ,}
        req = requests.post(url ,headers=headers ,data=data)
        if req.json()["status" ]=="ok":
            return {'status' :'Success' ,'reset' :True}
        else:
            return {'status' :'Success' ,'reset' :False}


    def get_email_busines(username: str, session: str) -> str:
        L = instaloader.Instaloader()
        profile = str(instaloader.Profile.from_username(L.context ,username))
        idd =str(profile.split(')>')[0]).split(' (')[1]
        url = "https://i.instagram.com/api/v1/users/ " +str(id ) +"/info/"
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=2205; shbts=1614954604.1671221; fbm_124024574287414=base_domain=.instagram.com; csrftoken=hE6dtVq6z7Zozo4yfyVPOpTJNEktuPky; rur=FRC; ds_user_id=46430696274; sessionid= " +str(session) +"",
            "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "none",
            "user-agent": str(gdo_drow.Server_IG())}
        res = requests.Session().get(url, data="", headers=headers).json()
        try:
            if res['user']['is_business'] == True and str(res['user']['public_email']) != "":
                email = str(res['user'].get('public_email'))
                if str("@") in email:
                    return {'status' :'Success' ,'email' :str(email)}
                else:
                    return {'status' :'error' ,'email' :None}
            else:
                {'status' :'error' ,'email' :None}

        except:
            return {'status' :'error' ,'email' :'bad request'}



    def get_email():
        s = ["@gmail.com" ,"@yahoo.com" ,"@hotmail.com" ,"@aol.com" ,"@outlook.com"]
        domin = random.choice(s)
        url = 'https://randommer.io/random-email-address'
        headers = {
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length': '239',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
            'origin': 'https://randommer.io',
            'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(os.system('ua')),
            'x-requested-with': 'XMLHttpRequest'}

        data = {
            'number': "1",
            'culture': 'en_US',
            '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
            'X-Requested-With': 'XMLHttpRequest'}
        req = requests.post(url, headers=headers, data=data).text
        data = req.replace('[' ,'').replace(']' ,'').split(',')
        for i in data:
            eail = i.replace('"' ,'')
            ema = eail.split("@")[0]
            email = ema + domin
            return email



    def get_proxy():
        pro = requests.get('https://gimmeproxy.com/api/getProxy')
        if '"protocol"' in pro.text or '"ip"' in pro.text or '"port"' in pro.text:
            if str(pro.json()['protocol']) == 'socks5':
                proxy = str(pro.json()['curl'])
                return {'proxy' :proxy ,'status' :True}
            else:
                return {'message' :'Bad proxy' ,'status' :'error'}
        else:
            return  {'message' :'Bad Protocol' ,'status' :'error'}


    def get_user_agent():
        message = str(os.system('ua'))
        return message


    def csrf_token():
        headers = {"User-Agent": str(gdo_drow.Server_IG())}
        with requests.Session() as azoz:
            url_tok = "https://www.instagram.com/"
            data = azoz.get(url_tok, headers=headers).content
            token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            return {'csrf_token' :str(token)}



    def id_post(url: str) -> str:
        url = str(url)
        igshid = url.split("?")[1].split("%")[0]
        data = {"igshid": igshid ,}
        res = requests.request("GET" ,url ,data=data).text
        id = res.split('content="instagram://media?id=')[1].split('"/>')[0]
        return id


    def get_info_ip(ip: str) -> str:
        url = "https://ipinfo.io/widget/demo/ " +ip
        headers = {
            'Host': 'ipinfo.io',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?1',
            'save-data': 'on',
            'user-agent': str(os.system('ua')),
            'sec-ch-ua-platform': '"Android"',
            'content-type': 'application/json',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ipinfo.io/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'flash=',
            'cookie': 'bento_visitor_id=d0224ad9-b83a-4103-a8e6-aa794b0fc1da',
            'cookie': 'bento_visit_id=b70e5bfe-8341-43e5-a46c-84a3c14cf2e5',
            'cookie': 'bento_events=%5B%7B%22id%22%3A%22a1203021-2f6a-4d31-b42d-06718983bd77%22%2C%22site%22%3A%220d66e7448ad29ad69828d1d4201299a2%22%2C%22visitor%22%3A%22d0224ad9-b83a-4103-a8e6-aa794b0fc1da%22%2C%22visit%22%3A%22b70e5bfe-8341-43e5-a46c-84a3c14cf2e5%22%2C%22type%22%3A%22%24view%22%2C%22date%22%3A%22Wed%2C%2022%20Jun%202022%2015%3A46%3A15%20GMT%22%2C%22browser%22%3A%7B%22user_agent%22%3A%22Mozilla/5.0%20%28Linux%3B%20Android%208.0.0%3B%20SM-G930V%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/96.0.4664.92%20Mobile%20Safari/537.36%22%7D%2C%22page%22%3A%7B%22url%22%3A%22https%3A//ipinfo.io/%22%2C%22queryString%22%3A%22%22%2C%22anchor%22%3A%22%22%2C%22host%22%3A%22ipinfo.io%22%2C%22path%22%3A%22/%22%2C%22protocol%22%3A%22https%3A%22%2C%22title%22%3A%22Comprehensive%20IP%20address%20data%2C%20IP%20geolocation%20API%20and%20database%20-%20IPinfo.io%22%2C%22referrer%22%3A%22%22%7D%2C%22identity%22%3A%7B%7D%7D%5D' ,}
        res = json.loads(requests.get(url ,headers=headers).text)
        try:
            try:ip = res["data"]["ip"]
            except KeyError:ip = False
            try:name = res["data"]["name"]
            except KeyError:name = False
            try:city = res["data"]["city"]
            except KeyError:city= False
            try:country = res["data"]["country"]
            except KeyError:country = False
            try:isp = res["data"]["region"]
            except KeyError:isp = False
            try:region = res["data"]["org"]
            except KeyError:region = False
            try:timezone = res["data"]["timezone"]
            except KeyError: timezone = False
            try:postal = res["data"]["postal"]
            except KeyError:postal = False
            try:asn = res["data"]["asn"]["asn"]
            except KeyError: asn = False
            try:asn_name = res["data"]["asn"]["name"]
            except KeyError:asn_name = False
            try:domain = res["data"]["asn"]["domain"]
            except KeyError:domain = False
            try:route = res["data"]["asn"]["route"]
            except KeyError: route = False
            try:company_name = res["data"]["company"]["name"]
            except KeyError:company_name = False
            try:vpn = res["data"]["privacy"]["vpn"]
            except KeyError:vpn = False
            try:proxy = res["data"]["privacy"]["proxy"]
            except KeyError: proxy = False
            try:service = res["data"]["privacy"]["service"]
            except KeyError: service = False
            try:hosting = res["data"]["privacy"]["hosting"]
            except KeyError: hosting = False
            try:address = res["data"]["abuse"]["address"]
            except KeyError: address = False
            try:email = res["data"]["abuse"]["email"]
            except KeyError: email = False
            try:phone = res["data"]["abuse"]["phone"]
            except KeyError: phone = False

            message ={}
            message["ip"] = ip
            message["name"] = name
            message["city"] = city
            message["country"] = country
            message["isp"] = isp
            message["region"] = region
            message["timezone"] = timezone
            message["postal"] = postal
            message["asn"] = asn
            message["asn_name"] = asn_name
            message["domain"] = domain
            message["route"] = route
            message["company_name"] = company_name
            message["vpn"] = vpn
            message["proxy"] = proxy
            message["service"] = service
            message["hosting"] = hosting
            message["address"] = address
            message["email"] = email
            message["phone"] = phone

            return message
        except:
            return False

# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
# -------------------------[CoDe BY GDØ]------------------------
