class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find Solution

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1): # Func. to find the root parent
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] # Compression for optimization of Union Find
                res = par[res]
            return res
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2: # Same parent so no need to merge
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n

        for n1, n2 in edges:
            res -= union(n1,n2)
        return res



