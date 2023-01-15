from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    cur = head.val
    start = head
    end = head

    while head:
        if head.val != cur:
            cur = head.val
            end.next = head
            end = head
        head = head.next
    end.next = None
    return start
