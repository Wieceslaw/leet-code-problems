from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    array = []
    while head:
        array.append(head.val)
        head = head.next
    length = len(array)
    for i in range(length // 2):
        if array[i] != array[length - i - 1]:
            return False
    return True
