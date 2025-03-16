from typing import List

class Soulution:
    def __init__(self) -> None:
        self.buffer = []
        self.result = [[]]
        self.gb = [0,0]
        self.upper_lock = False


    def str_edit(self, input_str:str)->List[str]:

        for str in input_str:
            if self.is_letter(str):
                # 先看大小写
                str = self.change_upper_lower(str)
                # 光标位置
                hang = self.gb[0]
                lie = self.gb[1]
                self.result[hang].insert(lie , str)
                # 更新光标
                self.gb[1] +=1           

            if str =='@':
                #大小写切换
                if self.upper_lock == False:
                    self.upper_lock = True
                else:
                    self.upper_lock = False
            
            if str =='+':
                #光标位置换行，光标右边的内容全部变成新一行。

                # 光标位置
                hang = self.gb[0]
                lie = self.gb[1]

                current_line = self.result[hang]
                
                new_line_left = current_line[:lie]
                new_line_right = current_line[lie:]

                self.result[hang] = new_line_left
                self.result.insert(hang+1,new_line_right)
                
                # 更新光标
                self.gb[0]+=1
                self.gb[1]=0


            if str == "~":
                if self.gb == [0,0]:
                    #如果在首行 行首，不动
                    pass
                elif self.gb[1] == 0:
                    # 更新光标列：
                    self.gb[1] = len(self.result[self.gb[0]-1])

                    # 如果光标在行首，将当前行拼到上一行
                    current_line = self.result[self.gb[0]]
                    self.result[self.gb[0]-1].extend(current_line)
                    self.result.pop(self.gb[0])
                    
                    # 更新光标行
                    self.gb[0] -=1
                else:                   
                    # 退格，删除光标左边字符
                    self.result[self.gb[0]].pop(self.gb[1]-1)
                    self.gb[1]-=1
            
            if str =='-':
                
                if self.gb == [len(self.result),len(self.result[-1])]:
                # 末行不能右移
                    pass
                elif self.gb[1]== len(self.result[self.gb[0]]):
                    down_line = self.result[self.gb[0]+1]
                    self.result[self.gb[0]].extend(down_line)
                    self.result.pop(self.gb[0]+1)

                    # 不更新光标
                else:
                     # 退格，删除光标右边字符
                    self.result[self.gb[0]].pop(self.gb[1])
                                    

            if str in ['^','*','<','>']:
                self.move_gb(str)

        res =[]
        for strs in self.result:
            tem = ""
            for s in strs:
                tem += s
            res.append(tem)

        return res

    def is_letter(self,x):
        # 判断是否字母
        if x.isalpha():
            return True
        else:
            return False
        
    def change_upper_lower(self,x):
        if self.upper_lock == False:
            return x
        else:
            return x.upper()
        
    def move_gb(self,str):
        if str == '^': # up
            #首行不能上移
            if self.gb[0] ==0:  
                pass
            else:
                up_line = self.result[self.gb[0]-1]
                current_line = self.result[self.gb[0]]
                if len(up_line)<self.gb[1]:
                    # 如果上一个行短，移到上一行最后
                    self.gb[0] -= 1
                    self.gb[1] = len(up_line)
                else:
                    self.gb[0] -= 1
                    
        elif str == '*': # down
            #末行不能下移
            if self.gb[0]==len(self.result)-1:
                pass
            else:
                current_line = self.result[self.gb[0]]
                down_line = self.result[self.gb[0]+1]
                if len(down_line)<self.gb[1]:
                    # 如果下一行短，移到下一行最后
                    self.gb[0] += 1
                    self.gb[1] = len(down_line)
                else:
                    self.gb[0] += 1

        elif str =="<": #left
            if self.gb == [0,0]:
                #首行不能左移
                pass
            elif self.gb[1]==0:
                # 如果在的行首，移到上一行最后
                up_line = self.result[self.gb[0]-1]
                current_line = self.result[self.gb[0]]
                self.gb[0] -= 1
                self.gb[1]=len(up_line)
            else:
                self.gb[1] -= 1
        
        elif str ==">": #right
            if self.gb == [len(self.result)-1,len(self.result[-1])]:
                # 末行不能右移
                pass
            elif self.gb[1]== len(self.result[self.gb[0]]):
                 # 如果在的行尾，移到下一行最前
                self.gb[0] += 1
                self.gb[1] = 0
            else:
                self.gb[0] += 1
           
if __name__ == "__main__":
    in_str = "aaaa+bbbb~@cc<<<^--d@d"
    # in_str = "^*><+++^^a**b+^"
    # in_str = "azcya+@bbbb@+ccccc"
    out_right = ["aaDd","bbbCC"]
    solu = Soulution()
    output = solu.str_edit(in_str)

    print(output)



