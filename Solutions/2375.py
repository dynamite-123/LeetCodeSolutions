class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res , stack = [], []
        for i in range(n + 1):
            stack.append(f"{i + 1}")

            while stack and (i == n or pattern[i] == "I"):
                res.append(stack.pop())

        return "".join(res)