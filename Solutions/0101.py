# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # type: ignore
        res1, res2 = [], []

        def dfspre(node, res):
            if not node:
                res.append(None)
                return 

            res.append(node.val)
            dfspre(node.left, res)
            dfspre(node.right, res)

        def dfspost(node, res):
            if not node:
                res.append(None)
                return 

            res.append(node.val)
            dfspost(node.right, res)
            dfspost(node.left, res)
        
        dfspre(root.left, res1)
        dfspost(root.right, res2)

        return res1 == res2