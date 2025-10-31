# m1 = [0,1]
# m2 = [3,2]

malloc_size = 5#int(input())  # 要申请的内存大小

if malloc_size <= 0 or malloc_size > 100: #总内存1001·
    print(-1)
    exit()

used_memory = []  # 已占用的内存
while True: #不限制输入长度
    try:
        offset, size = map(int, input().split())
        used_memory.append([offset, size])
    except:
        break

arr = [0]*100
for i in used_memory:
    offset, size = i
    for j in range(size):
        arr[offset]=1
        offset+=1


id_l = 0
id_r = 0
# for id,mm in enumerate(arr):

while id_l <= 99 or id_r <= 99:
    if arr[id_l] == 1 and arr[id_r] == 1:
        id_l += 1
        id_r += 1
    if arr[id_l] == 0 and arr[id_r] == 0:
        id_r += 1
    if arr[id_l] == 0 and arr[id_r] == 1:
        len = id_r - id_l
        if len >= malloc_size:
            break
        id_l = id_r

print(-1 if id_l == 100 else id_l)
    
        
