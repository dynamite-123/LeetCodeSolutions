class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]: # type: ignore
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            elif nums2[j][0] < nums1[i][0]:
                result.append(nums2[j])
                j += 1
            else:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i, j = i + 1, j + 1
        
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        return result


# BRUTE SOLUTION
        # hm = defaultdict(int)
        # for num in nums1:
        #     hm[num[0]] += num[1]

        # for num in nums2:
        #     hm[num[0]] += num[1]

        # res = list(hm.items())
        # res.sort()
        # return res