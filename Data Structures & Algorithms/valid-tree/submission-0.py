class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        nodes = defaultdict(list)

        for a,b in edges:
            nodes[a].append(b)
            nodes[b].append(a) # Since it is an undirected graph
        
        visited = set()
        
        def dfs(curr,parent):
            if curr in visited:
                return False

            visited.add(curr)

            for i in nodes[curr]:
                if i == parent: # We ignore the parent since the edge back to the parent is not a cycle.
                    continue
                if not dfs(i,curr):
                    return False
            return True

        if not dfs(0,-1):
            return False
        
        return len(visited) == 0 # No cycle ≠ Tree since there can be a disconnected node
            