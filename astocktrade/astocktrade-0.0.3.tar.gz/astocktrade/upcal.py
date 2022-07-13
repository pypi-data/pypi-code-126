def up_rate_cal(datalist):
    j = 0
    up_p = 0
    all_ = 0
    while(j+1 < len(datalist)):
            all_ += 1
            if(datalist[j+1] -  datalist[j] > 0 ):
                up_p += 1
            j += 1
    if(all_ != 0):
     rate1 = up_p / all_
    else:
     rate1 = 0
    return rate1