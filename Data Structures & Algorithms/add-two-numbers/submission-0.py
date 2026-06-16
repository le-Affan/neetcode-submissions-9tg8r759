# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        p1, p2 = l1, l2
        carry = 0

        while p1 and p2:
            total = p1.val + p2.val + carry
            if total >= 10:
                tail.next = ListNode(val = total % 10)
                carry = 1
            else:
                tail.next = ListNode(val = total)
                carry = 0
            tail = tail.next
            p1 = p1.next
            p2 = p2.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
        
        c = dummy.next
        if carry == 1:
            while c.next != None:
                c = c.next
            c.next = ListNode(val = 1)
        return dummy.next
            