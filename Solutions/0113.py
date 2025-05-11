from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]: # type: ignore
        if not root:
            return []
            
        res = []

        def dfs(node, cur, s):
            cur.append(node.val)
            s += node.val

            if not node.left and not node.right:
                if s == targetSum:
                    res.append(cur.copy())
            if node.left:
                dfs(node.left, cur, s)
            if node.right:
                dfs(node.right, cur, s)
            cur.pop()

        dfs(root, [], 0)
        return res