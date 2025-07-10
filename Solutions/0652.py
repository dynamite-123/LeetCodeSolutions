from typing import Optional, List
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]: #type: ignore
        hm = defaultdict(int)
        
        cur = []
        res = []
        def dfs(node):
            if not node:
                return [None]

            cur = [node.val] + dfs(node.left) + dfs(node.right)

            if hm[tuple(cur)] == 1:
                res.append(node)
            hm[tuple(cur)] += 1
            
            if node.val == 4: print(cur, hm[tuple(cur)])
            return cur
            
        
        dfs(root)

        return res