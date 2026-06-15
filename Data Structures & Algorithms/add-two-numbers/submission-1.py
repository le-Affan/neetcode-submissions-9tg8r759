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

        while p1 or p2 or carry == 1:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            total = v1 + v2 + carry
            if total >= 10:
                tail.next = ListNode(val = total % 10)
                carry = 1
            else:
                tail.next = ListNode(val = total)
                carry = 0
            tail = tail.next
            if p1:
                p1 = p1.next 
            if p2:
                p2 = p2.next
        
        return dummy.next
            