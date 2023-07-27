# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.string = str(root.val)

        if not root:
            return 

        if root.left:
            self.string += '(' + self.tree2str(root.left) + ')'
            
        if root.right:
            if not root.left:
                self.string += '()'

            self.string += '(' + self.tree2str(root.right) + ')'
            
        return self.string