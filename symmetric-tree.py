# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.symmetry(root , root)
    def symmetry(self , p , q):
        if not q and not p:
            return True
        if not q or not p or p.val != q.val:
            return False

        leftSubtree = self.symmetry(p.left,q.right)
        rightSubtree = self.symmetry(p.right , q.left)
        return leftSubtree and rightSubtree