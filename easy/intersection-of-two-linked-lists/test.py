from typing import Optional

from solution import ListNode, getIntersectionNode


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
            print(start_node.val, end=" ")
            start_node = start_node.next
        print()

    def test_1(self):
        list_a = []
        list_b = [1, 5]
        linked_a = self.convert_to_linked(list_a)
        linked_b = self.convert_to_linked(list_b)
        print()
        self.print_linked(linked_a)
        self.print_linked(linked_b)
        result = getIntersectionNode(linked_a, linked_b)
        self.print_linked(result)
