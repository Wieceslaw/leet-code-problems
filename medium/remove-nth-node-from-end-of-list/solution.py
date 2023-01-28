from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    start = head
    length = n + 1
    last_nodes = deque(maxlen=length)
    count = 0
    while head:
        if len(last_nodes) == length:
            last_nodes.popleft()
        last_nodes.append(head)
        head = head.next
        count += 1
    if count == n:
        return start.next
    k = max(count, length)
    if k == 1:
        return None
    if k == 2:
        pre_nth = last_nodes.popleft()
        pre_nth.next = None
    elif k >= 3:
        pre_nth = last_nodes.popleft()
        last_nodes.popleft()  # nth
        post_nth = last_nodes.popleft()
        pre_nth.next = post_nth
    return start
