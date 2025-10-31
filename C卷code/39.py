import re

# 输入获取
n, b_sub, sub = input().split()

covertStr = "0123456789abcdefghijklmnopqrstuvwxyz"


# 将十进制数num转为base进制数
def toBase(num, base):
    if num < base:
        return covertStr[num]
    else:
        return toBase(num // base, base) + covertStr[num % base]


def isValid(s, n):
    #  含前导的0只有0值本身合法
    if s.startswith("0"):
        return s == "0"

    # 被减数，减数只能包含字符0-9，a-z
    if re.search("[^0-9a-z]", s) is not None:
        return False

    # 被减数，减数长度最多100    9999 10000  A
    if len(s) > 100:
        return False

    # 被减数，减数的每位不能超过n
    for c in s:
        if c.isnumeric() and int(c) >= n:  # 比如2进制数的每一位不能超过2
            return False
        elif c.isalpha() and ord(c) - 87 >= n:  # 比如16进制数每一位不能超过f
            return False

    return True


# 算法入口
def getResult(n, b_sub, sub):
    n = int(n)
    if n < 2 or n > 35:
        return "-1"

    if not isValid(b_sub, n) or not isValid(sub, n):
        return "-1"

    b_sub_val = int(b_sub, n)
    sub_val = int(sub, n)

    diff = toBase(abs(b_sub_val - sub_val), n)
    sign = "0" if b_sub_val >= sub_val else "1"

    return sign + " " + str(diff)


# 算法调用
print(getResult(n, b_sub, sub))