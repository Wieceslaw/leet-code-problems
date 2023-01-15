from solution import lengthOfLastWord


class TestExample:
    def test_1(self):
        s = "Hello World"
        assert lengthOfLastWord(s) == 5

    def test_2(self):
        s = "   fly me   to   the moon  "
        assert lengthOfLastWord(s) == 4

    def test_3(self):
        s = "luffy is still joyboy"
        assert lengthOfLastWord(s) == 6

    def test_4(self):
        s = "Today is a nice day"
        assert lengthOfLastWord(s) == 3
