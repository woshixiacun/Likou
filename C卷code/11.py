m = 3 # int(input())
requirements = [3, 5, 3, 4] # list(map(int,input().split()))
N = len(requirements)


# if not 1<= N/2 <= m <=10000:
#     a=1
#     b=2
#     print('0')

def check(limit):
    """
    :param limit: 每辆自行车的限重
    :return: m辆自行车，每辆限重limit的情况下，能否带走n个人
    """
    l = 0  # 指向体重最轻的人 #index
    r = len(requirements) - 1  # 指向体重最重的人

    # 需要的自行车数量
    need = 0

    while l <= r:
        # 如果最轻的人和最重的人可以共享一辆车，则l++,r--，
        # 否则最重的人只能单独坐一辆车，即仅r--
        if requirements[l] + requirements[r] <= limit:
            l += 1
        r -= 1
        # 用掉一辆车
        need += 1

    # 如果m >= need，当前有的
    # +
    # ++
    # +自行车数量足够
    return m >= need


def getResult():
    # 排序
    requirements.sort()

    # 每辆自行车的限重 至少是 最重的那个人的体重
    low = requirements[-1]
    # 每辆自行车的限重 至多是 最重的和次重的那两个的体重
    high = requirements[-2] + requirements[-1]

    ans = high

    # 二分取中间值
    while low <= high:
        mid = (low + high) >> 1

        if check(mid):
            # 如果mid限重，可以满足m辆车带走n个人，则mid就是一个可能解，但不一定是最优解
            ans = mid
            # 继续尝试更小的限重，即缩小右边界
            high = mid - 1
        else:
            # 如果mid限重，不能满足m辆车带走n个人，则mid限重小了，我们应该尝试更大的限重，即扩大左边界
            low = mid + 1

    return ans


# 算法调用
print(getResult())