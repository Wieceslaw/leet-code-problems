from solution import ListNode, deleteDuplicates


class TestExample:
    def append_node(self, end: ListNode, val: ListNode):
        node = ListNode(val)
        end.next = node
        return node

    def convert_to_linked(self, array):
        if not array:
            return None
        start = ListNode(array[0])
        end = start

        for el in array[1:]:
            end = self.append_node(end, el)
        return start

    def convert_to_array(self, start: ListNode):
        if not start:
            return []

        array = []
        while start:
            array.append(start.val)
            start = start.next
        return array

    def print_linked(self, start):
        while start:
            print(start.val, end=" ")
            start = start.next
        print()

    def base_test(self, _input, _output):
        linked_input = self.convert_to_linked(_input)
        linked_output = deleteDuplicates(linked_input)
        array_output = self.convert_to_array(linked_output)

        assert len(array_output) == len(_output)
        for i in range(len(_output)):
            assert array_output[i] == _output[i]

    def test_1(self):
        _input = [1, 1, 2]
        _output = [1, 2]

        self.base_test(_input, _output)

    def test_2(self):
        _input = [1, 1, 2, 3, 3]
        _output = [1, 2, 3]

        self.base_test(_input, _output)
