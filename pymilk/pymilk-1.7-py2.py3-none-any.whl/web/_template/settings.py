from pymilk.web.token_tools import token_tools


debug = True
port = 81

# 根据需求自定义N个token处理器, 如无须token验证, 可全部去掉
tokenT1 = token_tools(token='123456', maxTimeDis=10, batchDis=10)
tokenT2 = token_tools(token='123456789', maxTimeDis=15, batchDis=30)
