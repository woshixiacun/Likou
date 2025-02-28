from collections import OrderedDict



class MultiWindowSys:
    def __init__(self) -> None:
        self.window_que = {}#OrderedDict()
        self.id_list = []
        pass

    def creat_window(self,id,row,col,w,h):
        
        if id in self.window_que.keys() or not self.chek([row,col,w,h]):
            return False
        else:
            self.window_que[id]=[row,col,w,h]
            self.id_list.append(id)
            # print(self.window_que)
            # print(self.id_list)
            return True

    def destroy_window(self,id):
        if id not in self.window_que.keys():
            return False
        else:
            win = self.window_que[id]
            self.window_que.pop(id)
            self.id_list.remove(id)
            # print(self.window_que)
            # print(self.id_list)
        return True

    def move(self,id, d_row,d_col):
        if id not in self.window_que.keys():
            return False
        else:
            self.window_que[id][0]=d_row
            self.window_que[id][1]=d_col
            
            self.id_list.remove(id)
            self.id_list.append(id)
            if not self.chek(self.window_que[id]):
                self.destroy_window(id)
                return False
            return True

    def click(self,row1,col1):
        for  id  in reversed(self.id_list):
            win = self.window_que[id] # r c w h

            if (row1 >= win[0] and row1 <= win[0]+win[3]) and (col1 >= win[1] and col1 <= win[1]+win[2]):
                self.id_list.remove(id)
                self.id_list.append(id)
                # print (id)
                return id
        return -1

    def chek(self,win):
        row=win[0]
        col=win[1]
        w=win[2]
        h=win[3]
        l_up=[row,col]
        r_up=[row,col+w]
        l_down = [row+h,col]
        r_down = [row+h,col+w]
        x=[[row,col],[row,col+w],[row+h,col],[row+h,col+w]]
        res = []
        for i in range(4):
            if (x[i][0] >= 0 and x[i][0] <= 999) and (x[i][1] >= 0 and x[i][1] <= 999):
                res.append(1)
            else:
                res.append(0)
        if 1 in res:
            return True
        return False





mw = MultiWindowSys() #null
print(mw.creat_window(2,70,80,15,17) ) #True
print(mw.creat_window(1,0,10,999,100) )#True
print(mw.move(2,5,6) )#True
print(mw.click(20,20) )# 2
print(mw.destroy_window(2) )# True



