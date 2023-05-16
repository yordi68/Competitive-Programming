# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = defaultdict(list)
        ans = []
        def traverse(root, curr):
            if not root:
                return

            level[curr].append(root.val)

            traverse(root.left, curr + 1)
            traverse(root.right, curr + 1)

        traverse(root,0)
        
        for arr in level.values():
            ans.append(sum(arr)/len(arr))

        return ans