import re

# 输入获取
s = input()
tmp = re.compile(r"A=\{(.+)},B=\{(.+)},R=(.+)").search(s)
A = list(map(int, tmp.group(1).split(",")))
B = list(map(int, tmp.group(2).split(",")))
R = int(tmp.group(3))


# 算法入口
def getResult():
    ans = []

    for a in A:  #1 2 3
        cnt = 0
        for b in B:  #167
            if b < a:
                continue

            if b - a <= R  or cnt == 0:
                ans.append(f"({a},{b})")
                cnt += 1
            else:
                break

    return "".join(ans)


# 算法调用
print(getResult())