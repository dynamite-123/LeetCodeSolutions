class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        choices = ['a', 'b', 'c']

        def helper(prev):
            nonlocal res
            nonlocal k
            
            if len(res) == n:
                k -= 1
                return k == 0

            for i in range(3):
                if i == prev:
                    continue
                res.append(choices[i])
                if helper(i):
                    return True
                # print(res, res[:-1], k)
                res = res[:-1]
            return False
        
        helper(-1)
        return "".join(res)