from tkinter import W
import numpy as np
import pandas as pd
from copy import deepcopy
from pprint import pprint
import requests
from rrdata.utils.rqDate_trade import rq_util_get_last_tradedate, rq_util_if_trade, rq_util_if_traded_now,rq_util_get_real_date
from rrdata.utils.rqDate import rq_util_date_today

#print(rq_util_date_today(), rq_util_if_trade(str(rq_util_date_today())))
file_path = "/mnt/f/Stock/iwencai/"


class Wencai(object):
    """  
    """
    def __init__(self):
      
        self.last_trade_date = rq_util_get_last_tradedate()
        self.date_today = str(rq_util_date_today())
        self.if_traded = rq_util_if_traded_now()
        self.if_trade = rq_util_if_trade(rq_util_date_today)
        
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
        
        self.headers_wc = deepcopy(headers)
        self.headers_wc["Referer"] = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"
        self.headers_wc["Host"] = "www.iwencai.com"
        self.headers_wc["X-Requested-With"] = "XMLHttpRequest"

        self.Question_url = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"

        self.Fields_all = ['股票代码', '股票简称', 
        '归属母公司股东的净利润(同比增长率)[20220331]', '营业收入(同比增长率)[20220331]',
       '销售毛利率[20220331]', '净资产收益率roe(加权,公布值)[20220331]',
       '新股上市日期',
       '预测净资产收益率(roe)平均值[20221231]', '预测净资产收益率(roe)平均值[20231231]',
       '预测净资产收益率(roe)平均值[20241231]', '归属于母公司所有者的净利润[20220331]',
       '股东权益合计[20220331]', 
       '所属同花顺行业', '所属同花顺行业',
       '申购日期', '单账户顶格', '公开发行市值', '网上发行数量','网下发行数量', '网上有效申购户数', '上市板块', '新股主承销商', '网上中签结果公告日', '招股说明书', '打新技巧',
       '营业收入[20220331]', '预测主营业务收入增长率[20221231]', '最新价', '最新涨跌幅', 'hqCode', 'marketId']
        
        self.drop_columns = ['申购日期', '单账户顶格', '公开发行市值', '网上发行数量','网下发行数量', '网上有效申购户数', '上市板块', 
                             '新股主承销商', '网上中签结果公告日','招股说明书', '打新技巧','hqCode', 'marketId'] #,'最新价', '最新涨跌幅','涨跌', '振幅',]
        self.Fields_inc = ['股票代码', '股票简称', '营业收入(同比增长率)','归属母公司股东的净利润(同比增长率)', '销售毛利率',"所属申万行业"]
        
        self.Fields_common = ["股票简称", "股票代码", '最新价',"市盈率(pe)", "市净率(pb)", '总股本', 
                              "所属申万行业",'所属同花顺行业']
        self.Fields_daily = ["股票代码","股票简称",	"开盘价:不复权","最高价:不复权","最低价:不复权", "收盘价:不复权","涨跌幅:前复权","成交量", "成交额","复权因子", "新股上市日期"]
        
        self.Fields_swl = ["股票简称", "股票代码", "市盈率(pe)", "市净率(pb)", "所属申万行业",'所属同花顺行业']
        self.Fields_new_high = ["股票简称", "股票代码", '最新价', '最新涨跌幅', "所属申万行业"]
        
        self.Fields_basic = ["股票简称", "股票代码", "市盈率(pe)", "市净率(pb)", '总市值','a股市值(不含限售股)',"所属申万行业",'所属同花顺行业','所属概念']
        
        self.Fields_rt =  ["股票简称", "股票代码", "年涨跌幅:前复权"] #5日涨幅", "20日涨幅","60日涨幅","245日涨幅"]
        self.Fields_query_daily = ["收盘价不复权","成交量", "复权因子"]

    
    def _fetch_data_from_wencai(self, trade_date=None,fields_query=None, fields_out=None):
        """通过问财接口抓取数据
        Arguments:
            trade_date {[type]} -- [description]
            fields {[type]} -- [description]
        Returns:
            [type] -- [description]
        """
        #fields_query = ["收盘价不复权","成交量", "复权因子"]
        payload = {
            # 查询问句
            "question": "{},{},上市日期<={}".format(trade_date, ",".join(fields_query), trade_date),
            # 返回查询记录总数 
            "perpage": 8000,
            "query_type": "stock"
        }
        try:
            response = requests.get(self.Question_url, params=payload, headers=self.headers_wc)
            if response.status_code == 200:
                json = response.json()
                df_data = pd.DataFrame(json["data"]["data"])
                print(df_data.columns)
                #print(df_data)
                # 规范返回的columns，去掉[xxxx]内容
                df_data.columns = [col.split("[")[0] for col in df_data.columns]
                # 筛选查询字段，非查询字段丢弃
                if not fields_out:
                    df = df_data.drop(columns=self.drop_columns) #, axis=1,inplace=True) #[fields_out]
                    #print(df_data.columns)
                else:
                    df = df_data[fields_out]
                # 增加列, 交易日期 code 设置索引
                trade_date = rq_util_get_real_date(trade_date) if (trade_date and self.if_traded) else rq_util_get_last_tradedate()
                print(f"Real trade date: {trade_date}")
                df = df.assign(trade_date=trade_date, code=df["股票代码"].apply(lambda x: x[0:6])).set_index("trade_date", drop=True)
                return df
                
            else:
                print("连接访问接口失败")
                           
        except Exception as e:
            print(e)

    def fetch_basic(self, trade_date=None, fields_qeury=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_qeury:
            fields_qeury = self.Fields_basic
        if not fields_out:
            fields_out = self.Fields_basic
        return self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_qeury,fields_out=fields_out)


    def fetch_swl(self, trade_date=None, fields_qeury=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_qeury:
            fields_qeury = self.Fields_swl
        if not fields_out:
            fields_out = self.Fields_swl
        return self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_qeury,fields_out=fields_out)
    
    
    def fetch_daily(self, trade_date=None, fields_qeury=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_qeury:
            fields_qeury = self.Fields_query_daily
        if not fields_out:
            fields_out = self.Fields_daily
        return self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_qeury,fields_out=fields_out)
    
    
    def fetch_period_return(self, trade_date=None, fields_qeury=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_qeury:
            fields_qeury = ["一周涨幅,一个月涨幅, 3个月涨幅,六个月涨幅,一年涨幅, 申万行业, 同花顺行业"]
        if not fields_out:
            fields_out = None
        return self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_qeury,fields_out=fields_out)
        
    
    def fetch_finance_inc(self, trade_date=None, fields_qeury=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_qeury:
            fields_qeury = ['营业收入(同比增长率)','归属母公司股东的净利润(同比增长率)', '销售毛利率','净资产收益率roe',"所属申万行业"]
        if not fields_out:
            fields_out = self.Fields_inc
        return self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_qeury,fields_out=fields_out)
    
    
    def fetch_technical(self):
        """ close > bull(upper)
            vol > 2*vol(50)
            close > ma(20) hold  to 1w
            oh > 85, ol > 25
            上市时间满1年，历史新高， 申万行业
            一周涨幅；一个月涨幅； 3个月涨幅；一年涨幅； 行业
        """
        pass
    
    
    def new_high(self, trade_date=None,fields_query=None, fields_out=None):
        if not trade_date:
            trade_date = self.last_trade_date            
        if not fields_query:
            fields_query = ['历史新高','申万行业','上市日期']
        df =  self._fetch_data_from_wencai(trade_date=trade_date, fields_query=fields_query,fields_out=fields_out).sort_values(by=u"所属申万行业")
        #df = df[df[u'上市天数'] > 250]
        df = df[self.Fields_new_high]
        return df
    
    def data_to_excel(self,data=None,file_name=None):
        try:
            data.to_excel(f"{file_path}/{file_name}.xlsx")
            
            print(f"Save data to excel <{file_name}.xlsx> finish !")
        except Exception as e:
            print(e)
    

if __name__ == "__main__":
    trade_date = rq_util_date_today()
    print(trade_date)
    WC = Wencai()
    print(WC._fetch_data_from_wencai())
    #print(WC.fetch_basic())
    #WC.data_to_excel(WC.fetch_basic(), 'stock_basic')
    #print(WC.fetch_swl(fields_out=["股票简称", "股票代码", "市盈率(pe)", "市净率(pb)", "所属申万行业",'所属同花顺行业']))
    #print(WC.fetch_daily(trade_date='2021-06-27'))
    #WC.data_to_excel(WC.fetch_daily(trade_date='2021-06-27'), "stock_daily")
    #print(WC.fetch_finance_inc())
    #WC.data_to_excel(data=WC.fetch_finance_inc(),file_name='finance_inc')
    #print(WC.fetch_period_return(trade_date))
    #WC.data_to_excel(WC.fetch_period_return(trade_date), f"stock_period_rt_{trade_date}")
    #print(WC.new_high(trade_date))
    #WC.data_to_excel(WC.new_high(trade_date),f'new_high_{trade_date}')
    
    
