from solution import addBinary


class TestExample:
    def test_1(self):
        a = '11'
        b = '1'
        result = '100'

        assert addBinary(a, b) == result

    def test_2(self):
        a = '1010'
        b = '1011'
        result = '10101'

        assert addBinary(a, b) == result
