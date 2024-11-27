# 输入获取 1 1 5 1 5 2 4 4
commands = list(map(int, input().split()))

# 算法入口
def getResult():
    screen = []   #  a
    clip = []
    isSelect = False
    
    for command in commands:  # [1 1 5 1 5 2 4 4]
        if command == 1: # a
            if isSelect:   # true false
                screen.clear()
            screen.append("a")
            isSelect = False
        elif command == 2:  # ctrl-c
            if isSelect:
                clip.clear() 
                clip.extend(screen)   #
        elif command == 3: #ctrl-x
            if isSelect:
                clip.clear()
                clip.extend(screen)
                screen.clear()
                isSelect = False
        elif command == 4: #ctrl-v
            if isSelect:
                screen.clear()
            screen.extend(clip)
            isSelect = False 
        elif command == 5: #ctrl-a
            if len(screen) != 0:
                isSelect = True

    return len(screen)

# 调用算法
print(getResult())