
####
# 输入获取
n, m = map(int, input().split())
msgs = [list(map(int, input().split())) for _ in range(m)]


# 并查集实现
class UnionFindSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x

    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)

        if x_fa != y_fa:
            self.fa[y_fa] = x_fa


# 算法入口
def getResult():
    # 如果第一行 n 和 m 的值超出约定的范围时，输出字符串”Null“。
    # 1<=n,m<100000
    if n < 1 or n >= 100000 or m < 1 or m >= 100000:
        print("NULL")
        return

    ufs = UnionFindSet(n + 1)

    for a, b, c in msgs:
        if a < 1 or a > n or b < 1 or b > n:
            # 当前行 a 或 b 的标号小于 1 或者大于 n 时，输出字符串‘da pian zi‘
            print("da pian zi")
            continue

        if c == 0:
            # c == 0 代表 a 和 b 在一个团队内
            ufs.union(a, b)
        elif c == 1:
            # c == 1 代表需要判定 a 和 b 的关系，如果 a 和 b 是一个团队，输出一行’we are a team’,如果不是，输出一行’we are not a team’
            print("we are a team" if ufs.find(a) == ufs.find(b) else "we are not a team")
        else:
            # c 为其他值，输出字符串‘da pian zi‘
            print("da pian zi")


# 算法调用
getResult()