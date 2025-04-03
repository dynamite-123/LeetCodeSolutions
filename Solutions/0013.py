class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        m = val[s[-1]]
        res = 0
        for c in s[::-1]:
            m = max(m, val[c])
            if val[c] < m:
                res -= val[c]
            else:
                res += val[c]

        return res