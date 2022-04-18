from unittest import TestCase

from puzzle.puzzle import BimaruPuzzle


class TestBimaruPuzzle(TestCase):
    def setUp(self) -> None:
        puzzle_grid = """EEEEEE
                        EEEEEU
                        EEEEEE
                        EEEEEE
                        EEEEEE
                        EEEEWE
                        """
        self.testpuzzle = BimaruPuzzle(puzzle_grid,
                                       [3, 1, 3, 3, 1, 3],
                                       [2, 3, 1, 3, 0, 5],
                                       [4, 3, 2, 2, 1, 1, 1]
                                       )

    def test_get_clean_grid(self):
        puzzle_grid = """EEEEEE
                        EEEEEU
                        EEEEEE
                        EEEEEE
                        EEEEEE
                        EEEEWE
                        """

        result_grid = [['E', 'E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'E', 'U'],
                       ['E', 'E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'W', 'E']]
        result = BimaruPuzzle.get_clean_grid(puzzle_grid)
        self.assertEqual(result, result_grid)

    def test_check_row_col_counts(self):
        # This is the solved sample puzzle
        puzzle_grid = """   OWWWWU
                            WWLRWD
                            OWWWWW
                            WWL-RW
                            WWWWWW
                            L--RWO
                            """

    def test_surrounding_ship_bits(self):
        puzzle_grid = """   OEEEED
                            EELREU
                            OEEEEE
                            EEL-RE
                            EEEEEE
                            L--REO
                        """
        self.testpuzzle = BimaruPuzzle(puzzle_grid,
                                       [3, 1, 3, 3, 1, 3],
                                       [2, 3, 1, 3, 0, 5],
                                       [4, 3, 2, 2, 1, 1, 1]
                                       )

class TestFixShipBitOrientations(TestCase):
    def setUp(self) -> None:
        puzzle_grid = """EEEEEE
                        EEEEEU
                        EEEEEE
                        EEEEEE
                        EEEEEE
                        EEEEWE
                        """
        self.testpuzzle = BimaruPuzzle(puzzle_grid,
                                       [3, 1, 3, 3, 1, 3],
                                       [2, 3, 1, 3, 0, 5],
                                       [4, 3, 2, 2, 1, 1, 1]
                                       )