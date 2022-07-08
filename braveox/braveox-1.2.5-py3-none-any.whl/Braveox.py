# -*- coding: utf-8 -*-
def braveox(a, g=0):
    if g == 0:
        print("关注贝拉哞，点点关注哞，谢谢了哞")
        print("https://space.bilibili.com/672353429/")
        print('说明：一=1，二=2，终=0')
    if a == 1 or a == 2 or a == 3:
        if a == 1:
            return "第一次勇敢牛牛"
        if a == 2:
            return "第二次勇敢牛牛"
        if a == 3:
            return "第三次勇敢牛牛"
    else:
        x = []
        jieguo = ''
        if a < 0:
            jieguo += '-'
            a *= -1
        if int(a) == 0:
            jieguo += '终'
        xiaoshu = a-int(a)
        zhengshu = int(a)
        while zhengshu > 2:
            b = zhengshu % 3
            zhengshu = zhengshu//3
            if b == 0:
                x.append("终")
            if b == 1:
                x.append("一")
            if b == 2:
                x.append("二")
        if zhengshu == 1:
            x.append("一")
        if zhengshu == 2:
            x.append("二")
        for i in range(-1, -1*len(x)-1, -1):
            jieguo += x[i]
        if int(a) != a:
            jieguo += '.'
            x = []
            for i in range(8):
                xiaoshu *= 3
                b = int(xiaoshu)
                xiaoshu -= int(xiaoshu)
                if b == 0:
                    x.append("终")
                if b == 1:
                    x.append("一")
                if b == 2:
                    x.append("二")
            for i in x:
                jieguo += i
        return jieguo
