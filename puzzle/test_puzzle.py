from unittest import TestCase

import puzzle


class TestBimaruPuzzle(TestCase):
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
        result = puzzle.BimaruPuzzle.get_clean_grid(puzzle_grid)
        self.assertEqual(result, result_grid)
