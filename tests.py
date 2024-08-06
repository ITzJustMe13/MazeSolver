import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_zero_cols(self):
        num_cols = 0
        num_rows = 5
        with self.assertRaises(ValueError):
            Maze(0, 0, num_rows, num_cols, 10, 10)
    
    def test_maze_zero_rows(self):
        num_cols = 5
        num_rows = 0
        with self.assertRaises(ValueError):
            Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_negative_cols(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, -1, 10, 10, 10)

    def test_maze_negative_rows(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, -1, 10, 10)

    def test_maze_negative_cell_size_x(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 10, -10, 10)

    def test_maze_negative_cell_size_y(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 10, 10, -10)
    
    def test_maze_both_negative_cell_size(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 10, -10, -10)
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        

if __name__ == "__main__":
    unittest.main()