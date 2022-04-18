from copy import deepcopy

EMPTY_CELL = "E"
WATER_CELL = "W"

SHIP_BITS = ["U",  # Up ship end
             "D",  # Down ship end
             "L",  # Left ship end
             "R",  # Right ship end
             "C",  # center ship
             "O",  # Baby ship 1U
             "-",  # left-right ship mid section
             "|"]  # up-down ship mid section

WATERING_PATTERNS = {
    "U":
        """
        WXW
        WUW
        WWW
        """,
    "D":
        """
        WWW
        WDW
        WXW
        """,
    "L":
        """
        WWW
        WLX
        WWW
        """,
    "R":
        """
        WWW
        XRW
        WWW
        """,
    "C":
        """
        WXW
        XCX
        WXW
        """
}


class BimaruPuzzle:
    def __init__(self, ascii_grid, counts_per_col, counts_per_row, ships_to_place):
        """

        :param ascii_grid: E=empty, U=ship up, L=ship left, R=ship right, D=ship down, C=ship centre, W=water
        :param counts_per_col:
        :param counts_per_row:
        :param ships_to_place:
        """
        self.grid = ascii_grid
        self.linegrid = None
        self.counts_per_col = counts_per_col
        self.counts_per_row = counts_per_row
        self.ships_to_place = ships_to_place
        self.clean_grid()
        self.add_autowater()
        pass

    def solve(self):
        self.add_autowater()
        self.surround_ship_bits()

    def get_grid_dims(self):
        return len(self.linegrid),len(self.linegrid[0])

    def clean_grid(self):
        if self.linegrid is None:
            self.linegrid = self.get_clean_grid(self.grid)

    @staticmethod
    def get_clean_grid(stringgrid):
        gridlines = stringgrid.splitlines(False)
        temp_linegrid = []
        for line in gridlines:
            line = line.strip()
            if line:
                temp_linegrid.append(list(line))
        return temp_linegrid

    def add_autowater(self):
        for row_idx, row in enumerate(self.linegrid):
            for col_idx, cell in enumerate(row):
                if not self.counts_per_row[row_idx] or not self.counts_per_col[col_idx]:
                    self.linegrid[row_idx][col_idx] = "W"

    def _superimpose_grids(self, grid_pattern, centre_row, centre_column):
        # Iterate over the old_grid and modify entries
        new_grid = deepcopy(self.linegrid)
        # Check the center coords are in the grid
        row_healthy = centre_row < len(new_grid)
        col_healthy = centre_column < len(new_grid[0])
        if False in [row_healthy, col_healthy]:
            print("Something is wrong here")
            return

        # Checking the dimensions on the pattern should be 3x3
        patt = self.get_clean_grid(grid_pattern)
        dims_healthy = len(patt) == 3 and len(patt[0]) == 3
        if not dims_healthy:
            print("Provided grid is inadequate")
            return

        grid_row_count, grid_col_count = self.get_grid_dims()
        top_row = min(centre_row - 1, grid_row_count-1)
        bottom_row = max(centre_row + 1, 0)
        right_col = min(centre_column + 1, grid_col_count-1)
        left_col = max(centre_column - 1, 0)

        for row_idx in range(top_row, bottom_row+1):
            for col_idx in range(left_col, right_col+1):
                subgrid_row = row_idx - centre_row + 1
                subgrid_col = col_idx - centre_column + 1
                subcell = patt[subgrid_row][subgrid_col]
                if subcell == "W":
                    new_grid[row_idx][col_idx] = subcell  # update cell
        self.linegrid = new_grid

    def surround_ship_bits(self):
        """
        Populates the ship surrounds with water
        :return:
        """
        # Search for ship bits
        for row_idx, row in enumerate(self.linegrid):
            for col_idx, cell in enumerate(row):
                if cell in SHIP_BITS:
                    # Got a bit o ship
                    self._superimpose_grids(WATERING_PATTERNS[cell], row_idx, col_idx)

    def __str__(self):
        if self.linegrid:
            stringgrid = "\n".join(["".join(row) for row in self.linegrid])
            return stringgrid



if __name__ == "__main__":
    puzzle_grid = """EEEEEE
                    EEEEEU
                    EEEEEE
                    EEEEEE
                    EEEEEE
                    EEEEWE
                    """
    sample_puzzle_a = BimaruPuzzle(puzzle_grid,
                                   [3, 1, 3, 3, 1, 3],
                                   [2, 3, 1, 3, 0, 5],
                                   [4, 3, 2, 2, 1, 1, 1]
                                   )
    sample_puzzle_a.solve()
    print(sample_puzzle_a)
