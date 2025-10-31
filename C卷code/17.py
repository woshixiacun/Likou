
# 输入获取
arr = input().split()
# arr = 'Who Love Solo'
sumV = 0
for wd in arr:
    sumV += len(wd)
# sumV = 0
# for i in range(len(arr)):
#     sumV += len(arr[i])

print(round(sumV / len(arr), 2))