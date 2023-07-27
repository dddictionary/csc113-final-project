import tkinter as tk
from Board import Board
class Player:
    def __init__(self, board):
        self.playerName = playerName
        self.board = board
    def left(self):
        self.board.compress()
        self.board.merge()
        moved = self.board.compressed or self.board.merged
        self.board.compress()

    def right(self):
        self.board.reverse()
        self.left()
        self.board.reverse()
    def up(self):
        self.board.transpose()
        self.left()
        self.board.transpose()
    def down(self):
        self.board.transpose()
        self.board.reverse()
        self.left()
        self.board.reverse()
        self.board.transpose()

    def user_keys(self, key_event):
        if key_event.keysym in ['UP', 'w', 'W']:
            self.up()
        elif key_event.keysym in ['DOWN', 's', 'S']:
            self.down()
        elif key_event.keysym in ['LEFT', 'a', 'A']:
            self.left()
        elif key_event.keysym in ['RIGHT', 'd','D']:
            self.right()





