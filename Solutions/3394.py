class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool: #type: ignore
        xs, ys = [], []

        for rect in rectangles:
            xs.append((rect[0], rect[2]))
            ys.append((rect[1], rect[3]))
        
        xs.sort()
        ys.sort()

        l, r = xs[0]
        res = 0
        for i, j in xs:
            if r > i:
                r = max(r, j)
                continue
            r = j
            res += 1
            if res >= 2: return True
        

        l, r = ys[0]
        res = 0
        for i, j in ys:
            if r > i:
                r = max(r, j)
                continue
            r = j
            res += 1
            if res >= 2: return True


        return False
   