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

def solve(l1, l2):
    head = tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        tail.next = ListNode(val)
        tail = tail.next
    return head.next

if __name__ == "__main__":
    print(solve(ListNode.from_list([2, 4, 3]), ListNode.from_list([5, 6, 4])))
    print(solve(ListNode.from_list([0]), ListNode.from_list([0])))
    print(solve(ListNode.from_list([9,9,9,9,9,9,9]), ListNode.from_list([9,9,9,9])))
