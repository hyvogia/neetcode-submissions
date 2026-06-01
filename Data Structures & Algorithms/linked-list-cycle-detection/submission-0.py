# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hsst = set()
        current = head
        while current:
            if current in hsst:
                return True
            hsst.add(current)
            current = current.next
        return False
        