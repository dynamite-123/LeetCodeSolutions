from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        # l root r - inorder traversal
        dummy = TreeNode() # type: ignore
        cur = dummy
        
        def dfs(node):
            nonlocal cur
            if not node: return
            dfs(node.left)
            cur.right = TreeNode(node.val) # type: ignore
            cur = cur.right
            dfs(node.right)
        dfs(root)

        return dummy.right        