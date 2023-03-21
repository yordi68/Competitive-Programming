# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverseSum(root)
        return self.ans


    def traverseSum(self , root):
        if not root:
            return [0 , 0]

        leftSum , leftCount = self.traverseSum(root.left)
        rightSum , rightCount = self.traverseSum(root.right)

        Sum = (leftSum + rightSum) + root.val
        count = rightCount + leftCount + 1

        if root.val == (Sum // count):
            self.ans += 1

        return [Sum , count]