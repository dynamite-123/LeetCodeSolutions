from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, N = len(board), len(board[0]), len(word)
        visited = set()

        def helper(ind, i, j):
            if ind == N:
                return True

            if not (0 <= i < m and 0 <= j < n) or (i, j) in visited:
                return False

            if board[i][j] != word[ind]:
                return False

            visited.add((i, j))
            cur = (
                helper(ind + 1, i + 1, j) or
                helper(ind + 1, i - 1, j) or
                helper(ind + 1, i, j + 1) or
                helper(ind + 1, i, j - 1)
            )
            visited.remove((i, j))
            return cur

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(0, i, j):
                    return True
        return False