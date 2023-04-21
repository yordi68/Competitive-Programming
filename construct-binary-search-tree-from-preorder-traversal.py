# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        for i in range(1 , len(preorder)):
            self.traverse(TreeNode(preorder[i]) , root)
        
        return root


    def traverse(self , node , root):
        if not root:
            return node

        if node.val < root.val :
            root.left = self.traverse(node , root.left)
            return root
        else:
            root.right = self.traverse(node, root.right)
            return root