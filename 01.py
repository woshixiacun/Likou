import math
# n=1

# A=[[0,3,3],#0
#    [1,2,4],#1
#    [1,3,1],#2
#    [2,3,1],#3
#    [0,5,9]]#4
n=2

A=[[1,4,10],
   [0,2,1],
   [5,10,1]]

t_start = 0
t_end = 0
for a in A:
    t_start = min(t_start,a[0])
    t_end=max(t_end,a[1])

delta_t = t_end-t_start
# print(t_start,t_end,delta_t)

cnt = [0]*delta_t
print(cnt)
for a in A:
    bred=a[2]
    t_start = a[0]
    t_end = a[1]
    
    k=0
    while k <bred:
        print('循环次数:',k,f'<{bred},{a}')
        for i in range(t_start,t_end):
            print(f'面包{a[2]}之',i)
            k+=1
            cnt[i]+=1
            if k >= bred:
                break
    print('--------task end----------')
print(cnt)
# total = 0
# for i in cnt:
#     total+=i
ave = sum(cnt)/delta_t
# print(ave)

result = int(ave/n)
print(result)

