class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # type: ignore
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)

        return res
        