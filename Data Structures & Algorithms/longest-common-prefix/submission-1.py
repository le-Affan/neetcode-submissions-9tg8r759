class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        longest = 0
        ind = 0

        for i,n in enumerate(strs):
            if len(n) > longest:
                longest = len(n)
                ind = i
        
        word = strs[ind]

        for i in range(len(word)):
            curr = word[i]
            match = True
            for j in strs:
                if i >= len(j):
                    match = False
                    break
                if j[i] != curr:
                    match = False
                    break
                else:
                    continue
            if match == True:
                res += word[i]
            if match == False:
                break
        return res
            
                

