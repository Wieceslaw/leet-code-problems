from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    ptr = None
    new_head = None
    while head:
        if not new_head and head.val != val:
            new_head = head
            ptr = new_head
            head = head.next
            continue
        if ptr and head.val != val:
            ptr.next = head
            ptr = head
        head = head.next
    if ptr:
        ptr.next = None
    return new_head
