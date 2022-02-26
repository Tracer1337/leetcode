class ListNode:
    @staticmethod
    def from_list(l):
        if len(l) == 0: return None
        head = ListNode(l[0])
        current = head
        for _, n in enumerate(l[1:]):
            current.next = ListNode(n)
            current = current.next
        return head

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next != None:
            return f"{self.val},{self.next}"
        return str(self.val)

def solve(head):
    if head == None: return None
    current, val, prev = head, head.val, None
    while current != None:
        if current.val == val and prev != None:
            prev.next = current.next
        else:
            prev = current
            val = current.val
        current = current.next
    return head

if __name__ == "__main__":
    print(solve(ListNode.from_list([1, 1, 2])))
    print(solve(ListNode.from_list([1, 1, 2, 3, 3])))
    print(solve(ListNode.from_list([1, 1, 1])))
