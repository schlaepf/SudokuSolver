from unittest import TestCase
from sudoku_solver import SudokuSolver
from controller import SudokuController
from unittest.mock import MagicMock


class TestSudokuSolver(TestCase):
    solvable_sudoku = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
                       [9, 0, 0, 3, 0, 5, 0, 0, 1],
                       [0, 0, 1, 8, 0, 6, 4, 0, 0],
                       [0, 0, 8, 1, 0, 2, 9, 0, 0],
                       [7, 0, 0, 0, 0, 0, 0, 0, 8],
                       [0, 0, 6, 7, 0, 8, 2, 0, 0],
                       [0, 0, 2, 6, 0, 9, 5, 0, 0],
                       [8, 0, 0, 2, 0, 3, 0, 0, 9],
                       [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    solved_sudoku = [[4, 8, 3, 9, 2, 1, 6, 5, 7],
                     [9, 6, 7, 3, 4, 5, 8, 2, 1],
                     [2, 5, 1, 8, 7, 6, 4, 9, 3],
                     [5, 4, 8, 1, 3, 2, 9, 7, 6],
                     [7, 2, 9, 5, 6, 4, 1, 3, 8],
                     [1, 3, 6, 7, 9, 8, 2, 4, 5],
                     [3, 7, 2, 6, 8, 9, 5, 1, 4],
                     [8, 1, 4, 2, 5, 3, 7, 6, 9],
                     [6, 9, 5, 4, 1, 7, 3, 8, 2]]

    invalid_sudoku = [[9, 0, 3, 0, 2, 0, 6, 0, 0],
                      [9, 0, 0, 3, 0, 5, 0, 0, 1],
                      [0, 0, 1, 8, 0, 6, 4, 0, 0],
                      [0, 0, 8, 1, 0, 2, 9, 0, 0],
                      [7, 0, 0, 0, 0, 0, 0, 0, 8],
                      [0, 0, 6, 7, 0, 8, 2, 0, 0],
                      [0, 0, 2, 6, 0, 9, 5, 0, 0],
                      [8, 0, 0, 2, 0, 3, 0, 0, 9],
                      [0, 0, 5, 0, 1, 0, 3, 0, 0]]

    unsolvable_sudoku = [[9, 0, 0, 1, 0, 0, 0, 0, 4],
                         [0, 1, 4, 0, 3, 0, 8, 0, 0],
                         [0, 0, 3, 0, 0, 0, 0, 9, 0],
                         [0, 0, 0, 7, 0, 8, 0, 0, 1],
                         [8, 0, 0, 0, 0, 3, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 3, 0],
                         [0, 2, 1, 0, 0, 0, 0, 7, 0],
                         [0, 0, 9, 0, 4, 0, 5, 0, 0],
                         [5, 0, 0, 0, 1, 6, 0, 0, 3]]

    def test_search_solution_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.search_solution(self.solvable_sudoku, (0, 0)))

    def test_search_solution_false(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.search_solution(self.unsolvable_sudoku, (0, 0)))

    def test_is_sudoku_filled_false(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.is_sudoku_filled(self.solvable_sudoku))

    def test_is_sudoku_filled_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.is_sudoku_filled(self.solved_sudoku))

    def test_get_next_square(self):
        solver = self.get_solver_object()
        self.assertEquals(solver.get_next_square((0, 8)), (1, 0))

    def test_is_number_allowed_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.is_number_allowed(self.solvable_sudoku, 5, (0, 0)))

    def test_is_number_allowed_false(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.is_number_allowed(self.solvable_sudoku, 1, (0, 0)))

    def test_number_in_row_allowed_true(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.number_in_row_allowed(self.solvable_sudoku, 6, 0))

    def test_number_in_row_allowed_false(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.number_in_row_allowed(self.solvable_sudoku, 1, 0))

    def test_number_in_column_allowed_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.number_in_column_allowed(self.solvable_sudoku, 1, 0))

    def test_number_in_column_allowed_false(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.number_in_column_allowed(self.solvable_sudoku, 9, 0))

    def test_number_in_block_allowed_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.number_in_block_allowed(self.solvable_sudoku, 5, (0, 0)))

    def test_number_in_block_allowed_false(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.number_in_block_allowed(self.solvable_sudoku, 9, (0, 0)))

    def test_is_input_valid_true(self):
        solver = self.get_solver_object()
        self.assertTrue(solver.is_input_valid(self.solvable_sudoku))

    def test_is_input_valid_true(self):
        solver = self.get_solver_object()
        self.assertFalse(solver.is_input_valid(self.invalid_sudoku))

    @staticmethod
    def get_solver_object():
        return SudokuSolver(MagicMock())
