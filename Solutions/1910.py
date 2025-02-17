class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:


        # while True:
        #     idx = s.find(part)
        #     if idx == -1:
        #         break
        #     s = s[:idx] + s[idx + len(part):]
        # return s


       # - stack based approach
        
        n1, n2 = len(s), len(part)

        if n1 < n2:
            return s


        res = list(s[0:n2])
        l = n2

        for i  in range(n2, n1):
            if l >= n2:
                if part == "".join(res[-n2:]):
                    l -= n2
                    for j in range(n2):
                        res.pop()
            res.append(s[i])
            l += 1

        if l >= n2:
                if part == "".join(res[-n2:]):
                    l -= n2
                    for j in range(n2):
                        print(res[-1])
                        res.pop()
        

        return "".join(res)