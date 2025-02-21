# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # type: ignore
        mind = float("inf")
        arr = []

        def dfs(node: TreeNode): # type: ignore
            nonlocal mind

            if not node: return 
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        arr.sort()
        
        for i in range(len(arr) - 1):
            mind = min(mind, abs(arr[i] - arr[i+1]))
        return mind
