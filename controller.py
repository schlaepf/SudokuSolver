from gui import SudokuUI
from sudoku_solver import SudokuSolver
from file_handler import SudokuFilehandler
from exceptions.illegal_format_exception import IllegalFormatException


class SudokuController:
    """ Controller layer from logic to UI to file handler"""

    def __init__(self):
        print('init controller')
        self.solver = SudokuSolver(self)
        self.gui = SudokuUI(self)
        self.filehandler = SudokuFilehandler(self)
        self.gui.call_mainloop()

    # updates the sudoku grid on the UI
    def update_gui_grid(self, grid):
        self.gui.update_gui_grid(grid)

    # starts the search for a solution for the given grid
    def search_solution(self, grid):
        self.solver.main(grid)

    # shows a message on the UI
    def show_message_on_gui(self, title, message):
        self.gui.show_message(title, message)

    # opens a file and shows the grid it on the UI
    def handle_file(self, filename):
        try:
            grid = self.filehandler.convert_file_to_grid(filename)
            self.gui.update_gui_grid(grid)
        except (ValueError, IllegalFormatException) as e:
            self.gui.show_message('Error', 'Wrong format of input file')

