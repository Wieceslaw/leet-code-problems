from solution import plusOne


class TestExample:
    def test_1(self):
        digits = [1, 2, 3]
        result = [1, 2, 4]

        assert plusOne(digits) == result

    def test_2(self):
        digits = [4, 3, 2, 1]
        result = [4, 3, 2, 2]

        assert plusOne(digits) == result

    def test_3(self):
        digits = [9]
        result = [1, 0]

        assert plusOne(digits) == result
