class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang={}

        for i in strs:
            base="".join(sorted(i))
            if base not in ang:
                ang[base]=[]
                ang[base].append(i)
            elif base in ang:
                ang[base].append(i)
        
        return list(ang.values())
                
            






