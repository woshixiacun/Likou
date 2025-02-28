def min_people_to_complete_tasks(tasks):
    # 将任务按照结束时间排序
    tasks.sort(key=lambda x: x[1])
    
    # 初始化变量
    max_people = 0
    current_people = 0
    # 用于存储每个时间点的任务开始和结束
    timeline = []
    
    # 遍历任务，更新时间线
    for start, end, _ in tasks:
        # 找到所有在这个任务开始之前结束的任务
        while timeline and timeline[0][1] <= start:
            current_people -= 1
            timeline.pop(0)
        # 开始新任务，增加人数
        current_people += 1
        # 将这个任务的结束时间添加到时间线
        timeline.append([start, end])
        # 更新最大需要的人数
        max_people = max(max_people, current_people)
    
    # 处理所有任务结束后剩余的任务
    while timeline:
        current_people -= 1
        timeline.pop(0)
    
    return max_people

# 任务列表，每个元素为[开始时间, 结束时间, 任务标识]
tasks = [[0,3,3],[1,2,4],[1,3,1],[2,3,1],[0,5,9]]
# 调用函数并打印结果
print(min_people_to_complete_tasks(tasks))