'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。


示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
 

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
'''
# hashtable={'a':[1,2],'b':[1,2,3]}

# print(hashtable.values)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # letter_dic={}
    hashtable = dict()
    for word in strs:
        word_ = sorted(word)
        key = "".join(word_)
        # hashtable[key].append(word)
        print(key)
        if key in hashtable.keys():
            hashtable[key].append(word)
        else:
            hashtable[key]=[word]
    return list(hashtable.values())

groupAnagrams(strs)
# print(A)       

import collections

class Solution2:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())



        
