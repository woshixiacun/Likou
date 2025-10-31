

s = "abcabcbb"

def lengthOfLongestSubstring( s):
    r = 0
    n = len(s)
    occ = set()
    ans = 0
    for l in range(n):
        while  r < n and s[r] not in occ:
            occ.add(s[r])
            r += 1
        if l == 0:
            continue
        else:
            occ.remove(s[l-1])

        ans = max(ans, r-l+1)
    return ans


def lengthOfLongestSubstring2(s):
    ans = 0
    left = 0
    window = set()
    for r, c in enumerate(s):
        while c in window:
            window.remove(s[left])
            left += 1
        window.add(c)
        ans = max(ans, r-left+1)

    return ans

print(lengthOfLongestSubstring2(s))

def lengthOfLongestSubstring3(s):

    ans = 0
    for i in range(len(s)):
        tmp_ans = 0
        for j in range(len(s)):
            if j < i:
                continue
            occ = set()
            for k in range(i,j+1):
                if s[k] not in occ:
                    occ.add(s[k])
                else:
                    break
                if k == j:
                    tmp_ans = max(tmp_ans, j-i+1)
        ans = max(ans, tmp_ans)
    return ans

print(lengthOfLongestSubstring3(s))




