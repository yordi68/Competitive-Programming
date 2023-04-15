# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def evenSum(node,parent,gran):
            nonlocal ans
            if not node:
                return 
            if gran % 2 == 0:
                ans += node.val
            evenSum(node.left,node.val,parent)
            evenSum(node.right,node.val,parent)
        evenSum(root,-1,-1)
        return ans