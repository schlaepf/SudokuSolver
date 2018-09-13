from controller import SudokuController


class SudokuMain:

    def __init__(self):
        print('init main')

    # Starts the program by initiating the controller
    def run(self):
        print('run')
        controller = SudokuController()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    m = SudokuMain()
    m.run()
