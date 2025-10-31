n = int(input())
heights = list(map(int,input().split()))
weights = list(map(int,input().split()))
# 算法入口
def getResult():
    students = []

    for i in range(n):
        students.append([heights[i], weights[i], i + 1])

    students.sort(key=lambda x: (x[0], x[1], x[2]))

    return " ".join(map(lambda x: str(x[2]), students))


# 算法调用
print(getResult())

# print(list(map(lambda x, y: x+y,[1,3,5,7,9],[2,4,6,8,10])))# Python中map和lambda的套用无法直接显示，需要加list
# #结果如下：
# [3, 7, 11, 15, 19]