# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(node, subNode):
            if not node or subNode:
                return False

            if node != subNode:
                return False
            
            left = check(node.left,subNode.left)
            right = check(node.right, subNode,right)

            return left and right
        
        return check(root, subRoot)


