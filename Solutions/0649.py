class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        rc = dc = 0
        rq, dq = collections.deque(), collections.deque() # type: ignore

        for i, c in enumerate(senate):
            if c == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while dq and rq:
            if rq[0] < dq[0]:
                dq.popleft()
                rq.append(rq.popleft() + N)
            else:
                rq.popleft()
                dq.append(dq.popleft() + N)
        
        return 'Radiant' if rq else 'Dire'
    