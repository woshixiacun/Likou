from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 3:
            rowtype = numRows
        else:
            rowtype = 2*numRows-2
        # print(rowtype)
        row_num = []
        for x in range(rowtype):
            if x < numRows:
                row_num.append(x)
            else: 
                y = (numRows-1)-(x-(numRows-1))
                row_num.append(y)

        harsh = defaultdict(list)
        this_row = 0
        for id,sub_s in enumerate(s):
            
            row = row_num[this_row]
            harsh[row].append(sub_s)
            # print(harsh)
            this_row += 1
            if this_row == rowtype:
                this_row = 0
        result = ''.join(''.join(harsh[k]) for k in sorted(harsh))
        return result
        

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = [i for i in range(numRows)]
        print(temp)
        temp += temp[1:-1][::-1]  # 就是去掉首尾后，再把剩余部分倒序。
        print(temp)

        res = [''] * numRows
        n = len(s)

        for i in range(n):
            res[temp[i%len(temp)]] += s[i]

        return ''.join(res)


s = "PAYPALISHIRING"
numRows = 1
# s = "P"
# numRows = 1
# s = "PAYPALISHIRING"
# numRows = 4
a = Solution().convert(s,numRows)
print(a)  #"PAHNAPLSIIGYIR"
