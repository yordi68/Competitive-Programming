# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.counter = defaultdict(list)
        self.traverse(root , 0 , 1)
        ans = float('-inf')
        for arr in self.counter.values():
            ans = max(ans , arr[-1] - arr[0] + 1)

        return ans

    def traverse(self , root , index , level):
        if root:
            self.counter[level].append(index)
            self.traverse(root.left , (2 * index) + 1 , level + 1)
            self.traverse(root.right , (2 * index) + 2 , level + 1)