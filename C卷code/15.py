import re

# 输入获取
s = input()


# 算法入口
def getResult():
    words = s.split()

    letter = "[aeiouAEIOU]"

    for i in range(len(words)):
        if re.search(letter, words[i]): # 如果可以在letter中搜索到元素
            words[i] = re.sub(letter, "*", words[i]) # 把元素换成*
        else:
            lst = list(words[i])
            lst[0], lst[-1] = lst[-1], lst[0]
            words[i] = "".join(lst)

    return " ".join(words)


# 算法调用
print(getResult())



#
# .strip() #去除字符串前面和后面的所有设置的字符串
# st = "hello"
# st = st.strip('h,o,e')
# print(st)

# s='Hello me'
# A=s.replace('e','*')
