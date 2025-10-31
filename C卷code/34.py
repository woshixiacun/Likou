# 第一行输入解析
n, end_x = (4, 10)# map(int, input().split()) #N条指令,机器运行的横坐标终点值E

# 记录题解
ans = 0

last_x = 0  # 上一个点的横坐标
last_y = 0  # 上一个点的纵坐标

# 获取n行输入
for _ in range(n):
    # 当前点的横坐标, 当前点纵坐标相较于上一个点纵坐标的偏移量
    cur_x, offset_y = map(int, input().split())

    # cur_x - last_x 结果是上一个点到当前点的横向距离, 这个距离过程中，高度保持为abs(last_y)
    ans += (cur_x - last_x) * abs(last_y)

    # 更新last_x, last_y
    last_x = cur_x
    last_y += offset_y

# 注意结束位置的处理
if end_x > last_x:
    ans += (end_x - last_x) * abs(last_y)

print(ans)