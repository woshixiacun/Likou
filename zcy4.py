from collections import deque

class FileTarSys:
    # 初始化，0时刻开始，以based 整数划分窗口[i*base,(i+1)base),每次对时间窗口打包
    # 打包后的一个tar文件：大小不超过max_size；文件数不超过max_count
    def __init__(self,base:int,max_count:int,max_size:int):
        self.base = base
        self.max_count = max_count
        self.max_size = max_size
        
        self.file_list = deque([])
        self.tar_list = []

        self.time_win = 0
        self.time_win_next = 1
        self.cnt_file = 0

        self.flag = 0


    # 创建普通文件，三个参数表示：[时间戳，编号，大小]
    # file_id全局唯一，time递增
    def create_file(self,time:int,file_id:int,size:int):
        file = [time, file_id, size]
        self.file_list.append(file)

    # 对每个时间窗口打包。按照tar生成顺序，返回tar文件的属性值
    # 按照普通文件创建顺序，逐个打包；
    # 如果 已经存在是生成的tar文件，尝试向最新的里面追加
    #如果 tar文件不存在，或者超过打包约束，生成一个新的tar文件
    #被打包后，普通文件被删除
    # tar 格式[时间戳，编号，大小]，时间戳为素有文件中时间最早的，编号也是最早的文件的编号，大小是所有普通文件大小总和
    def tar(self):#-->list[]

        # if self.flag ==0 and len(self.file_list) != 0:
        if self.flag ==0:
            if len(self.file_list) != 0:
                self.tar_list.append(self.file_list[0])
                self.file_list.popleft()

                self.cnt_file+=1
                self.flag =1
            else:
                return []
        
        if self.flag ==1:
            while self.file_list:
            # for file in self.file_list:
                file = self.file_list[0]
                # print('------',file)
                
                time = file[0]
                id = file[1]
                size = file[2]
                
                if int(time/self.base)==self.time_win_next:
                    self.time_win += 1
                
                if self.time_win <self.time_win_next:
                    if self.cnt_file < self.max_count:
                        if size+self.tar_list[-1][2]<=self.max_size:
                            self.tar_list[-1][2]+=size
                            self.cnt_file+=1
                            self.file_list.popleft()
                        else:
                            self.tar_list.append(file)
                            self.file_list.popleft()
                            self.cnt_file=1
                    else:
                        self.tar_list.append(file)
                        self.file_list.popleft()
                        self.cnt_file=1

                elif self.time_win == self.time_win_next:
                    self.tar_list.append(file)
                    self.file_list.popleft()
                    self.cnt_file=1

                    self.time_win_next +=1

        return self.tar_list
    
# FTS = FileTarSys(100,2,100)  #null
# print(FTS.create_file(1,1,90))#null
# print(FTS.create_file(3,13,20))#null
# print(FTS.create_file(4,4,1))#null
# print(FTS.create_file(4,5,1))#null
# print(FTS.create_file(100,16,100))#null

# print(FTS.tar()) #[[1,1,90],[3,13,21],[4,5,1],[100,16,100]]

# print(FTS.create_file(101,2,1))#null

# print(FTS.tar())#[[1,1,90],[3,13,21],[4,5,1],[100,16,100],[101,2,1]]
    
FTS = FileTarSys(100,10,200)  #null
print(FTS.tar())
print(FTS.create_file(90,0,100))#null
print(FTS.create_file(91,1,199))#null
print(FTS.create_file(93,3,90))#null
print(FTS.tar())# 90 0 100  91 1 199  93 3 90
print(FTS.create_file(94,4,10))#null
print(FTS.tar()) # 90 0 100  91 1 199  93 3 100
print(FTS.create_file(101,6,90))#null
print(FTS.create_file(101,5,120))#null
print(FTS.tar()) # 90 0 100  91 1 199  93 3 100  101 6 90  101 5 120
