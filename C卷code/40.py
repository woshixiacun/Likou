# version1 = list(input().split('.'))
# version2 = list(input().split('.'))

# # 去除前导0
# def rmLeadZero(x):
#     tmp = x.lstrip("0")
#     return "0" if tmp == "" else tmp


# if len(version1) < len(version2):
#     version1.extend(['0'] * (len(version2) - len(version1)))
# else:
#     version2.extend(['0'] * (len(version1) - len(version2)))

# flag = 0
# for i in range(len(version1)):
#     v1 = list(rmLeadZero(version1[i]))
#     v2 = list(rmLeadZero(version2[i]))

#     if len(v1) < len(v2):
#         v1.extend(['0'] * (len(v2) - len(v1)))
        
#     else:
#         v2.extend(['0'] * (len(v1) - len(v2)))


#     version1[i] = v1  
#     version2[i] = v2  


# print(version1 > version2)

# #     # for j in range(v1):

# #     if v1 > v2:
# #         flag = 1
# #         print(1)
# #         break
# #     elif v1 < v2:
# #         flag = 1
# #         print(-1)
# #         break
    
# # if flag == 0:
# #     print(0)

# ##---------
# # 去除前导0
# # def rmLeadZero(x):
# #     tmp = x.lstrip("0")
# #     return "0" if tmp == "" else tmp

# # version1 = list(map(rmLeadZero,input().split('.')))
# # version2 = list(map(rmLeadZero,input().split('.')))


# 输入获取
v1 = input()
v2 = input()


# 去除前导0
def rmLeadZero(x):
    tmp = x.lstrip("0")
    return "0" if tmp == "" else tmp


# 将大版本按"."切割为子版本列表
def convert(version):
    return list(map(rmLeadZero, version.split(".")))


# 算法入口
def getResult():
    arr1 = convert(v1)
    arr2 = convert(v2)

    n = max(len(arr1), len(arr2))

    for i in range(n):
        # 空字符和0相等，比如 1 和 1.0 相等
        tmp1 = arr1[i] if len(arr1) > i else "0"
        tmp2 = arr2[i] if len(arr2) > i else "0"

        if tmp1.isdigit() and tmp2.isdigit():
            tmp1 = int(tmp1)
            tmp2 = int(tmp2)

        if tmp1 > tmp2:
            return 1
        elif tmp1 < tmp2:
            return -1

    return 0


# 算法调用
print(getResult())