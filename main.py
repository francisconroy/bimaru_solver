from puzzle.puzzle import BimaruPuzzle

puzzle_grid = """EEEEEE
                EEEEEU
                EEEEEE
                EEEEEE
                EEEEEE
                EEEEWE
                """
sample_puzzle_a = BimaruPuzzle(puzzle_grid,
    [3,1,3,3,1,3],
    [2,3,1,3,0,5],
    [4,3,2,2,1,1,1]
)