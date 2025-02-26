# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # type: ignore
        if not lists:
            return None

        heap = []

        for l in lists:
            if not l:
                continue
            cur = l
            while cur:
                heapq.heappush(heap, cur.val) # type: ignore
                cur = cur.next
                
        if not heap: return None

        res = ListNode(heappop(heap)) # type: ignore

        prev = res
        for i in range(len(heap)):
            cur = ListNode(heappop(heap)) # type: ignore
            prev.next = cur
            prev = prev.next
        
        return res