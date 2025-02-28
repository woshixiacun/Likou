from collections import deque
'''
分页内存管理
把进程使用的 虚拟内存 划分成大小相等的若干页（每页有编号）
物理内存 也按同样大小分成frame_num个页框
进程访问某页数据时，需要把这一页的数据缓存入物理内存的一个页框内进行访问。
已缓存的页需要记录两个属性：[访问次数，访问时间]

某段时间内，进程先后访问虚拟内存中 页的信息 记录于pages
pages[i]表示要访问的 页的编号，
请计算 依次访问完成后发生页置换的次数

若访问页 已经缓存在页框中，该页的访问次数+1，并更新访问时间为最新
若访问页 没有访问在页框中，则产生缺页中断，这个时候：
    如果有空闲页框，选择其中一个用于缓存该页；设置该页的访问次数为1，访问时间为最新
    如果没有空闲页框，则发生一次 页置换（置换出一页用来缓存）；设置该页的访问次数为1，
    访问时间为最新。置换策略：
        首先，将页框中缓存的页按照访问时间先后，选择前window_size个页 作为过期候选。
        然后，从这些过期候选中，优先选择访问次数最少的；如果有多个，选择最久没有访问的
        （=时间最前面的）
'''

# frame_num = 3  # 3个页框
# window_size = 2 # 候选页为2
# pages = [51,52,53,54,54,51,52,53,54]
# out = 4

frame_num = 4  # 3个页框
window_size = 3 # 候选页为2
pages = [1,1,30,20,5,6,5,20,5,20,1,6,7,6]
out = 2

# frame_num = 4  # 3个页框
# window_size = 3 # 候选页为2
# pages = [1,2,3,4,5,100,5,4,3,2,1,100,1,2,3,4,5,100,5,4,3,2,1,100]
# out = 11

# frame_num = 4  # 3个页框
# window_size = 3 # 候选页为2
# pages = [15,15,60,50,20,80,80,20,50,15,9,80]
# out = 3


class Solution:
    def __init__(self) -> None:
        
        self.fangwen_time = {} #访问次数
        self.t = [] #时间早晚
        self.count = 0

        self.huancun = []
        self.houxuan =[]


    def calc_page_fault_num(self, frame_num: int, window_size:int, pages):
        pages = deque(pages)
        i = 1
        while pages:
            page = pages.popleft()
            if i <= frame_num:
                #有空闲页框
                
                if page in self.huancun:
                    self.huancun.remove(page)
                    self.huancun.append(page)
                    # page已经缓存
                    self.fangwen_time[page][0] +=1
                    self.t.remove(page)
                    self.t.append(page)
                    # 更新时间
                    for t_page in self.t:
                        self.fangwen_time[t_page][1] = self.t.index(t_page)
                else:
                    # page没有缓存
                    i+=1            ##
                    self.huancun.append(page)
                    self.fangwen_time[page] = self.fangwen_time.get(page,[0,0,page]) #【访问次数，访问时间，编号】
                    self.fangwen_time[page][0] += 1

                    self.t.append(page)
                    for t_page in self.t:
                        self.fangwen_time[t_page][1] = self.t.index(t_page)
                    
            else:
                #没有有空闲页框
                if page in self.huancun:
                    self.huancun.remove(page)
                    self.huancun.append(page)
                    # page已经缓存
                    self.fangwen_time[page][0] +=1
                    self.t.remove(page)
                    self.t.append(page)

                    for t_page in self.t:
                        self.fangwen_time[t_page][1] = self.t.index(t_page)

                else:
                    # page没有缓存
                    self.houxuan = self.huancun[:window_size]
                    sort_list =[]
                    for houxuan_page in self.houxuan:
                        sort_list.append(self.fangwen_time[houxuan_page])
                    # 次数少、时间早
                    sort_list = sorted(sort_list, key=lambda x:(x[0],x[1]))
                    zhihuan_page = sort_list[0][-1]
                    # print(zhihuan_page)
                    # print(self.huancun)
                    # 置换
                    self.huancun.remove(zhihuan_page)
                    self.count+=1
                    self.huancun.append(page)

                    # 新缓存页时间=1
                    self.fangwen_time[page] = self.fangwen_time.get(page,[0,0,page]) #【访问次数，访问时间，编号】
                    self.fangwen_time[page][0] = 1


                    #新页时间最新
                    if page in self.t:
                        self.t.remove(page)
                    self.t.append(page)
                    
                    for t_page in self.t:
                        self.fangwen_time[t_page][1] = self.t.index(t_page)                     
        print(self.count)
        return self.count

S = Solution()
S.calc_page_fault_num(frame_num, window_size, pages)