# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 3-Step Solution

        # Step 1: Finding the midpoint of the list
        if head.next != None:
            slow, fast = head, head.next
        else:
            return None

        while fast != None:
            slow = slow.next
            fast = fast.next
            if  fast != None:
                fast = fast.next
        
        # Step 2: Reversing the second half to make
        #         pointer movement easier during weaving
        rev_curr, rev_prev = slow.next, None
        slow.next = None

        while rev_curr:
            # Saving the head of 2nd part for Step 3
            if rev_curr.next == None:
                head2 = rev_curr

            # Standard LL Rev. procedure
            rev_temp = rev_curr.next
            rev_curr.next = rev_prev
            rev_prev = rev_curr
            rev_curr = rev_temp
        
        # Step 3: Weaving the second half into the first
        w1_curr = head
        w1_temp = w1_curr.next

        w2_curr = head2
        w2_temp = w2_curr.next

        while w2_curr:
            # Weaving
            w1_curr.next = w2_curr
            w2_curr.next = w1_temp

            # Pointer Update
            w1_curr = w1_temp
            w1_temp = w1_temp.next
            w2_curr = w2_temp
            if w2_curr == None:
                break
            else:
                w2_temp = w2_temp.next
        

        












        