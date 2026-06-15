# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Not the most optimal solution. Most optimal would require you to stop
        # after 'k' nodes have been added to the result... I think...
        
        res = []

        def inOrder(node):
            if not node:
                return 
            
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return res[k - 1]