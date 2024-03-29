# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = head
        runner = head
        while runner is not None and runner.next is not None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: return True
        return False
