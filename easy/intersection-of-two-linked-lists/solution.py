from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_len(head: ListNode) -> int:
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def get_nth_node(head: ListNode, n: int) -> ListNode:
    while n:
        n -= 1
        head = head.next
    return head


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    length_a = linked_list_len(headA)
    length_b = linked_list_len(headB)
    longest = max(length_a, length_b)
    shortest = min(length_a, length_b)
    if length_a != length_b:
        diff = longest - shortest
        if longest == length_a:
            headA = get_nth_node(headA, diff)
        else:
            headB = get_nth_node(headB, diff)

    for _ in range(shortest):
        if headA == headB:
            return headA
        headB = headB.next
        headA = headA.next
    return None
