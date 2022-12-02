# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1: Iterative

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    prevNode, currentNode = None, head
    while currentNode:
      if currentNode.val == val:
        if prevNode:
          prevNode.next = currentNode.next
        else:
          head = currentNode.next
        currentNode = currentNode.next
        continue
      prevNode = currentNode
      currentNode = currentNode.next
    return head

# Solution 2: Recursive

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      if head == None:
        return None
      head.next = self.removeElements(head.next, val)
      return head.next if head.val == val else head
