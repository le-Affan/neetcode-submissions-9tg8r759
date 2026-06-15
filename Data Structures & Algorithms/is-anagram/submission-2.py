from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        freqS, freqT = defaultdict(int), defaultdict(int)

        for i in s:
            freqS[i] += 1
        for i in t:
            freqT[i] += 1
        
        return True if freqS == freqT else False

        