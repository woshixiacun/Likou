# 输入获取
k = 0# int(input())
n = 7# int(input())
words = [input() for _ in range(n)]


# 算法入口
def getResult():
    chain = [words.pop(k)]  #去除列表中的第k个元素

    prefix = {}
    for word in words:
        w = word[0]
        if prefix.get(w) is None: #如果字典里没有“w”开头的字母
            prefix[w] = []
        prefix[w].append(word)

    for w in prefix.keys():
        prefix[w].sort(key=lambda x: (-len(x), [ord(i) for i in x])) 
        # 长度从大到小、字母顺序从小到大
    while True:
        tail = chain[-1][-1] #最后一个单词的最后一个字母

        if prefix.get(tail):
            chain.append(prefix[tail].pop(0))
        else:
            break

    return "".join(chain)


# 调用算法
print(getResult())