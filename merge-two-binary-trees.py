# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(root1 , root2):
            if not root2 and not root1:
                return 
            x = root1.val if root1 else 0
            y = root2.val if root2 else 0
            node = TreeNode(x+y)
            left1 = root1.left if root1 else None
            right1 = root1.right if root1 else None
            left2 = root2.left if root2 else None
            right2 = root2.right if root2 else None
            node.left = merge(left1,left2)
            node.right = merge(right1, right2)
            return node
        return merge(root1,root2)