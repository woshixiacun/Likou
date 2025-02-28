#  不重复节点访问数
'''
有向图  n个节点  编号0~ n-1 
包含n条有向边
每个节点作为起点都有一条有向边

给你n个节点对应有向边的终点
求以每个节点为起点出发
沿有向边前进
最大不重复访问节点数

返回一组数据作为答案,其中第i个数表示,如果从节点i开始执行该过程,你可以访问到的不同节点数
输入:第一行为数组长度n
第二行为n个数据value[n],分别代表节点i通往的节点值

2<=n<=10^5
0<=valune[i]<=n-1
value[i]!=i

输出
n个数据,代表每个节点作为起点访问的节点数
n个数用空格分开

输入
5
1 2 3 4 0
输出
5 5 5 5 5
'''

edges = [1,2,0,0]
n=len(edges)
def countVisitedNodes(edges):
    tu = {}
    for start,end in enumerate(edges):
        tu[start]=end
    print(tu)

    result = []
    for i in range(n):
        res = [i]
        end =i
        while tu[end] not in res:
            end = tu[end]
            res.append(end)
            print(end,res)
        len_res = len(res)
        result.append(len_res)
    return result

        
print(countVisitedNodes(edges))