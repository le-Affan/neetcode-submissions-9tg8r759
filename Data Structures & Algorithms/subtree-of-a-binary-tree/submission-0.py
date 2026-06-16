# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return (check(root.left, subRoot.left) and check(root.right, subRoot.right))
        
        found = False

        if check(root, subRoot):
            found = True
        elif check(root.left, subRoot) or check(root.right, subRoot):
            found = True
        return found
            