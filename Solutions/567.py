class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N, n = len(s2), len(s1)
        if n > N:
            return False

        cs1, hm = {}, {}
        for i in range(n):
            cs1[s1[i]] = cs1.get(s1[i], 0) + 1
            hm[s2[i]] = hm.get(s2[i], 0) + 1

        for i in range(n, N):
            if cs1 == hm:
                return True

            hm[s2[i]] = hm.get(s2[i], 0) + 1
            prev = s2[i - n]
            hm[prev] -= 1

            if hm[prev] == 0:
                del hm[prev]
                # hm.pop(prev) 
                #this deletes and return the result, default can be provided to overcome error issue

        return cs1 == hm

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         N, n = len(s2), len(s1)
#         cs1 = {}

#         hm = {}
#         for i in range(n):
#             if s2[i] in hm:
#                 hm[s2[i]] += 1
#             else:
#                 hm[s2[i]] = 1
                
#             if s1[i] in cs1:
#                 cs1[s1[i]] += 1
#             else:
#                 cs1[s1[i]] = 1

#         for i in range(n+1, N):
#             if cs1 == hm:
#                 return True

#             if s2[i] in hm:
#                 hm[s2[i]] += 1
#             else:
#                 hm[s2[i]] = 1

#             hm[s2[i - n - 1]] -= 1
#             if s2[i - n - 1] in hm and hm[s2[i - n - 1]] == 0:
#                 hm.pop(s2[i - n - 1])
#         if cs1 == hm:
#             return True
#         return False