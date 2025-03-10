class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowels = defaultdict(int) # type: ignore
            l = consonents = res = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowels[word[r]] += 1
                else:
                    consonents += 1
                while len(vowels) == 5 and consonents >= k:
                    res += len(word) - r
                    if word[l] in 'aeiou':
                        vowels[word[l]] -= 1
                    else:
                        consonents -= 1                
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                    l += 1

            return res

        return atleastk(k) - atleastk(k + 1)
        
    # initial approach
        # consonents = l = r = res = 0
        # vowels = []
        # if word[0] in 'aeiou':
        #     vowels.append(word[0])
        # while r < len(word) - 1 and l < len(word):
        #     if consonents > k:
        #         if word[l] not in 'aeiou':
        #             consonents -= 1
        #         else:
        #             vowels.remove(word[l])
        #         l += 1
        #     else:
        #         r += 1
        #         if word[r] not in 'aeiou':
        #             consonents += 1
        #         else:
        #             vowels.append(word[r])
        #     if consonents == k and len(set(vowels)) == 5:
        #         for i in range(l, r + 1):
                    
        #         res += 1
        #     print(word[l: r+1], res, consonents, len(set(vowels)))
        
            
        # return res
