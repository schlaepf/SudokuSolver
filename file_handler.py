from exceptions.illegal_format_exception import IllegalFormatException


class SudokuFilehandler:

    NUMBER_OF_LINES = 9
    NUMBER_OF_ROWS = 9

    def __init__(self, controller):
        self.controller = controller
        print('init filehandler')

    # opens a file, reads it and converts it to a sudoku grid (9-by-9 two dimensional array)
    # if the file is in a wrong format, it raises an exception
    def convert_file_to_grid(self, filename):
        file = open(filename, 'r').read().splitlines()
        grid = []
        line_nr = 0
        if len(file) == 9:
            for line in file:
                grid.append([])
                if len(line) == 9:
                    for number in line:
                        grid[line_nr].append(int(number))
                    print(grid[line_nr])
                    line_nr += 1
                else:
                    raise IllegalFormatException
        else:
            raise IllegalFormatException
        return grid
