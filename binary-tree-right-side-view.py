# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.counter = defaultdict(int)
        self.rightside(0 , root)
        ans = []
        for val in self.counter.values():
            ans.append(val)
        return ans

    def rightside(self , level ,root):
        if root:
            self.counter[level] = (root.val)
            self.rightside(level + 1 , root.left)
            self.rightside(level + 1 , root.right)