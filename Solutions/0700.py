# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # type: ignore
        node = root
        while node:
            if node.val == val: break
            if val > node.val:
                node = node.right
            else: 
                node = node.left
        if not node:
            return None
    
        return node