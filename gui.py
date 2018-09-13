import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class SudokuUI(tk.Frame):
    """ This UI includes the sudoku grid as well as a button to open and read a file and a button to start the search
    for a solution to a given sudoku """

    gui_grid = []
    start_button = None
    open_file_button = None

    def __init__(self, controller):
        print('init gui')
        self.grid = []
        self.controller = controller
        self.root = tk.Tk()
        self.sudoku_grid_frame = tk.LabelFrame(master=self.root, borderwidth=2, relief="solid", height=9, width=9)
        self.sudoku_grid_frame.grid(column=0, row=0)
        self.info_label = tk.Label(self.root, bd=2, text=str(0), font=('Arial', 12))
        self.init_gui()

    # initializes the different parts of the UI
    def init_gui(self):
        self.root.title('Sudoku solver')
        self.init_gui_grid()
        self.init_start_button()
        self.init_open_file_button()
        self.init_info_label()

    def init_info_label(self):
        self.info_label.configure(text='')
        self.info_label.grid(column=0, row=12)

    # calls the mainloop, has to be done after the whole UI is being initialized
    def call_mainloop(self):
        self.root.mainloop()

    def start_btn_clicked(self):
        self.info_label.configure(text='')
        self.controller.search_solution(self.grid)

    def open_file_btn_clicked(self):
        filename = filedialog.askopenfilename(initialdir='C:\\', title='Select file',
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.controller.handle_file(filename)

    def init_gui_grid(self):
        for x in range(0, 9):
            self.gui_grid.append([])
            for y in range(0, 9):
                self.gui_grid[x].append(tk.Label(self.sudoku_grid_frame, borderwidth=1, relief="ridge", text=str(0), font=('Arial', 14), width=2, height=1))
                self.gui_grid[x][y].grid(row=x, column=y)

    def init_start_button(self):
        self.start_button = tk.Button(self.root, text='Solve', command=self.start_btn_clicked)
        self.start_button.grid(column=0, row=10)

    def init_open_file_button(self):
        self.open_file_button = tk.Button(self.root, text='Open File', command=self.open_file_btn_clicked)
        self.open_file_button.grid(column=0, row=11)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    # updates the grid of the UI with the new given grid
    def update_gui_grid(self, new_grid):
        if new_grid:
            self.grid = new_grid
            for x in range(0, 9):
                for y in range(0, 9):
                    self.gui_grid[x][y].configure(text=new_grid[x][y])
        else:
            self.info_label.configure(text='No solution found')
