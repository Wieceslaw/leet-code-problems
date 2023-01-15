from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    st = set()
    while head:
        if head not in st:
            st.add(head)
        else:
            return True
        head = head.next
    return False
