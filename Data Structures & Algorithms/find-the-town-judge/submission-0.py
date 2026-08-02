class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        ind2 = {}
        for i in range(len(trust)):
            if trust[i][1] in ind2.keys():
                ind2[trust[i][1]] += 1
            else:
                ind2[trust[i][1]] = 1
        
        for key, val in ind2.items():
            if val == n - 1:
                res = key
                break
        
        for i in range(len(trust)):
            if trust[i][0] == res:
                res = -1
                break
        return res
