class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        res = 1
        l, r = 0, 1
        curr = set(s[l])

        while r < len(s):
            if s[r] not in curr:
                curr.add(s[r])
                res = max(res, len(curr))
                r += 1
            else:
                while s[l] in curr:
                    curr.discard(s[l])
                    l += 1
        return res

        
            
