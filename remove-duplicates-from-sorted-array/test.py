from solution import removeDuplicates


class TestExample:
    def test_1(self):
        _input = [1, 1, 2]
        _output = [1, 2, 0]
        k = 2

        assert removeDuplicates(_input) == k

        for i in range(k):
            assert _input[i] == _output[i]

    def test_2(self):
        _input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        _output = [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
        k = 5

        assert removeDuplicates(_input) == k

        for i in range(k):
            assert _input[i] == _output[i]
