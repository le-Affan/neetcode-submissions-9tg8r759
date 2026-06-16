# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def dfs(node):
            if not node:
                return self.isValid
            
            if node.left:
                if node.left.val >= node.val:
                    self.isValid = False
                    return self.isValid
            if node.right:
                if node.right.val <= node.val:
                    self.isValid = False
                    return self.isValid
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.isValid
            


            
