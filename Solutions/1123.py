import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        # BFS Solution
        hm = {}
        level = []
        q = collections.deque([root])

        while q:
            qlen = len(q)
            level.clear()
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node)
                    if node.left: 
                        q.append(node.left)
                        hm[node.left] = node
                    if node.right: 
                        q.append(node.right)
                        hm[node.right] = node

        temp = collections.deque(level.copy())

        while len(temp) > 1:
            tlen = len(temp)
            for _ in range(tlen):
                t = temp.popleft()
                if hm[t] not in temp:
                    temp.append(hm[t])
        return temp[0]
        