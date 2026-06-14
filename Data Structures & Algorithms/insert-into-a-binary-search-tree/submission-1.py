# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def traverse(node):
            if not node:
                return TreeNode(val = val, left=None, right=None)

            if node.val > val:
                node.left = traverse(node.left)
            
            elif node.val < val:
                node.right = traverse(node.right)
            
            return node
            
        return traverse(root)
