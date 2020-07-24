
import unittest  


from combinatoria import Combinatoria


class TestMyCombinatoria(unittest.TestCase):  

    def setUp(self):
        self.comb = Combinatoria()

    def test_combinatoria(self):
        self.comb.combi(-3,5)
        self.assertEqual("error", self.comb.ans)

        self.comb.combi(5,-3)
        self.assertEqual("error", self.comb.ans)
        
        self.comb.combi(-2,3)
        self.assertEqual("error", self.comb.ans)

        self.comb.combi(3,0)
        self.assertEqual(1, self.comb.ans)

        self.comb.combi(4,1)
        self.assertEqual(4, self.comb.ans)

        self.comb.combi(5,2)
        self.assertEqual(10, self.comb.ans)

        self.comb.combi(3,3)
        self.assertEqual(1, self.comb.ans)

        self.comb.combi("4",5)
        self.assertEqual("error", self.comb.ans)

        self.comb.combi(1,1)
        self.assertEqual(1, self.comb.ans)


if __name__ == '__main__':
    unittest.main()