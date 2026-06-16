# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        if head:
            l, t = head, head
        else:
            return head
        
        length = 0
        while l:
            l = l.next
            length += 1
        
        target = length - n + 1

        count = 1
        while count != target:
            if count == target - 1:
                prev = t
            t = t.next
            count += 1
        
        nxt = t.next
        if prev != None:
            prev.next = nxt
        return head




