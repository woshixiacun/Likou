str = '123#222235/56' #input()

keybd={
    '1':[',','.'],
    '2':['a','b','c'],
    '3':list('d e f'.split()),
    '4':list('g h i'.split()),
    '5':list('j k l'.split()),
    '6':list('m n o'.split()),
    '7':list('p q r s'.split()),
    '8':list('t u v'.split()),
    '9':list('w x y z'.split()),
    '0':' '
}

s = str.split('#')   # 偶数位 数字； 奇数位英文

res = []

for i in range(len(s)):
    if i % 2 == 0 and s[i] != '':
        s_temp = s[i].split('/')
        for ins in s_temp:
            res.append(ins)
    if i % 2 == 1 and s[i] != '':
        s_temp = s[i].split('/')
        for ins in s_temp:
            count = {}
            for ss in ins:
                count[ss] = count.get(ss, 0) + 1
                
            for key,value in count.items():
                bd_value = keybd[key]
                tm = bd_value[value % len(bd_value) - 1]
                res.append(tm)

print(' '.join(res))

# res =[]
# mod = False
# count = 1


# for i,s in enumerate(str):
#     if s =='#' and mod==False:
#         mod = True
#         continue
#     elif s =='#' and mod==True:
#         mod = False
#         continue

#     if mod:
#         a = 0
#         # if s == '/':
#         #     count = 1
#         #     continue

#         # if i+1 <= len(str) and str[i+1] == str[i]:
#         #     # str[i+1] == str[i]
#         #     count += 1
        
#         # elif i+1 <= len(str) and str[i+1] != str[i]:
#         #       pass

#     else:
#         res.append(s)
#         #  print(int(i))

# print(' '.join(res))