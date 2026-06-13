# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (p and not q) or (q and not p):
            return False

        if p == None and q == None:
            return True

        elif not p.val == q.val:
    
            return False

        else:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return left and right
        
        