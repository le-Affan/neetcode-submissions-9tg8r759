class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = {}

        for i in s1:
            if i in letters.keys():
                letters[i] += 1
            else:
                letters[i] = 1
        
        l, r = 0, len(s1) - 1

        while r <= len(s2):
            window_freq = {}
            
            for i in s2[l:r + 1]:
                if i in window_freq.keys():
                    window_freq[i] += 1
                else:
                    window_freq[i] = 1
            
            if window_freq == letters:
                return True
            else:
                l += 1
                r += 1
        return False
