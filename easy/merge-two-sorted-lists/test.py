from typing import Optional

from solution import ListNode, mergeTwoLists


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

    def merge_to_array(self, array1: list, array2: list) -> list:
        linked1 = self.convert_to_linked(array1)
        linked2 = self.convert_to_linked(array2)
        result = mergeTwoLists(linked1, linked2)
        return self.convert_to_array(result)

    def test_1(self):
        array1 = [1, 2, 4]
        array2 = [1, 3, 4]
        result = [1, 1, 2, 3, 4, 4]

        assert self.merge_to_array(array1, array2) == result

    def test_2(self):
        array1 = []
        array2 = []
        result = []

        assert self.merge_to_array(array1, array2) == result

    def test_3(self):
        array1 = []
        array2 = [1]
        result = [1]

        assert self.merge_to_array(array1, array2) == result
