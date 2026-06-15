"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}

        if head != None:
            p1 = head
        else:
            return head

        while p1 != None:
            mapping[p1] = Node(p1.val)
            p1 = p1.next
        
        for original, copy in mapping.items():
            copy.next = mapping.get(original.next)
            copy.random = mapping.get(original.random)
            # We use .get() to handle cases where mapping would return None
        return mapping.get(head)    