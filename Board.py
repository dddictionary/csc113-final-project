import tkinter as tk

# Define the dimensions of the game board
BOARD_DIM = 4
CELL_SIZE = 100
PAD_SIZE = 5

class Board(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("2048 Game")
        self.geometry(f"{BOARD_DIM * CELL_SIZE + PAD_SIZE * (BOARD_DIM + 1)}x{BOARD_DIM * CELL_SIZE + PAD_SIZE * (BOARD_DIM + 1)}")
        self.create_board()

    def create_board(self):
        self.board = [[0 for _ in range(BOARD_DIM)] for _ in range(BOARD_DIM)]
        self.tiles = [[None for _ in range(BOARD_DIM)] for _ in range(BOARD_DIM)]

        for row in range(BOARD_DIM):
            for col in range(BOARD_DIM):
                x0 = col * CELL_SIZE + (col + 1) * PAD_SIZE
                y0 = row * CELL_SIZE + (row + 1) * PAD_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                tile = tk.Frame(self, bg="gray", width=CELL_SIZE, height=CELL_SIZE)
                tile.grid(row=row, column=col, padx=PAD_SIZE, pady=PAD_SIZE)
                self.tiles[row][col] = tile


if __name__ == "__main__":
    game_board = Board()
    game_board.mainloop()

# TODO implement merge_tile
# def merge_tile(self,i,j,left):
#     if left == True and j > 0:
#         if self.board[i][j] == self.board[i][j+1]:
#             self.board[i][j] = self.board[i][j] * 2
#             self.board[i][j+1] = 0
#     elif right == True and j < 3:
#         if self.board[i][j] == self.board[i][j-1]:
#             self.board[i][j] = self.board[i][j] * 2
#             self.board[i][j-1] = 0
#     elif up == True and i > 0:
#         if self.board[i][j] == self.board[i+1][j]:
#             self.board[i][j] = self.board[i][j] * 2
#             self.board[i+1][j] = 0
#     else down == True and i < 3:
#         if self.board[i][j] == self.board[i-1][j]:
#             self.board[i][j] = self.board[i][j] * 2
#             self.board[i-1][j] = 0