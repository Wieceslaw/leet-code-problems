from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    def func(node: ListNode, start: Optional[ListNode]) -> Optional[ListNode]:
        if not start:
            return node
        temp = start.next
        start.next = node
        return func(start, temp)
    temp = head.next
    head.next = None
    result = func(head, temp)
    return result
