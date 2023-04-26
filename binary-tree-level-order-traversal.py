# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = defaultdict(list)
        def traverse(root, cur):
            if not root:
                return
            level[cur].append(root.val)
            traverse(root.left, cur + 1)
            traverse(root.right, cur + 1)

        traverse(root, 0)
        for arr in level.values():
            ans.append(arr)

        return ans