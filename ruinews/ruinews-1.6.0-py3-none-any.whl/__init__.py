import requests
import re, os, datetime, json,time
from requests_toolbelt.multipart.encoder import MultipartEncoder
from lxml import etree
from gne import GeneralNewsExtractor,ListPageExtractor
import pandas as pd

# class ruinews():
#     def __init__(self):
pic_api = ''
upload_api = ''
rt = ''
TIMEOUT = 10

class Snow:
    """雪花算法生成全局自增唯一id"""

    init_date = time.strptime('2022-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
    start = int(time.mktime(init_date) * 1000)
    last = int(time.time() * 1000)
    pc_room = 1
    pc = 1
    seq = 0

    @classmethod
    def get_guid(cls):
        """获取雪花算法生成的id"""
        now = int(time.time() * 1000)
        if now != cls.last:
            cls.last = now
            cls.seq = 1
        else:
            while cls.seq >= 4096:
                time.sleep(0.1)
                return cls.get_guid()
            cls.seq += 1

        time_diff = now - cls.start
        pk = (time_diff << 22) ^ (cls.pc_room << 18) ^ (cls.pc << 12) ^ cls.seq

        return pk


class ruinewsV2():
    hd = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36',
        # 'Content-Type':'Content-Type: application/json;charset=UTF-8',
    }

    def __init__(self,domain_url,web_code='utf-8'):
        self.domain_url=domain_url
        self.web_code=web_code

    def element_convert(self,s):
        # xpath取到的element转换为html
        s = etree.tostring(s, pretty_print=True, method='html', encoding='utf-8')
        s = str(s, encoding="utf-8")
        return s

    def pic_process(self,art_content, art_url, domain_url=''):
        pic_path = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
        pic_url = re.findall('src="(.*?)"', art_content, re.S)
        if domain_url == '':
            domain_url = art_url[0:art_url.find('/', art_url.find('://') + 3)]

        # //data:image
        for url in pic_url:
            pic_name = url.split('/')[-1]
            file = pic_path + '/' + url.split('/')[-1]
            if url.startswith('data:image') and art_content.find('data-src=') > 0:
                art_content = art_content.replace(url, '')
                art_content = art_content.replace('data-src=', '><img src=')
                continue
            if pic_name.find('.') == -1:
                art_content = art_content.replace(url, '')
                continue
            if not os.path.isdir(pic_path):
                os.makedirs(pic_path)
            dnurl = url

            if str(url).startswith('./'):
                dnurl = art_url.replace(art_url.split('/')[-1], '') + url.replace('./', '')
            elif not str(url).startswith('http'):
                dnurl = domain_url + url
            try:
                r = requests.get(dnurl, timeout=5)
                if r.status_code == 200:
                    with open(file, 'wb') as f:
                        f.write(r.content)
                else:
                    continue

                m = MultipartEncoder(
                    fields={'file': (url.split('/')[-1], open(file, 'rb'))}
                )
                headers = {'Content-Type': m.content_type}

                r = requests.post(pic_api, data=m.read(), headers=headers)

                if r.status_code == 200:
                    r = r.text
                    new_img_url = json.loads(r)['url']
                    art_content = art_content.replace(url, new_img_url)
                    os.remove(file)
                else:
                    print('ERR:文件上传接口出错,返回状态码%s' % r.status_code)

            except Exception as e:
                continue

        return art_content

    def filter_tags_tw(self,htmlstr, tags):
        if htmlstr is None or htmlstr == '' or htmlstr == '[]':
            return ''
        htmlstr = ''.join(htmlstr)
        re_h = re.compile('(?!</?(' + tags + ').*?>)<.*?>')
        s = re_h.sub('', htmlstr)  # 去掉HTML 标签
        s = s.replace(' ' * 3, '')
        s = s.replace('<img', '<p')
        s = s.replace('<a', '<p')
        s = s.replace('\t', '').replace('\r', '').replace('\n', '')
        return s

    def check_url(self,url:str,num:int):
        '''
        查重url并写入history.csv文件中
        :return:
        '''
        csv = 'history.csv'
        # 文件不存在创建，存在取前条数据查重
        if os.path.exists(csv):
            df_csv = pd.read_csv(csv).tail(num)
        else:
            df_csv = pd.DataFrame(columns=['url'])
        df_csv.set_index('url')
        csv_ls = []
        # 判断csv文件是否存在
        rtn = False
        if df_csv[df_csv['url'].isin([url])].empty:
            if url not in csv_ls:
                csv_ls.append(url)
                rtn = True
        if len(csv_ls) > 0:
            dfb = pd.DataFrame(csv_ls, columns=['url'])
            if df_csv.empty:
                dfb.to_csv(csv)
            else:
                dfb.to_csv(csv, mode='a', header=False)
        return rtn
    def filter_json_url(self,news_ls):
        #查重json返回的url
        if len(news_ls) == 0:
            print('no data')
            return []
        csv = 'history.csv'
        if os.path.exists(csv):
            df_csv = pd.read_csv(csv)
        else:
            df_csv = pd.DataFrame(columns=['url'])
        df_csv.set_index('url')
        csv_ls = []
        for item in news_ls:
            url = item['url']
            if not url.startswith('http'):
                if url.startswith('/'):
                    url = self.domain_url + url
                elif url.startswith('./'):
                    url = self.domain_url + url[1:]
                else:
                    url = self.domain_url + '/' + url
            if df_csv[df_csv['url'].isin([url])].empty:
                if url not in csv_ls:
                    csv_ls.append(url)

        if len(csv_ls) > 0:
            dfb = pd.DataFrame(csv_ls, columns=['url'])
            if df_csv.empty:
                dfb.to_csv(csv)
            else:
                dfb.to_csv(csv, mode='a', header=False)
            return csv_ls
        else:
            return []
    def get_news_list(self,url,links_xpath,is_etree=False):
        #get list方式 返回列表
        r = requests.get(url, headers=self.hd, verify=False)
        html = r.content.decode(self.web_code)
        if is_etree==True:
            html=etree.HTML(html)
            news_ls=html.xpath(links_xpath)
        else:
            ls_ex = ListPageExtractor()
            news_ls = ls_ex.extract(html, feature=links_xpath)

        if len(news_ls) == 0:
            print('no data')
            return []
        csv = 'history.csv'
        if os.path.exists(csv):
            df_csv = pd.read_csv(csv)
        else:
            df_csv = pd.DataFrame(columns=['url'])
        df_csv.set_index('url')
        csv_ls = []
        for item in news_ls:
            if is_etree==True:
                url=item
            else:
                url = item['url']
            if not url.startswith('http'):
                if url.startswith('/'):
                    url = self.domain_url + url
                elif url.startswith('./'):
                    url = self.domain_url + url[1:]
                else:
                    url = self.domain_url + '/' + url
            if df_csv[df_csv['url'].isin([url])].empty:
                if url not in csv_ls:
                    csv_ls.append(url)

        if len(csv_ls) > 0:
            dfb = pd.DataFrame(csv_ls, columns=['url'])
            if df_csv.empty:
                dfb.to_csv(csv)
            else:
                dfb.to_csv(csv, mode='a', header=False)
            return csv_ls
        else:
            return []
    def get_news_detail(self,url,content_xpath='',is_kwd=False,
                title_xpath='',test_flag=False,proc_art_date='',
                author_xpath='',no_gne_content=True,del_tag='',
                source_xpath='',IS_EN_SITE=False,
                publish_time_xpath='',web_code=''):

        if not url.startswith('http'):

            if url.startswith('/'):
                url = self.domain_url + url
            elif url.startswith('./'):
                url=self.domain_url+url[1:]
            else:
                url = self.domain_url + '/' + url

        art_ex = GeneralNewsExtractor()
        r=requests.get(url, headers=self.hd, verify=False)
        if r.status_code!=200:
            print('request error')
            return
        if web_code:
            art_html = r.content.decode(web_code)
        else:
            art_html = r.content.decode(self.web_code)
        etree_html=etree.HTML(art_html)
        if del_tag != '':
            div = etree_html.xpath(del_tag)

            for d in div:
                d.getparent().remove(d)
        art_html = re.sub(r' style="' + '(.*?)' + '">', '>', art_html)
        try:
            rst = art_ex.extract(art_html, title_xpath=title_xpath,publish_time_xpath=publish_time_xpath,
                                 body_xpath=content_xpath, with_body_html=True,source_xpath=source_xpath,author_xpath=author_xpath)
        except:
            print('GNE解析出错')
            return


        art_title = rst['title']
        art_date = rst['publish_time']
        if no_gne_content==True:
            etree_html=etree.HTML(art_html)
            if content_xpath!='':
                art_content = self.element_convert(etree_html.xpath(content_xpath)[0])
            else:
                art_content = rst['body_html']
        else:
            art_content = rst['body_html']
        if art_title == '' or art_content == '':
            print('title or content is empty')
            return

        art_author = rst['author']
        art_source = rst['source']

        art_url = url
        art_content = self.filter_tags_tw(art_content,'a|p|img|div')

        if not test_flag:
            art_content = self.pic_process(art_content, art_url,self.domain_url)

        art_content=re.sub(r' style="'+'(.*?)'+'">','>',art_content)
        nitem = {}

        nitem['title'] = art_title
        nitem['html'] = art_content
        nitem['source'] = art_source
        nitem['url'] = art_url
        nitem['author'] = art_author
        nitem['releaseAt'] = art_date

        return nitem