# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        else:
            s, f = head, head.next

        while f and f.next != None:
            s = s.next
            f = f.next

            if s == f:
                return True
        return False
    

        
        