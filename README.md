# SudokuSolver
This is a small application which solves a given sudoku using the backtracking method.
It has a very simple user interface made with tkinter.

## Usage
The input - the sudoku puzzle to solve - comes from a file which the user has to provide. The file needs to have the following format:

003020600  
900305001  
001806400  
008102900  
700000008  
006708200  
002609500  
800203009  
005010300  

Whereas the zeros are interpreted as empty fields, which need to be filled by the application. If the input file is in a wrong format, the application will display a warning.
