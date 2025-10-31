# s = input().split()
# A_num = int(s[0])
# B_num = int(s[1])

# team_total = []
# for i in range(2):
#     team = int(input().split())
#     team.append(str)


import sys
# l1, l2= 2,2
# A=[1,2]
# B=[2,3]

while True:
    try:
        l1, l2 = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        sumA = sum(A)
    
        sumB = 0
        setB = set()
    
        for b in B:
            sumB += b
            setB.add(b)
    
        # 由于本题必然存在解，因此sumA-sumB的结果肯定可以整除2，如果不能整除则half_diff为小数，
        # 而half_diff = a - b，其中a,b都是整数，因此不可能存在half_diff是小数的情况
        half_diff = (sumA - sumB) // 2
    
        # 记录用于交换的最小的a
        minA = sys.maxsize
        # 记录题解
        ans = ""
    
        for a in A:
            b = a - half_diff
    
            if b in setB: #先满足能找到b
                if a < minA:  #再满足a尽可能小
                    minA = a  
                    ans = f"{a} {b}"
    
        print(ans)
    except:
        break


