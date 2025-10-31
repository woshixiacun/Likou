# 输入获取
nums = list(map(int,'10 10 56 34 99 1 87 8 99 3 255 6 99 5 255 4 99 7 255 2 99 9 255 21'.split()))#input()
x, y = map(int, '3 4'.split()) #input()


# 算法入口
def getResult():
    rows = nums[0]
    cols = nums[1]

    graph = [-1] * (rows * cols)

    start = 0
    for i in range(2, len(nums), 2):
        gray = nums[i]
        length = nums[i + 1]

        graph[start:start + length] = [gray] * length

        start += length

    return graph[x * cols + y] #3行：3*10=30个像素，往后多数4个数，即4列


# 算法调用
print(getResult())