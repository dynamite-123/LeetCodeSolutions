# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        s = 0
        def dfs(node):
            nonlocal s
            if not node:
                return

            dfs(node.right)
            s += node.val
            node.val = s
            dfs(node.left)

            return
    
        dfs(root)
        return root

        # to preserver the original tree
        # s = 0
        # def dfs(node):
        #     nonlocal s
        #     if not node:
        #         return None

        #     new_node = TreeNode()
        #     new_node.right = dfs(node.right)
        #     s += node.val
        #     new_node.val = s
        #     new_node.left = dfs(node.left)

        #     return new_node
    
        # new_root = dfs(root)
        # return new_root