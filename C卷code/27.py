# 输入获取
import math

x, y = map(int, input().split())


# 算法入口
def getResult(x, y):
    print(max(1, math.ceil(math.log10(x / math.pow(26, y)))))


# 算法调用
getResult(x, y)