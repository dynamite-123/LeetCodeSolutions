class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int: # type: ignore
        N = len(questions)
        cache = {}
        def helper(i):
            if i > N - 1:
                return 0
            if i in cache: return cache[i]
            cache[i] = max(
                helper(i + 1),
                questions[i][0] + helper(i + 1 + questions[i][1])
            )
            return cache[i]
        return helper(0)

        # N = len(questions)
        # @cache
        # def helper(i):
        #     if i > N - 1:
        #         return 0
        #     return max(
        #         helper(i + 1),
        #         questions[i][0] + helper(i + 1 + questions[i][1])
        #     )
        # return helper(0)
