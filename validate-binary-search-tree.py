# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            self.isValidBST(root.left)
            self.arr.append(root.val)
            self.isValidBST(root.right)
        
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))