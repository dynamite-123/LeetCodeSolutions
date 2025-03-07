# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]: # type: ignore
        if not inorder:
            return None
        root = TreeNode(postorder.pop()) # type: ignore
        mid = inorder.index(root.val)
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        root.left = self.buildTree(inorder[0 : mid], postorder)

        return root