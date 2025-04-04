from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # type: ignore
        # DFS
        def dfs(node):
            if not node: return None
        
            if node == p or node == q: return node

            left, right = dfs(node.left), dfs(node.right)

            if left and right: return node

            return left if left else right

        return dfs(root)

        # BFS
        # hm = {}
        # que = deque([root])
        
        # while que:
        #     qlen = len(que)
        #     for _ in range(qlen):
        #         node = que.popleft()
        #         if node:
        #             if node.left:
        #                 hm[node.left] = node
        #                 que.append(node.left)
        #             if node.right:
        #                 hm[node.right] = node
        #                 que.append(node.right)
        # temp = {p}

        # while p in hm:
        #     p = hm[p]
        #     temp.add(p)

        # while q in hm:
        #     if q in temp: return q
        #     q = hm[q]
        # if q in temp: return q