import copy

'''
直接赋值：其实就是对象的引用（别名）。

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

字典浅拷贝实例
'''
# a = [1,2,3]
# print(id(a))
 
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)  # b,c,d 和a都是指向同一个地址

# print(id(a), id(b), id(c), id(d))  # 这里a指向了“aaa”所以id变了，但是b,c,d还是指向“123”
# print(a, b, c, d)

# a.pop()   # 数据被修改后，a指向的地址被改变
# print(id(a), id(b), id(c), id(d))  # 这里a指向了“aaa”所以id变了，但是b,c,d还是指向“123”
# print(a, b, c, d)


nums = [1,2,3]

nums.sort()

used = [0,0,0]

result = []

path = []

def backtracking(nums, used):

    if len(path) == len(nums):
        a = copy.deepcopy(path)
        result.append(a)
        return
    
    for i in range(len(nums)):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(nums[i])
        backtracking(nums, used)
        path.pop()
        used[i] = 0
        
backtracking(nums, used)

print(result)
