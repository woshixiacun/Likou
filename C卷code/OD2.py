news = list(map(int,input().split()))
consumers = list(map(int,input().split()))
news_list = []
consumers_list = []
for i in range(0,len(news),2):
    news_list.append([news[i],news[i+1]])
for i in range(0,len(consumers),2):
    consumers_list.append([consumers[i],consumers[i+1]])
#消息按照到达时刻排序
news_list.sort(key=lambda x: x[0])
#定义消费者收到消息内容的数量
res_list = []
for i in range(len(consumers_list)):
    res_list.append([])
#遍历每条消息
for i in range(len(news_list)):
    #查询每条消息，按照优先级顺序是否到达(反向遍历)，如果在消费者订阅，并未取消订阅存入数组
    for j in range(len(consumers_list),0,-1):
        #判断消息达到时刻是否满足消费者要求
        if consumers_list[j - 1][0] <= news_list[i][0] < consumers_list[j - 1][1]:
            res_list[j - 1].append(news_list[i][1])
            break
#逐个打印消费者消息
for contents in res_list:
    if len(contents) == 0:
        print("-1")
    else:
        print(" ".join(map(str, contents)))

# 2 22 1 11 4 44 5 55 3 33
# 1 7 2 3