from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not head: return None

        new_head = ListNode(head.val) # type: ignore
        cur = head.next
        new_cur = new_head

        while cur:
            if cur.val != new_cur.val:
                new_cur.next = ListNode(cur.val) # type: ignore
                new_cur = new_cur.next
            cur = cur.next

        return new_head