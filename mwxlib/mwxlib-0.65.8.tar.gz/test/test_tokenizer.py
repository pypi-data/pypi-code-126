import unittest
import mwx.utilus as ut


class TestTokenizerMethods(unittest.TestCase):

    def test_split_words1(self):
        s = ' '
        c = ','
        values = (
            ("f(a * b, x, y), f (x,y)", ['f(a * b, x, y)', c, s, 'f', s, '(x,y)']),
            ("f(1,\n 2)", ['f(1,\n 2)']),
            ("1@p", ['1', '@', 'p']),
        )
        for text, result in values:
            ret = list(ut.split_words(text, reverse=0))
            print("{!r} --> {}".format(text, ret))
            self.assertEqual(ret, result)


if __name__ == "__main__":
    unittest.main()
