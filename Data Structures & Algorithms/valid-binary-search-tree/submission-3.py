# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if not node:
                return True
            
            if node.left == None and node.right == None:
                return True

            elif not node.left and node.right.val < node.val:
                return False
            
            elif not node.right and node.left.val > node.val:
                return False

            elif node.left.val > node.val or node.right.val < node.val:
                return False
            
            left = check(node.left)
            right = check(node.right)

            return left and right
        
        return check(root)

        
        