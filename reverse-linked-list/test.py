from typing import Optional

from solution import ListNode, reverseList


class TestExample:
    def convert_to_linked(self, lst: list) -> Optional[ListNode]:
        if not lst:
            return None

        start = ListNode(lst[0])
        end = start
        for el in lst[1:]:
            new_node = ListNode(el)
            end.next = new_node
            end = new_node
        return start

    def convert_to_array(self, start_node: Optional[ListNode]):
        if not start_node:
            return []

        array = []
        while start_node:
            array.append(start_node.val)
            start_node = start_node.next
        return array

    def print_linked(self, start_node: Optional[ListNode]):
        if not start_node:
            print("Empty list")

        while start_node:
            print(start_node.val, end="-")
            start_node = start_node.next
        print()

    def test_1(self):
        array = [1, 2, 3, 4, 5]
        linked = self.convert_to_linked(array)
        print()
        self.print_linked(linked)
        result = reverseList(linked)
        self.print_linked(result)
