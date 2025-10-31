# 输入获取
maxPrice = 5#int(input())
prices = [1,1,3,4]#list(map(int, input().split()))


# 算法入口
def getResult():
    # 将商品按价格从小到大排序
    prices.sort()

    count = 0
    l = 0  # l指针指向最小价格的商品
    r = len(prices) - 1  # r指针指向最大价格的商品

    # 如果商品价格不超过上限，则优先最小价格和最大价格组合
    while l < r:
        sumPrice = prices[l] + prices[r]

        # 如果最小价格+最大价格 不超过上限，则组合，否则最大价格独立一组
        if sumPrice <= maxPrice:
            l += 1

        r -= 1
        count += 1

    if l == r:
        count += 1

    return count


# 算法调用
print(getResult())