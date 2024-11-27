# # 访问历史日志的条数
# n = int(input())

# # 记录各层级上各关键字出现的频次
# cnts = []

# # 遍历历史日志2
# for _ in range(n):
#     # 将日志按照 "/" 分割，注意split函数会将 "/a/b/c" 会分割出数组 ["", "a", "b", "c"]，因此a,b,c的层级就是其索引值
#     urlComponents = input().split("/")

#     # 遍历url的各层级
#     for level in range(len(urlComponents)):
#         urlComponent = urlComponents[level]

#         # 如果cnts不存在对于层级
#         if level >= len(cnts):
#             # 则创建对应层级
#             cnts.append({})

#         # 获取对应层级
#         cnts[level][urlComponent] = cnts[level].get(urlComponent, 0) + 1

# # 要查询的给定层级, 要查询的关键字
# tar_level, tar_urlComponent = input().split()

# tar_level = int(tar_level)

# if tar_level >= len(cnts):
#     # 如果要查询的层级超出了统计范围，则返回0
#     print(0)
# else:
#     # 获取对应层级上对应关键字出现的频次，如果没有出现，则返回0
#     print(cnts[tar_level].get(tar_urlComponent, 0))


## 2

s = input()
s = int(s)

str_total = []
for i in range(s):
    str = input()
    str_total.append(str)

s = input().split()

level = int(s[0])
key = s[1]

value = 0
for str in str_total:
    
    str_list = str.split('/')
    str_list = str_list[1:]

    if level <= len(str_list) and str_list[level - 1] == key:
        value += 1

print(value)

