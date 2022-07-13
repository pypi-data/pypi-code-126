import chinese_calendar
import datetime
import pandas as pd
import baostock as bs
import tushare as ts
import requests

def get_tradeday(start_str,end_str):
    start = datetime.datetime.strptime(start_str, '%Y-%m-%d') # 将字符串转换为datetime格式
    end = datetime.datetime.strptime(end_str, '%Y-%m-%d')
    # 获取指定范围内工作日列表
    lst = chinese_calendar.get_workdays(start,end)
    expt = []

    # 找出列表中的周六，周日，并添加到空列表
    for time in lst:
        if time.isoweekday() == 6 or time.isoweekday() == 7:
            expt.append(time)
    # 将周六周日排除出交易日列表
    for time in expt:
        lst.remove(time)
    date_list = [item.strftime('%Y-%m-%d') for item in lst] #列表生成式，strftime为转换日期格式
    return date_list

def getdatafrombaostock(stnamelist,stday,edday,fq,otpath,add_or_rpl): #stday,edday like 'xxxx-xx-xx'  #otpath 以 \\ 结尾

    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    name_list = pd.read_csv(stnamelist)
    L = len(name_list)
    j = 0
    while(j < L):

        stock_code = name_list.ts_code[j]

        rs = bs.query_history_k_data_plus(stock_code,
            "date,time,code,open,high,low,close,volume,amount,adjustflag",
            start_date = stday, end_date = edday,
            frequency = fq , adjustflag = "3")

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        #### 结果集输出到csv文件 ####   
        if(add_or_rpl == 'add'):
          result.to_csv(otpath + stock_code +'.csv', header=None ,index=False,mode='a')
        else:
          result.to_csv(otpath + stock_code +'.csv', index=False)

        print(j+1)

        j += 1


    bs.logout()

def get_alldatebar(st,ed,otpath):#起止日期 like xxxx-xx-xx #otpath 以 \\ 结尾

    pre_path = otpath

    lst = get_tradeday(st,ed)

    i = 0
    while(i < len(lst)):
        s = lst[i]
        lst[i] = s[0]+s[1]+s[2]+s[3]+s[5]+s[6]+s[8]+s[9]
        i += 1


    #44bd527b59125d78c4cb094bd152e6e86bd7ed0fb8056c678439b764

    ts.set_token('44bd527b59125d78c4cb094bd152e6e86bd7ed0fb8056c678439b764')

    pro = ts.pro_api()

    j = 0

    while(j<len(lst)):
        
        df = pro.daily(trade_date=lst[j])

        ticks_df = pd.DataFrame(df)

        ticks_df.to_csv(pre_path + 'T' + lst[j] + '.csv', index=0)

        j += 1
        print("fininsh" + str(j))

def get_tick(stock_code) :
      headers = {'referer': 'http://finance.sina.com.cn'}
      resp = requests.get('http://hq.sinajs.cn/list=' + 'sh' + stock_code, headers=headers, timeout=6)
      data = resp.text
      list1 = data.split(',')
      #{
      # 0 名称
      # 1 今开
      # 2 昨收
      # 3 此时价格
      # 4 最高
      # 5 最低
      # 30 年月天
      # 31 时分秒
      # }
      #last = list1[3]
      #trade_datetime = list1[30] + ' ' + list1[31]
      #self.tick = (trade_datetime,last)
      return list1

