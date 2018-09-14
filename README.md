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

After the startup of the program it looks like this:

![start](https://user-images.githubusercontent.com/18100041/45557340-a96fea80-b83d-11e8-9606-8d909dc5dd37.PNG)

After the input file is loaded the sudoku can be solved:

![after_file](https://user-images.githubusercontent.com/18100041/45557338-a96fea80-b83d-11e8-9dc1-b7578e3befd1.PNG)

Then - depending on wheter the sudoku can be solved - the solved puzzle is displayed:

![solved](https://user-images.githubusercontent.com/18100041/45557339-a96fea80-b83d-11e8-8770-4a05738ed337.PNG)


## Testing
The solver was tested with some sample inputs, which can be found in the folder *test_input_files*.
Most of the test cases can be found here:
- [invalid test cases](http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html)
- [valid test cases](http://sudopedia.enjoysudoku.com/Valid_Test_Cases.html)
