import math 
trees = list(map(int,input().split()))
H = int(input())
if len(trees)<=0 or len(trees)>=10000 or H<=0 or H>=10000:
    print('0')
    exit()

ans = 0

def check(speed):
    cost = 0
    for tree in trees:
        # 以speed速度吃完一颗桃树需要的时间，累加进cost
        cost += math.ceil(tree / speed)
         # 如果已花费时间超过了limit限制，那么说明无法以speed速度在limit时间内吃完所有桃树，此时可以直接返回false
        if cost > H:
            return False
    # 可以以speed速度，在limit小时内吃完所有cnts桃树
    return True

if H >= len(trees):
    if H == len(trees):
        ans = max(trees)
    else:
        maxSpeed = max(trees)
        minSpeed = 1
        while minSpeed <= maxSpeed:
            # 取中间值作为吃桃速度进行尝试
            mid = (minSpeed + maxSpeed) >> 1
            # 如果以mid速度，可以在h小时内吃完cnts所有桃，那么mid就是一个可能解
            if check(mid):
                ans = mid
                # 继续尝试更小的速度
                maxSpeed = mid - 1
            else:
                 # 以mid速度无法在h小时内吃完cnts所有桃，那么mid就取小了，下次应该取更大的吃桃速度
                minSpeed = mid + 1
    print(ans)

else:
    print('0')


    #0000010   0000100


