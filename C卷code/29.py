# 输入获取
n = int(input())
countries = []

for i in range(n):
    name, gold, silver, bronze = input().split()
    countries.append([int(gold), int(silver), int(bronze), name])


# 算法入口
def getResult():
    countries.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3])) #前三个降序，最后一个升序

    for c in countries:
        print(c[3])


# 算法调用
getResult()