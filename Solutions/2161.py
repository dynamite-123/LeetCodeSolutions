class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]: # type: ignore
        l1, l2, count = [], [], 0

        for num in nums:
            if num < pivot:
                l1.append(num)
            elif num > pivot:
                l2.append(num)
            else:
                count += 1

        return l1 + [pivot] * count + l2