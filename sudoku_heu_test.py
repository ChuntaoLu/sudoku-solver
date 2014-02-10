import unittest
import sudoku_heu


class sudoku_heuTest(unittest.TestCase):
    B = False
    #no solution
    BD1 = [1, 2, 3, 4, 5, 6, 7, 8, B,
           B, B, B, B, B, B, B, B, 2,
           B, B, B, B, B, B, B, B, 3,
           B, B, B, B, B, B, B, B, 4,
           B, B, B, B, B, B, B, B, 5,
           B, B, B, B, B, B, B, B, 6,
           B, B, B, B, B, B, B, B, 7,
           B, B, B, B, B, B, B, B, 8,
           B, B, B, B, B, B, B, B, 9]
    #easy
    BD2 = [2, 7, 4, B, 9, 1, B, B, 5,
           1, B, B, 5, B, B, B, 9, B,
           6, B, B, B, B, 3, 2, 8, B,
           B, B, 1, 9, B, B, B, B, 8,
           B, B, 5, 1, B, B, 6, B, B,
           7, B, B, B, 8, B, B, B, 3,
           4, B, 2, B, B, B, B, B, 9,
           B, B, B, B, B, B, B, 7, B,
           8, B, B, 3, 4, 9, B, B, B]
    #hard
    BD3 = [5, B, B, B, B, 4, B, 7, B,
           B, 1, B, B, 5, B, 6, B, B,
           B, B, 4, 9, B, B, B, B, B,
           B, 9, B, B, B, 7, 5, B, B,
           1, 8, B, 2, B, B, B, B, B,
           B, B, B, B, B, 6, B, B, B,
           B, B, 3, B, B, B, B, B, 8,
           B, 6, B, B, 8, B, B, B, 9,
           B, B, 8, B, 7, B, B, 3, 1]
    #very hard
    BD4 = [B, B, 5, 3, B, B, B, B, B,
           8, B, B, B, B, B, B, 2, B,
           B, 7, B, B, 1, B, 5, B, B,
           4, B, B, B, B, 5, 3, B, B,
           B, 1, B, B, 7, B, B, B, 6,
           B, B, 3, 2, B, B, B, 8, B,
           B, 6, B, 5, B, B, B, B, 9,
           B, B, 4, B, B, B, B, 3, B,
           B, B, B, B, B, 9, 7, B, B]
    #BD2 solution
    BD2S = [2, 7, 4, 8, 9, 1, 3, 6, 5,
            1, 3, 8, 5, 2, 6, 4, 9, 7,
            6, 5, 9, 4, 7, 3, 2, 8, 1,
            3, 2, 1, 9, 6, 4, 7, 5, 8,
            9, 8, 5, 1, 3, 7, 6, 4, 2,
            7, 4, 6, 2, 8, 5, 9, 1, 3,
            4, 6, 2, 7, 5, 8, 1, 3, 9,
            5, 9, 3, 6, 1, 2, 8, 7, 4,
            8, 1, 7, 3, 4, 9, 5, 2, 6]
    #BD3 solution
    BD3S = [5, 3, 9, 1, 6, 4, 8, 7, 2,
            8, 1, 2, 7, 5, 3, 6, 9, 4,
            6, 7, 4, 9, 2, 8, 3, 1, 5,
            2, 9, 6, 4, 1, 7, 5, 8, 3,
            1, 8, 7, 2, 3, 5, 9, 4, 6,
            3, 4, 5, 8, 9, 6, 1, 2, 7,
            9, 2, 3, 5, 4, 1, 7, 6, 8,
            7, 6, 1, 3, 8, 2, 4, 5, 9,
            4, 5, 8, 6, 7, 9, 2, 3, 1]
    #BD4 solution
    BD4S = [1, 4, 5, 3, 2, 7, 6, 9, 8,
            8, 3, 9, 6, 5, 4, 1, 2, 7,
            6, 7, 2, 9, 1, 8, 5, 4, 3,
            4, 9, 6, 1, 8, 5, 3, 7, 2,
            2, 1, 8, 4, 7, 3, 9, 5, 6,
            7, 5, 3, 2, 9, 6, 4, 8, 1,
            3, 6, 7, 5, 4, 2, 8, 1, 9,
            9, 8, 4, 7, 6, 1, 2, 3, 5,
            5, 2, 1, 8, 3, 9, 7, 6, 4]

    def test_solve(self):
        self.assertFalse(sudoku_heu.solve(self.BD1))
        self.assertEqual(sudoku_heu.solve(self.BD2), self.BD2S)
        self.assertEqual(sudoku_heu.solve(self.BD3), self.BD3S)
        self.assertEqual(sudoku_heu.solve(self.BD4), self.BD4S)

    def test_is_solved(self):
        self.assertTrue(sudoku_heu.is_solved(self.BD2S))
        self.assertFalse(sudoku_heu.is_solved(self.BD2))

    def test_valid_fills(self):
        self.assertEqual(sudoku_heu.valid_fills(self.BD2, 3), set([6, 8]))

    ##Randomization makes it hard to test?
    #def test_fill_board(self):
    #    bd = self.BD2[:]
    #    bd[6] = 3
    #    self.assertEqual(sudoku_heu.fill_board(self.BD2), [bd])


if __name__ == "__main__":
    unittest.main()
