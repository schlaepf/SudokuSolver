
class SudokuSolver:

    # TODO eventually do the work in a background thread
    def __init__(self, controller):
        self.controller = controller
        print('init solver')

    def search_solution(self, grid, position):
        row = position[0]
        column = position[1]
        if self.is_sudoku_filled(grid):
            return True

        if grid[row][column] != 0 and row < 9 and column < 9:
            # square already filled
            if self.search_solution(grid, self.get_next_square(position)):
                return True
        else:
            for n in range(1, 10):
                if self.is_number_allowed(grid, n, position):
                    grid[row][column] = n
                    if self.search_solution(grid, self.get_next_square(position)):
                        return True
            grid[row][column] = 0

        return False

    def is_sudoku_filled(self, grid):
        for i in grid:
            if 0 in i:
                return False
        return True

    def get_next_square(self, position):
        row = position[0]
        column = position[1]
        if column == 8:
            new_position = (row + 1, 0)
        else:
            new_position = (row, column + 1)
        return new_position

    # number: will be put into the square, if the rules are met
    # position: a tuple, first the row, then the column
    def is_number_allowed(self, grid, number, position):
        row = position[0]
        column = position[1]
        return self.number_in_row_allowed(grid, number, row) and self.number_in_column_allowed(grid, number, column) \
               and self.number_in_block_allowed(grid, number, position)

    def number_in_row_allowed(self, grid, number, row_nr):
        return number not in grid[row_nr]

    def number_in_column_allowed(self, grid, number, column_nr):
        column = []
        for i in range(0, 9):
            column.append(grid[i][column_nr])
        return number not in column

    def number_in_block_allowed(self, grid, number, position):
        row = position[0]
        column = position[1]

        # determine the upper left square of the block
        ul_row = row - (row % 3)
        ul_column = column - (column % 3)

        # iterate through block to check if number is already in it
        for i in range(ul_row, ul_row + 3):
            if number in grid[i][ul_column:ul_column + 3]:
                return False

        return True

    # starts the solver if the given input is valid
    def main(self, grid):
        self.controller.update_gui_grid(grid)
        if self.is_input_valid(grid):
            if self.search_solution(grid, (0, 0)):
                self.print_field(grid)
                self.controller.update_gui_grid(grid)
            else:
                self.controller.update_gui_grid(None)
                print('no solution found')
        else:
            self.controller.show_message_on_gui('Invalid', 'Input is invalid')

    # checks, if a given sudoku is valid
    def is_input_valid(self, grid):
        if not grid:
            return False

        input_valid = True
        for row in range(0, 9):
            for column in range(0, 9):
                number = grid[row][column]
                if number:
                    grid[row][column] = 0
                    if not self.is_number_allowed(grid, number, (row, column)):
                        return False
                    grid[row][column] = number
        return input_valid

    # helper method to print the sudoku grid in the console
    def print_field(self, grid):
        for line in grid:
            for square in line:
                print(square, end='')
                print(' |', end='')
            print()
            print('----------------------------')
        print()
