from solution import mySqrt


class TestExample:
    def test_1(self):
        assert mySqrt(4) == 2

    def test_2(self):
        assert mySqrt(8) == 2

    def test_3(self):
        assert mySqrt(5) == 2

    def test_4(self):
        assert mySqrt(1) == 1

    def test_5(self):
        assert mySqrt(0) == 0

    def test_6(self):
        assert mySqrt(2) == 1

    def test_7(self):
        assert mySqrt(12) == 3
