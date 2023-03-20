# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(root):
            nonlocal arr
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)
        count = dict(Counter(arr))
        count = (sorted(count.items(),key = lambda x : x[1], reverse=True))
        max_ = count[0][1]
        ans = []

        for x , y in count:
            if y == max_:
                ans.append(x)
        return (ans)