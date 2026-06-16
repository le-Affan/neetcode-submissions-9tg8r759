class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxLen = 1
        word = set(s[l])

        while r < len(s):
            if s[r] not in word:
                word.add(s[r])
                maxLen = max(maxLen, len(word))
                r += 1
            else:
                l += 1
                r += 1
        return maxLen


            
