from pinyin import get


def SortByName(lt):
    nsl = [x for x in 'abcdefghijklmnopqrstuvwxyz' +
           'abcdefghijklmnopqrstuvwxyz'.upper()+'0123456789']
    ns = {}
    for index, x in enumerate(nsl):
        ns[x] = index+1
    lt1 = []
    rst_y = []
    rst = []
    for index, x in enumerate(lt):
        lt1.append(get(x, delimiter='', format='strip'))

    for x in range(len(lt1)):
        s = lt1[x]
        rst.append('')
        rst_y.append('')
        for i, y in enumerate(s):
            rst_y[x] = (lt[x])
            lt1[x] = lt1[x][:i] + str(ns[y])+lt1[x][i+len(str(ns[y])):]
            rst[x] = (lt1[x][:i] + str(ns[y])+lt1[x][i+len(str(ns[y])):])
    x = 0
    flag = True
    while x < len(rst)-1 and flag:
        for y in range(len(rst[x])):
            j = y
            if int(rst[x][j]) > int(rst[x+1][j]):
                rst[x], rst[x + 1] = rst[x + 1], rst[x]
                rst_y[x], rst_y[x + 1] = rst_y[x + 1], rst_y[x]
                flag = False
                break
            elif int(rst[x][j]) == int(rst[x+1][j]):
                continue
            else:
                flag = False
                break
        x += 1
    return rst_y


print(SortByName(['04809', 'jask']))
