nums = list(map(int,input().split())) #[10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 15]  

def zcy():
    count = {}
    for i in nums:
        # print(list(count.keys()))
        if i not in list(count.keys()):
            count[i]=1
        else:
            count[i]+=1
            
    # print(count)

    maxCount = max(count.values())
    # print(maxCount)

    zhongshu =[]
    for key, val in list(count.items()):
        if val == maxCount:
            zhongshu.append(key)

    zhongshu.sort()

    mid = len(zhongshu)//2
    if len(zhongshu) % 2 == 0:
        # 偶数个数时，取中间两个位置的平均值
        ans = (zhongshu[mid] + zhongshu[mid - 1]) // 2
    else:
        # 奇数个数时，取中间位置的值
        ans = zhongshu[mid]

    print(ans)
    return ans

## 2
# 算法入口
def getResult():
    count = {}

    # 统计各数字出现次数
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # 获取最大出现次数
    maxCount = max(count.values())

    # 将众数挑选出来
    mode = []
    for k in count:
        if count[k] == maxCount:
            mode.append(int(k))

    # 众数升序
    mode.sort()

    # 中位数取值
    mid = len(mode) // 2
    if len(mode) % 2 == 0:
        # 偶数个数时，取中间两个位置的平均值
        return (mode[mid] + mode[mid - 1]) // 2
    else:
        # 奇数个数时，取中间位置的值
        return mode[mid]


# 算法调用
print(getResult())