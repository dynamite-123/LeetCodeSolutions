# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        res = []

        def dfs(node, res):
            if not node:
                return

            dfs(node.left, res)
            dfs(node.right, res)
            res.append(node.val)

        dfs(root, res)

        return res