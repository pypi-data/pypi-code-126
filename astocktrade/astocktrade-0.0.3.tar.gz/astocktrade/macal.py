def ma_yh_cal(bar_x_m,x,y,h_or_d,store_len):
    may_yh = []
    sum = 0.0
    l1 = len(bar_x_m)
    st_p = l1 - 1
    loop1 = (y*60)/x   
    if(st_p - loop1 < 0):
        return may_yh
    step1 = 1
    if(h_or_d == 0):
        step1 = 60/x
    else:
        step1 = 240/x
    ct = 1
    if(h_or_d == 0):
        ct = y
    else:
        ct = y/4

    num_in = 0

    while(st_p + 1 > loop1):
        #print(st_p,l1)
        i = st_p
        while(i > st_p - loop1):
            sum += bar_x_m.close[i]
            i -= step1        
        ma_y = sum / ct
        sum = 0.0
        may_yh.append((ma_y))
        num_in += 1
        if(num_in >= store_len):
            break
        st_p -= step1
    may_yh.reverse()
    return may_yh