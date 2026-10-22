class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        l, r = 0, 1
        maxLen = 1
        word = set(s[l])

        while r < len(s):
            if s[r] not in word:
                word.add(s[r])
                maxLen = max(maxLen, len(word))
                r += 1
            else:
                while s[r] in word:
                    word.remove(s[l])
                    l += 1

        return maxLen


            
