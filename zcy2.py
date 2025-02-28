# 1<=procNum<=5,100<=maxMemSize<=1000
#1<=deviceType<=3,1<=memSize<=100,1<=deviceID<=1000

# deviceType有【无线、数通、接入】3种类，数值1 2 3，针对每一种有一个进程管理，编号也是1 2 3 
# 每个进程组有procNum个进程（procID 编号从0开始）
# 每个进程管理多个设备，进程资源的上限maxMemSize,每次新增加管理一个设备，都要消耗内存资源
import functools

# a = [[0,200],[1,200],[3,500],[4,500]]

{'1':[[0,200],[1,200]],'2':[[0,200],[1,200]],'3':[[0,200],[1,200]]}

# 初始化，每组procNum个进程，资源上限maxMemSize
class DeviceMgtSystem():

    def __init__(self, procNum: int, maxMemSize: int):   
        self.procNum = procNum
        self.maxMemSize = maxMemSize
        
        pro_list = []
        for i in range(procNum):
            pro_list.append([i, maxMemSize])
        self.processgrps = {'1': pro_list,
                           '2': pro_list,
                           '3': pro_list}
        self.info = []

    # 在deviceType对应进程组，按照【负载均衡】选择一个进程，创建deviceID进行管理，
    # 内存消耗为memSize。创建成功，返回进程编号
    # 进程组里面所有进程组的剩余内存资源都不足，失败，返回-1
    
    # 负载均衡:优先选择内存  空闲较多 的进程。若空闲内存相同，选择小编号
    # 用例保证每次传入的deviceID不同
    def creaDevice(self, deviceID: int, deviceType: int, memSize: int):
        processgrp = self.processgrps[str(deviceType)]

        mem = 0
        for  aa  in processgrp:
            if aa[1]> mem:
                mem = aa[1]
                procID = aa[0]
        # print(id, mem)
        new_mem = mem-memSize
        if new_mem < 0:
            print(-1)
            return -1 
        else:
            self.processgrps[str(deviceType)][procID][1]=new_mem
            
            deviceinfo =[deviceID, memSize, procID, deviceType]
            self.info.append(deviceinfo)
            
            print(procID)
            return procID
        

    # 删除设备deviceID，
    # 如果存在设备，删除成功，释放内存，返回true
    # 否则返回false
    def deleteDevice(self, deviceID: int):
        for x, devices in enumerate(self.info):
            if devices[0] == deviceID:
                self.info.remove(x)
                return True
        return False
                

    # 返回deviceType对应进程组内所有设备信息的列表，或者为空列表[]
    # 设备信息格式：[deviceID，MemSize，procID]
    
    # 返回顺序：优先按照 设备消耗的内存MemSize 降序；
    # 如有相同，按照设备procID升序
    # 如果还有相同，按照deviceID升序
    def queryDevice(self, deviceType):
        info_list = []
        for devices in self.info:
            if devices[-1] == deviceType:
                info_list.append(devices[:-1])
        
        sorted_info_list = sorted(info_list, key=lambda x: (-x[1], x[2], x[0]))
        print(sorted_info_list)
        return sorted_info_list



# data = [[3, 30, 1],[8, 50, 0], [12, 30, 1]]
# # 使用 sorted 函数对数据进行排序
# sorted_data = sorted(data, key=lambda x: (-x[1], x[2], x[0]))

# print(sorted_data)

DM = DeviceMgtSystem(2,200) # null
DM.creaDevice(8,1,50) # 0  #负载均衡规则，选择在进程0创建
DM.creaDevice(12,1,30) # 1  #进程组1的进程1创建，返回1
DM.creaDevice(3,1,30) # 1 # 进程组1中选择空闲多的进程1创建，返回1
DM.queryDevice(1) #[[8,50,0],[3,30,1],[12,30,1]] #
DM.creaDevice(15,1,30) # 0 #进程组1的进程0创建，返回0
DM.queryDevice(1) # [[8,50,0],[15,30,0],[3,30,1],[12,30,1]]
print(DM.deleteDevice(10))  # false 


