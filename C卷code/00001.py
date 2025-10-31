def min_people_to_complete_tasks(tasks):
    # 将任务按照开始时间排序
    tasks.sort(key=lambda x: x[0])
    
    # 初始化变量
    max_people = 0
    current_people = 0
    # 用于存储每个时间点需要完成的任务数量
    time_line = [0] * (max(task[1] for task in tasks) + 1)
    
    # 遍历任务，更新时间线
    for start, end, _ in tasks:
        time_line[start] += 1      # 开始时间点，人数加1
        time_line[end] -= 1       # 结束时间点，人数减1
    
    # 计算每个时间点需要的人数
    for i in range(1, len(time_line)):
        time_line[i] += time_line[i - 1]  # 累加前面的人数
        max_people = max(max_people, time_line[i])  # 更新最大需要的人数
    
    return max_people

# 任务列表，每个元素为[开始时间, 结束时间, 任务标识]
tasks = [[0,3,3],[1,2,4],[1,3,1],[2,3,1],[0,5,9]]
# 调用函数并打印结果
print(min_people_to_complete_tasks(tasks))