# 输入获取
nums = [2, 8, 3 ,7, 3 ,6 ,3 ,5,5 ,3 ,6, 2 ,7 ,3, 8, 4 ,7, 5]#list(map(int, input().split()))


# 算法入口
def getResult():
    ans = []

    # 上一个点坐标（preX, preY）
    preX = nums[0]
    preY = nums[1]

    # 上一次的运动方向（preDirectX, preDirectY）
    preDirectX = 0
    preDirectY = 0

    for i in range(2, len(nums), 2):
        # 当前点坐标（curX, curY）
        curX = nums[i]
        curY = nums[i + 1]

        # 上一个点到当前点的偏移量（offsetX, offsetY）
        offsetX = curX - preX
        offsetY = curY - preY

        # 根据偏移量得出本次的运动方向
        base = max(abs(offsetX), abs(offsetY))
        directX = offsetX // base
        directY = offsetY // base

        # 如果两次运动的方向不同
        if directX != preDirectX or directY != preDirectY:
            # 则上一个点是拐点，需要记录下来
            ans.extend([preX, preY])

        preX = curX
        preY = curY

        preDirectX = directX
        preDirectY = directY

    # 注意收尾
    ans.extend([preX, preY])

    return " ".join(map(str, ans))


# 算法调用
print(getResult())