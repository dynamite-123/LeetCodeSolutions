"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: #type: ignore
        if not node: return None
        hm = {}

        def dfs(node):
            if node in hm:
                return hm[node]
        
            new_node = Node(node.val)
            hm[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return hm[node]
        return dfs(node)