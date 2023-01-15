from solution import isValid


class TestExample:
    def test_1(self):
        assert isValid("()") is True

    def test_2(self):
        assert isValid("()[]{}") is True

    def test_3(self):
        assert isValid("(]") is False
