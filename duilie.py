from collections import deque
s = "olveleetcode"
class Solution:
    
    def firstUniqChar(self,s):
#-----    
        # count = {}
        # for letter in s:
        #    count[letter] = count.get(letter, 0) + 1
        # for id,i in enumerate(s):
        #     if count[i]==1:
        #         return id
        # return -1
#------
        position = dict()
        q = deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i # {字母：下表}
                q.append(ch,i) #(字母，下标)
            else:
                position[ch]=-1 #{ch:-1}
                while q and position[q[0][0]]==-1:
                    q.popleft()
            if not q:
                return -1
            else:
                return q[0][1]


sol=Solution().firstUniqChar(s)
print(sol)