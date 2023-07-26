import tkinter as tk
from Player import Player
import random

class Board():
    def __init__(self, dim):
        self.dim = dim
        self.cells = self.generate_empty_grid()
        self.compressed = False
        self.merged = False
        self.moved = False
        self.current_score = 0
    
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
    
    