import tkinter as tk
from Player import Player
import random

class Board(tk.TK):
    def __init__(self, dim):
        super.__init__()
        self.dim = dim
        self.cells = self.generate_empty_grid()
        self.compressed = False
        self.merged = False
        self.moved = False
        self.current_score = 0
        self.title('2048')
        self.resizable(False, False)
        self.background = tk.Frame(self, bg=tk.GamePanel.BACKGROUND_COLOR)
        self.cell_labels = []
        for i in range(self.grid.size):
            row_labels = []
            for j in range(self.grid.size):
                label = tk.Label(self.background, text='',
                                 bg=tk.GamePanel.EMPTY_CELL_COLOR,
                                 justify=tk.CENTER, font=tk.GamePanel.FONT,
                                 width=4, height=2)
                label.grid(row=i, column=j, padx=10, pady=10)
                row_labels.append(label)
            self.cell_labels.append(row_labels)
        self.background.pack(side=tk.TOP)
    
    def draw(self):
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                if self.grid.cells[i][j] == 0:
                    self.cell_labels[i][j].configure(
                         text='',
                         bg=tk.GamePanel.EMPTY_CELL_COLOR)
                else:
                    cell_text = str(self.grid.cells[i][j])
                    if self.grid.cells[i][j] > 2048:
                        bg_color = tk.GamePanel.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = tk.GamePanel.CELL_COLOR_DICT.get('beyond')
                    else:
                        bg_color = tk.GamePanel.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = tk.GamePanel.CELL_COLOR_DICT.get(cell_text)
                    self.cell_labels[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)

    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.grid.random_cell()
    
    def start(self):
        self.add_start_cells()
        self.draw()
        self.bind('<Key>', self.key_handler)
        self.panel.root.mainloop()
    
    def retrieve_empty_cells(self):
        ret = []
        for i in range(self.dim):
            for j in range(self.dim):
                if self.cells[i][j] == 0:
                    ret.append((i, j))
        return ret
    
    def generate_random_cell(self):
        cell = random.choice(self.retrieve_empty_cells())
        i = cell[0]
        j = cell[1]
        self.cells[i][j] = 2 if random.random() < 0.9 else 4

    def generate_empty_grid(self):
        [[0] * self.size for i in range(self.dim)]

    def transpose(self):
        '''
        This function is used to swap the rows and columns. 
        With this in addition to the reverse function, we will
        simplify the code. If we wish to move up we will only 
        need to transpose the grid and apply the merges, but if 
        we want to move down, we need to apply the transpose and 
        reverse the grid.
        '''
        self.cells = [list(t) for t in zip(*self.cells)]

    def reverse(self):
        '''
        This is used to reverse the order of the cells in each row.
        With this in addition to the transpose function, we will be able to implement the movement functions.
        '''
        for i in range(self.size):
            start = 0
            end = self.size - 1
            while start < end:
                self.cells[i][start], self.cells[i][end] = \
                    self.cells[i][end], self.cells[i][start]
                start += 1
                end -= 1
    
    def compress(self):
        self.compressed = False
        new_grid = self.generate_empty_grid()
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.cells[i][j] != 0:
                    new_grid[i][count] = self.cells[i][j]
                    if count != j:
                        self.compressed = True
                    count += 1
        self.cells = new_grid
        
    def merge(self):
        self.merged = False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.cells[i][j] == self.cells[i][j + 1] and self.cells[i][j] != 0:
                    self.cells[i][j] *= 2
                    self.cells[i][j + 1] = 0
                    self.current_score += self.cells[i][j]
                    self.merged = True
    
    