class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        res = 1
        l, r = 0, 1
        curr = set()
        curr.add(s[l])

        while l < len(s) - 1:
            while r < len(s) and s[r] not in curr :
                curr.add(s[r])
                res = max(res, len(curr))
                r += 1
            
            while l < len(s) - 1 and r < len(s) and s[l] != s[r]:
                curr.discard(s[l])
                l += 1
            l += 1
            if l < len(s) - 1 and l == r:
                r += 1
        
        return res
            
