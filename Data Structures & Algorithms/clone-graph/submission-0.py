"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {}

        def clone(currNode):
            if currNode in mapping:
                return mapping[currNode]
            
            currCopy = Node(currNode.val)
            mapping[currNode] = currCopy

            for n in currNode.neighbors:
                currCopy.neighbors.append(clone(n))
            return currCopy
        
        return clone(node) if node else None

        
