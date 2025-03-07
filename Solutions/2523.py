class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]: # type: ignore
        def get_primes(n, left):
            res = []
            prime = [True for i in range(n+1)]
            p = 2
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            for p in range(left, n+1):
                if prime[p] and p != 1:
                    res.append(p)
            return res
        res = get_primes(right, left)
        n = len(res)
        if n < 2:
            return [-1, -1]

        l, r = res[0], res[1]
        dif = res[1] - res[0]

        for i in range(1, n - 1):
            if res[i + 1] - res[i] < dif:
                l, r = res[i], res[i + 1]
                dif = res[i + 1] - res[i]

        return [l, r]