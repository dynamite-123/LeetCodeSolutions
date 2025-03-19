# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # type: ignore

        if not root: return TreeNode(val) # type: ignore
        cur = root

        while cur:
            if val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val) # type: ignore
                    break
            elif val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val) # type: ignore
                    break
            else:
                if val > cur.val:
                    cur.right = TreeNode(val) # type: ignore
                else:
                    cur.left = TreeNode(val) # type: ignore
                break
        


        return root