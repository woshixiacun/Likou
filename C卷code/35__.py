import re

# 输入获取
s = '7#6$5#12'#input()


# 算法入口
def getResult(s):
    p = re.compile("(\\d+)\\$(\\d+)")

    while True:
        m = p.search(s)
        if m:
            subS = m.group()
            x = int(m.group(1))
            y = int(m.group(2))
            s = s.replace(subS, str(3 * x + y + 2), 1)  # 注意这里replace只能进行替换第一次出现的，不能替换多次，因此replace方法第三个参数为1，表示只替换首次匹配
        else:
            break

    arr = list(map(int, s.split("#")))

    x = arr[0]
    for y in arr[1:]:
        x = 2 * x + 3 * y + 4

    return x


# 算法调用
print(getResult(s))