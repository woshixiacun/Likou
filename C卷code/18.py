# cards = [input().split() for i in range(5)]

nums, colors = [],[]
for i in range(5):
    card = input().split()
    if card[0]=="J":
        card_num = 11
    elif card[0]=="Q":
        card_num = 12        
    elif card[0]=="K":
        card_num = 13
    elif card[0]=="A":
        card_num = 14
    else:
        card_num = int(card[0])
    
    nums.append(card_num)
    colors.append(card[1])

# print(nums, colors)


def countNums(nums, partCount, maxSameNumCount):
    count = {}

    for num in nums:
        # if count.get(num) is None:
        #     count[num] = 0
        # count[num] += 1
        count[num] = count.get(num, 0) + 1

    if len(count.keys()) != partCount: # 四条、葫芦有2种数字；三条有3种数字
        return False

    return maxSameNumCount in count.values() #有4 就是4条，有3 就是葫芦


# 三条
def isSantiao(nums):
    # 三条由三部分组成，第一个部分由三张相同牌组成，第二个，第三个部分分别是两种不同的牌
    return countNums(nums, 3, 3)


# 葫芦
def isHulu(nums):
    # 葫芦由两部分组成，一个部分三张牌相同，一个部分两张牌相同
    return countNums(nums, 2, 3)


# 四条
def isSitiao(nums):
    # 四条由两部分组成，一个部分四张相同牌，一个部分一张牌
    return countNums(nums, 2, 4)


# 同花
def isTonghua(colors):
    # 同花牌的所有花色都一样
    return len(set(colors)) == 1 # 集合 去重
# # 同花  H、S、C、D表示红桃、黑桃、梅花、方块
# pattern = {}
# for card  in cards:
#     p = card[1]
#     pattern[p] = pattern.get(p, 0) + 1
# # print(len(pattern.keys()))
# if len(pattern.keys()) == 1:
#     print('tonghua')

# 顺子
def isShunzi(nums):

    if nums == [2,3,4,5,14]:  #  特殊顺子A 2 3 4 5
    # if "".join(nums) == "234514":
        return True

    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            return False
    return True


# 算法入口
def getResult():

    nums.sort()

    if isShunzi(nums) and isTonghua(colors):
        return 1
    elif isSitiao(nums):
        return 2
    elif isHulu(nums):
        return 3
    elif isTonghua(colors):
        return 4
    elif isShunzi(nums):
        return 5
    elif isSantiao(nums):
        return 6
    else:
        return 0


# 算法调用
print(getResult())
    