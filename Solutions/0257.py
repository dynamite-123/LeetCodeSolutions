# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: #type: ignore
        res = []
        def dfs(node, path):
            if not node: return 
            if not node.right and not node.left:
                path.append(node.val)
                res.append("->".join(str(num) for num in path))
                path.pop()
                return 
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return res