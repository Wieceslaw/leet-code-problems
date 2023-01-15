from solution import removeElement


class TestExample:
    def test_1(self):
        _input = [3, 2, 2, 3]
        val = 3

        _output = [2, 2, 0, 0]
        k = 2

        assert k == removeElement(_input, val)

        for i in range(k):
            assert _input[i] == _output[i]
