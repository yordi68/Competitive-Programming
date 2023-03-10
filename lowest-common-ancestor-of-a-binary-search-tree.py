# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.commonAncestor(root , p , q)
        

    def commonAncestor(self , node , p , q):
        if not node:
            return
        if p.val <= node.val  <= q.val:
            return node
        if q.val <= node.val  <= p.val:
            return node
        if node.val < p.val or node.val < q.val:
            return self.commonAncestor(node.right , p, q)
        if node.val > p.val or node.val > q.val:
            return self.commonAncestor(node.left , p, q)