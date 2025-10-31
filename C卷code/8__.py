class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class CycleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, val):
        node = Node(val)

        if self.size > 0:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.head.prev = self.tail
        self.tail.next = self.head
        self.size += 1

    def remove(self, cur):
        pre = cur.prev
        nxt = cur.next

        pre.next = nxt
        nxt.prev = pre

        cur.next = cur.prev = None

        if self.head == cur:
            self.head = nxt

        if self.tail == cur:
            self.tail = pre

        self.size -= 1

        return nxt


# 输入获取
n = int(input())


# 算法入口
def getResult():
    link = CycleLinkedList()

    for i in range(1, n + 1):
        link.append(i)

    num = 1
    cur = link.head

    while link.size > 1:
        if num == 3:
            num = 1
            cur = link.remove(cur)
        else:
            num += 1
            cur = cur.next

    return cur.val


# 算法调用
print(getResult())