# 本题实际考试时会核心代码模式，无需处理输入输出，只需要写出merge方法实现即可
def merge(roomTimes):
    # 将各个会议按照开始时间升序
    roomTimes.sort(key=lambda x: x[0])

    # 记录合并后的会议室占用时间段
    ans = []

    # 上一个会议占用时间段
    pre = roomTimes[0]
    for i in range(1, len(roomTimes)):
        # 当前会议占用时间段
        cur = roomTimes[i]

        if cur[0] <= pre[1]:
            # 当前会议开始时间 <= 上一个会议结束时间，则两个会议时间重叠，可以合并
            # 注意合并时，结束时间取两个时间段中较大的结束时间
            pre[1] = max(pre[1], cur[1])
        else:
            # 否则不可以合并
            ans.append(pre)
            pre = cur

    ans.append(pre)

    return ans


# 输入输出处理
n = 4#int(input())

roomTimes = []
for _ in range(n):
    roomTimes.append(list(map(int, input().split())))

for start, end in merge(roomTimes):
    print(f"{start} {end}")