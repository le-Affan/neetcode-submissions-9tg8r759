# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        tail.next = head

        curr = tail
        count = 0

        while count <= right:
            if count < left:

                if count == left - 1:
                    preList, prev = curr, curr
                
                    curr = curr.next
                    count += 1
                    continue

                curr = curr.next
                count += 1
                continue
            
            if count == left:
                endList = curr

            if left <= count:      
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
                count += 1
        
        endList.next = curr
        preList.next = prev

        return tail.next

"""
Move to the node just before the part we want to reverse.

Keep track of:
- preList: the node before the reversal starts
- endList: the first node of the section being reversed

Reverse the nodes from left to right in-place using the standard
linked list reversal technique.

After reversing:
- Connect preList to the new start of the reversed section.
- Connect endList (which is now the end of the reversed section)
  to the remaining part of the list.

A dummy node is used so the same logic works even when the reversal
starts at the head of the list.
"""