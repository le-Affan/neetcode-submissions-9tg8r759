class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = collections.defaultdict(int)
        freqT = collections.defaultdict(int)

        for i in s:
            freqS[i] += 1
        for i in t:
            freqT[i] += 1
        
        return freqS == freqT

