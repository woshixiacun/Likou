class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.replace(' ','')
        # print(s)
        # s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
        # ['+','-','.']
        fushu = False
        my_dict= {
                'num':[],
                'fuhao':[],
                'kongge':[]
                }    
        for sub_s in s:
            if sub_s in ['+','-']:
                if len(my_dict['num'])!=0:
                    break
                if len(my_dict['fuhao'])!=0:
                    break
                if sub_s == '-':
                    fushu = True
                my_dict['fuhao'].append(sub_s)
                 
            elif sub_s.isdigit():
                my_dict['num'].append(sub_s)

            elif not sub_s.isdigit() and sub_s != " ":  # 字母 or '.'
                break
            
            elif sub_s == ' ':
                if len(my_dict['num']) !=0 or len(my_dict['fuhao']) !=0:
                    break
                else:
                    my_dict['kongge'].append(sub_s)

        if len(my_dict['num'])==0:
            return 0

        ans = 0
        for i in my_dict['num']:
            ans = ans*10 + int(i)
        if fushu == True:
            ans = -ans

        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        return ans
        # return my_dict
        
class Solution2:
    def myAtoi(self, s: str) -> int:

        start = 0
        flag = True

        for sub_s in s:
            if sub_s == " ":
                start = start + 1
                continue
            
            elif sub_s == "-":
                flag = False
                start = start + 1
                break
            elif sub_s == "+":
                start = start + 1
                break
            else:
                break

        ans = 0
        for sub_s in s[start:]:
            if sub_s.isdigit():
                ans = ans * 10 + int(sub_s)

            if sub_s.isalpha():
                break

        if not flag:
            return -ans

        return ans            
                

# x = "words and 987"
# x = "1337c0d3"
x ="   +0 123"
a = Solution().myAtoi(x)
print(a)
