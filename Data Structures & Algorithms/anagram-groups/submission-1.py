class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for i in strs:
            if ''.join(sorted(i)) in anag.keys():
                anag[sorted(i)].append(i)
            else:
                anag[sorted(i)] = [i]
        
        res = []
        for i in anag.values():
            res.append(i)
        
        return res