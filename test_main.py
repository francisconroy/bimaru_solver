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
        self.test_puzzle = BimaruPuzzle(puzzle_grid,
                                        [3, 1, 3, 3, 1, 3],
                                        [2, 3, 1, 3, 0, 5],
                                        [4, 3, 2, 2, 1, 1, 1]
                                        )

    def test_surround_ship_bits(self):
        self.fail()
