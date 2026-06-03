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