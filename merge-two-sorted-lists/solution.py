from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def min_node(first, second):
    if None == first:
        return second
    if None == second:
        return first
    if None == second and None == first:
        return None
    if second.val <= first.val:
        return second
    return first


def append_node(list_end: ListNode, node: ListNode):
    list_end.next = node
    return node


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pointer1 = list1
    pointer2 = list2

    start = min_node(pointer1, pointer2)
    if start is None:
        return None

    end = start

    if start == pointer1:
        pointer1 = pointer1.next
    if start == pointer2:
        pointer2 = pointer2.next

    while pointer1 or pointer2:
        node = min_node(pointer1, pointer2)
        if node == pointer1:
            pointer1 = pointer1.next
        if node == pointer2:
            pointer2 = pointer2.next
        end = append_node(end, node)

    return start
