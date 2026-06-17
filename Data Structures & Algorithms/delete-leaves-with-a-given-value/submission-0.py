# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def NodeDelete(node):
            if not node:
                return
            
            if (node.left == node.right == None) and node.val == target:
                return None
            
            node.left = NodeDelete(node.left)
            node.right = NodeDelete(node.right)

            if (node.left == node.right == None) and node.val == target:
                return None

            return node
        
        return NodeDelete(root)


