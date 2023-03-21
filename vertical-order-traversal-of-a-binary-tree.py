# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.columnCounter = defaultdict(list)
        self.columnBuilder(root , 0 , 0)

        self.columnCounter = dict(sorted(self.columnCounter.items(),key=lambda x:x[0]))

        for arr in self.columnCounter.values():
            arr.sort()
            temp = []
            for i in range(len(arr)):
                temp.append(arr[i][1])

            ans.append(temp)

        return ans

    def columnBuilder(self , root , x , y):
        if root:
            self.columnCounter[y].append((x , root.val))
            self.columnBuilder(root.left , x + 1 , y - 1)
            self.columnBuilder(root.right , x + 1 , y + 1)