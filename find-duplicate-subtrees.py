# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = Counter()

    def dfs(root):
      if not root:
        return ''

      string = str(root.val) + '*' + dfs(root.left) + '*' +  dfs(root.right)
      
      count[string] += 1
      if count[string] == 2:
        ans.append(root)
      return string

    dfs(root)
    return ans